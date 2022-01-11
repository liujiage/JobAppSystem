import os
import sqlite3
from abc import ABCMeta, abstractmethod
from sqlite3 import Cursor, Connection

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Handle connect database,parent class,provide basically access database the methods, like query,execute...
'''
class DaoService(metaclass=ABCMeta):

    # init connect the database
    def __init__(self):
        self._filename = os.path.dirname(os.path.dirname(__file__)) + '/resources/database/job.db'
        self._conn = sqlite3.connect(self._filename)
        # init necessary tables
        self.__initTables()

    # query data
    @abstractmethod
    def query(self, value) -> list:
        pass

    # delete data
    @abstractmethod
    def delete(self, value) -> int:
        pass

    # create or modify data
    @abstractmethod
    def updateOrInsert(self, value) -> int:
        pass

    # connect database
    @property
    def conn(self) -> Connection:
        if self._conn is None:
            print("connect is null create a new instance")
            self._conn = sqlite3.connect(self._filename)
        return self._conn

    # close database
    def close(self):
        if self._conn is not None:
            print("close current database connect")
            self._conn.close()
            self._conn = None

    # fetch all data
    def fetch(self, sql) -> list:
        c = self.conn.cursor()
        rs = c.execute(sql).fetchall()
        c.close()
        return rs

    # get one data, like get count or state data
    def fetchOneInt(self, sql) -> int:
        c = self.conn.cursor()
        rs = c.execute(sql).fetchone()
        c.close()
        return rs[0]

    # execute sql script like create,insert and update
    def execute(self, sql) -> int:
        c = self.conn.cursor()
        c.execute(sql)
        rs = self.conn.total_changes
        self._conn.commit()
        return rs

    # init database
    def __initTables(self):
        c = self.conn.cursor()
        count = c.execute("SELECT COUNT(*) as count FROM sqlite_master where type='table' and name='job_apply'").fetchone()[0]
        if count == 1:
            c.close()
            return
        # starting init tables
        c.executescript('''
        CREATE TABLE job_apply (
    id                  VARCHAR (100)  NOT NULL
                                       PRIMARY KEY,
    name                VARCHAR (50),
    create_time         DATETIME       DEFAULT (CURRENT_TIMESTAMP)
                                       NOT NULL,
    position            VARCHAR (50),
    expected_salary     DOUBLE         DEFAULT (0),
    availability_months INT            DEFAULT (0),
    content             VARCHAR (5000),
    review_id           VARCHAR (100)  UNIQUE,
    review_officer      VARCHAR (50),
    review_outcome      VARCHAR (50)   DEFAULT none,
    review_reason       VARCHAR (200),
    review_time         DATETIME
);
CREATE TABLE job_position (
    id    INTEGER      PRIMARY KEY
                       NOT NULL,
    title VARCHAR (50) UNIQUE
                       NOT NULL
);
INSERT INTO job_position (title,id) VALUES ('job1', 1),('job2', 2),('job3', 3),('job4', 4),('job5', 5);
                      ''')
        print("init tables successful.")
        self._conn.commit()
        c.close()


