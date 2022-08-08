DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    mobile NUMBER NOT NULL,
    address TEXT NOT NULL
)