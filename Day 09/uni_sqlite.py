#SQLite Uni

import os
import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_University1' )

c = conn.cursor()
c.execute ("""CREATE TABLE student_cred(
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_Roll_No INTEGER,
          Student_Branch TEXT
          )""")

c.execute("INSERT INTO student_cred VALUES ('Pulkit Mathur', 20, 129, 'CSE')")
c.execute("INSERT INTO student_cred VALUES ('Jon Snow', 26, 130, 'CSE')")
c.execute("INSERT INTO student_cred VALUES ('Sansa Stark', 24, 131, 'CSE')")
c.execute("INSERT INTO student_cred VALUES ('Daenerys Targaryen', 26, 132, 'CSE')")
c.execute("INSERT INTO student_cred VALUES ('Arya Stark', 22, 133, 'IT')")
c.execute("INSERT INTO student_cred VALUES ('Bran Stark', 20, 134, 'IT')")
c.execute("INSERT INTO student_cred VALUES ('Tyrion Lannister', 31, 135, 'ECE')")
c.execute("INSERT INTO student_cred VALUES ('Lord Varys', 40, 136, 'ECE')")

c.execute("SELECT * FROM student_cred")
df = DataFrame(c.fetchall())
df.columns = ["Student_Name","Student_age","Student_Roll_No","Student_Branch"]

conn.commit()
conn.close()