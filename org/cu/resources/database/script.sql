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
INSERT INTO job_position (
                             title,
                             id
                         )
                         VALUES (
                             'job1',
                             1
                         ),
                         (
                             'job2',
                             2
                         ),
                         (
                             'job3',
                             3
                         ),
                         (
                             'job4',
                             4
                         ),
                         (
                             'job5',
                             5
                         ),
                         (
                             'job6',
                             6
                         );