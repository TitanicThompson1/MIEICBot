import sqlite3


def connect_database():
    return sqlite3.connect('test.db')



def get_next_exam(conn, discipline: str):
    c = conn.cursor()

    if discipline == None:
        return _any_exam(c)
    
    if not _discipline_exists(c, discipline):
        return "Error"

    return _next_exam_dscpl(c, discipline)



def get_all_examss(conn, discipline: str):
    c = conn.cursor()

    if discipline == None:
        return _all_exams(c)
    
    if not _discipline_exists(c, discipline):
        return "Error"

    return _all_examss_dscpl(c, discipline)


def _all_exams(c):
    c.execute('''
    SELECT name, date 
    FROM Exam, Discipline
    WHERE Exam.idDiscipline=Discipline.idDiscipline
    ORDER BY date(date) 
    ASC;
    ''')
    
    return c.fetchall()


def _discipline_exists(c, discipline):
    dscp_upper = discipline.upper()

    tuple_querry = (dscp_upper,)

    c.execute('''
    SELECT * 
    FROM  Discipline
    WHERE Discipline.name=?;
    ''', tuple_querry)

    return c.fetchone() != None


def _all_examss_dscpl(c, discipline):
    dscp_upper =discipline.upper()

    tuple_querry = (dscp_upper,)

    c.execute('''
    SELECT name, date 
    FROM Exam, Discipline
    WHERE Exam.idDiscipline=Discipline.idDiscipline AND
            Discipline.name=?
    ORDER BY date(date) 
    ASC;
    ''', tuple_querry)

    return c.fetchall()




def _next_exam_dscpl(c, discipline):
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

