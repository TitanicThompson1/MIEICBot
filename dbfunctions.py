import sqlite3


def init_database():
    return sqlite3.connect('test.db')



def get_next_exam(conn, discipline: str):
    c = conn.cursor()

    if discipline == None:
        return _any_exam(c)
    
    if not _discipline_exists(c, discipline):
        return "Error"

    return _specific_exam(c, discipline)



def _discipline_exists(c, discipline):
    dscp_upper = discipline.upper()

    tuple_querry = (dscp_upper,)

    c.execute('''
    SELECT * 
    FROM  Discipline
    WHERE Discipline.name=?;
    ''', tuple_querry)

    return c.fetchone() != None


def _specific_exam(c, discipline):
    dscp_upper =discipline.upper()

    tuple_querry = (dscp_upper,)

    c.execute('''
    SELECT name, date 
    FROM Exam, Discipline
    WHERE Exam.idDiscipline=Discipline.idDiscipline AND
            Discipline.name=?
    ORDER BY date(date) 
    ASC Limit 1;
    ''', tuple_querry)

    return c.fetchone()



def _any_exam(c):
    c.execute('''
    SELECT name, date 
    FROM Exam, Discipline
    WHERE Exam.idDiscipline=Discipline.idDiscipline
    ORDER BY date(date) 
    ASC Limit 1;
    ''')
    
    return c.fetchone()


def close_db(conn):
    conn.close()

