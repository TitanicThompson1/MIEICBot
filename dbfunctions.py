import sqlite3

conn = sqlite3.connect('test.db')



def get_next_exam():
    c = conn.cursor()

    c.execute('''
    SELECT name, date 
    FROM Exam, Discipline
    WHERE Exam.idDiscipline=Discipline.idDiscipline
    ORDER BY date(date) 
    ASC Limit 1;
    ''')

    return c.fetchone()

