import sqlite3

conn = sqlite3.connect('test.db')


conn.execute('''INSERT INTO Discipline(name, academicYear) VALUES ('PLOG', 3)''')       # 1
conn.execute('''INSERT INTO Discipline(name, academicYear) VALUES ('RCOM', 3)''')       # 2
conn.execute('''INSERT INTO Discipline(name, academicYear) VALUES ('ESOF', 3)''')       # 3
conn.execute('''INSERT INTO Discipline(name, academicYear) VALUES ('LAIG', 3)''')       # 4
conn.execute('''INSERT INTO Discipline(name, academicYear) VALUES ('LTW', 3)''')        # 5


conn.execute('''INSERT INTO Exam(idDiscipline, date, duration) VALUES (2, '2021-01-20 11:30', '1h30')''')
conn.execute('''INSERT INTO Exam(idDiscipline, date, duration) VALUES (3, '2021-01-12 17:30', '1h30')''')
conn.execute('''INSERT INTO Exam(idDiscipline, date, duration) VALUES (1, '2021-01-08 17:30', '1h30')''')

conn.execute('''INSERT INTO Assigment(idDiscipline, date) VALUES (1, '2021-01-04')''')
conn.execute('''INSERT INTO Assigment(idDiscipline, date) VALUES (3, '2020-12-18')''')
conn.execute('''INSERT INTO Assigment(idDiscipline, date) VALUES (4, '2020-01-03')''')

conn.commit()


conn.close()




