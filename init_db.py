from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as file:
    connection.executescript(file.read())

cursr = connection.cursor()

cursr.execute("INSERT INTO employee (company_name, name, email, mobile, address) VALUES (?, ?, ?, ?, ?)",
                ("Comp 1",  "Employee 1", "test1@gmail.com", "123456789", "Chicago")
            )

connection.commit()
connection.close()