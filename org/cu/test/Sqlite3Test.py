import unittest
import sqlite3

'''
testing for connecting sqlite3 database
'''
class MyTestCase(unittest.TestCase):
    def test_connect(self):
        conn = sqlite3.connect("../resources/database/job.db")
        conn.close()
        self.assertEqual(True, conn is not None)

    def test_select(self):
        conn = sqlite3.connect("../resources/database/job.db")
        c = conn.cursor()
        cursor = c.execute("select id,title from job_position")
        for row in cursor:
            print(row)
        count = c.execute("select count(1) as num from job_position").fetchone()[0]
        print(count)
        cursor.close()
        c.close()
        conn.close()
        self.assertEqual(True, cursor is not None and count > 0)

    def test_delete(self):
        conn = sqlite3.connect("../resources/database/job.db")
        c = conn.cursor()
        cursor = c.execute("delete from job_position where id =?", (2,))
        count = conn.total_changes
        print(conn.total_changes)
        conn.commit()
        cursor.close()
        c.close()
        conn.close()
        self.assertEqual(True, count > 0)

    def test_insert(self):
        conn = sqlite3.connect("../resources/database/job.db")
        c = conn.cursor()
        cursor = c.execute("insert into job_position(title) values(?)", ("test2",))
        count = conn.total_changes
        print(conn.total_changes)
        conn.commit()
        cursor.close()
        c.close()
        conn.close()
        self.assertEqual(True, count > 0)


if __name__ == '__main__':
    unittest.main()
