import sqlite3


def connect_database():
    """Connects to the database and returns the connection to it

    Returns:
    The database connections

    """
    return sqlite3.connect('test.db')


def close_db(conn):
    """Closes the connection with the database

    Parameters:

    conn : the connection with the database

    """
    conn.close()


def get_next_exam(conn, discipline: str):

    """Gets the next exam from the database. 

    Parameters:
    conn : the connection with the database

    discipline (str) : the name of the discipline, if the user provided it. None otherwise
    
    Returns:
    A tuple with (name_of_discipline, date_of_exam,). The string "error", if the discipline does not exist
    """
    c = conn.cursor()

    if discipline == None:
        return _next_exam(c)
    
    if not _discipline_exists(c, discipline):
        return "Error"

    return _next_exam_dscpl(c, discipline)



def get_all_exams(conn, discipline: str):

    """Gets all the exams from the database. 

    Parameters:
    conn : the connection with the database

    discipline (str) : the name of the discipline, if the user provided it. None otherwise
    
    Returns:
    A list of tuples with (name_of_discipline, date_of_exam,). The string "error", if the discipline does not exist
    """

    c = conn.cursor()

    if discipline == None:
        return _all_exams(c)
    
    if not _discipline_exists(c, discipline):
        return "Error"

    return _all_exams_dscpl(c, discipline)


def get_next_deadline(conn, discipline):
    """Gets the next deadline from the database. 

    Parameters:
    conn : the connection with the database

    discipline (str) : the name of the discipline, if the user provided it. None otherwise
    
    Returns:
    A tuple with (name_of_discipline, date_of_deadline,). The string "error", if the discipline does not exist
    """


    c = conn.cursor()

    if discipline == None:
        return _next_deadline(c)
    
    if not _discipline_exists(c, discipline):
        return "Error"

    return _next_dd_dscpl(c, discipline)


def get_all_deadlines(conn, discipline):
    """Gets all the deadlines from the database. 

    Parameters:
    conn : the connection with the database

    discipline (str) : the name of the discipline, if the user provided it. None otherwise
    
    Returns:
    A list of tuples with (name_of_discipline, date_of_deadline,). The string "error", if the discipline does not exist
    """

    c = conn.cursor()

    if discipline == None:
        return _all_deadlines(c)

    if not _discipline_exists(c, discipline):
        return "Error"

    return _all_dd_dscpl(c, discipline)



def _next_deadline(c):
    """Executes the query to get the next deadline 

    Parameters:

    c : the cursor of the database
    
    Returns:
    A tuple with (name_of_discipline, date_of_deadline,).
    """

    c.execute('''
    SELECT name, date 
    FROM Assigment, Discipline
    WHERE Assigment.idDiscipline=Discipline.idDiscipline
    ORDER BY date(date) 
    ASC Limit 1;
    ''')
    
    return c.fetchone()


def _all_deadlines(c):
    """Executes the query to get all deadlines

    Parameters:

    c : the cursor of the database
    
    Returns:
    A list of tuples with (name_of_discipline, date_of_deadline,). 
    """

    c.execute('''
    SELECT name, date 
    FROM Assigment, Discipline
    WHERE Assigment.idDiscipline=Discipline.idDiscipline
    ORDER BY date(date) ASC;
    ''')

    return c.fetchall()


def _all_exams(c):
    """Executes the query to get all exams

    Parameters:

    c : the cursor of the database
    
    Returns:
    A list of tuples with (name_of_discipline, date_of_exam,). 
    """

    c.execute('''
    SELECT name, date 
    FROM Exam, Discipline
    WHERE Exam.idDiscipline=Discipline.idDiscipline
    ORDER BY date(date) 
    ASC;
    ''')
    
    return c.fetchall()


def _discipline_exists(c, discipline):
    """Executes the query to determine if a discipline exists

    Parameters:

    c : the cursor of the database

    discipline (str) : the discipline
    
    Returns:
    True if the discipline exists. False otherwise.
    """

    dscp_upper = discipline.upper()

    tuple_querry = (dscp_upper,)

    c.execute('''
    SELECT * 
    FROM  Discipline
    WHERE Discipline.name=?;
    ''', tuple_querry)

    return c.fetchone() != None


def _all_dd_dscpl(c, discipline):
    """Executes the query to get all deadlines of a discipline

    Parameters:

    c : the cursor of the database

    discipline (str) : the discipline
    
    Returns:
    A list of tuples with (name_of_discipline, date_of_deadline,). 
    """


    dscp_upper = discipline.upper()

    tuple_querry = (dscp_upper,)

    c.execute('''
    SELECT name, date 
    FROM Assigment, Discipline
    WHERE Assigment.idDiscipline=Discipline.idDiscipline AND
            Discipline.name=?
    ORDER BY date(date) ASC;
    ''', tuple_querry)

    return c.fetchall()



def _all_exams_dscpl(c, discipline):
    """Executes the query to get all exams of a discipline

    Parameters:

    c : the cursor of the database

    discipline (str) : the discipline
    
    Returns:
    A list of tuples with (name_of_discipline, date_of_exam,). 
    """

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
    """Executes the query to get the next exam of a discipline

    Parameters:

    c : the cursor of the database

    discipline (str) : the discipline
    
    Returns:
    A tuple with (name_of_discipline, date_of_exam,). 
    """

    dscp_upper = discipline.upper()

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



def _next_dd_dscpl(c, discipline):
    """Executes the query to get the next deadline of a discipline

    Parameters:

    c : the cursor of the database

    discipline (str) : the discipline
    
    Returns:
    A tuple with (name_of_discipline, date_of_deadline,). 
    """

    dscp_upper = discipline.upper()

    tuple_querry = (dscp_upper,)

    c.execute('''
    SELECT name, date 
    FROM Assigment, Discipline
    WHERE Assigment.idDiscipline=Discipline.idDiscipline AND
            Discipline.name=?
    ORDER BY date(date) 
    ASC Limit 1;
    ''', tuple_querry)

    return c.fetchone()    



def _next_exam(c):
    """Executes the query to get the next exam

    Parameters:

    c : the cursor of the database
    
    Returns:
    A tuple with (name_of_discipline, date_of_deadline,). 
    """

    c.execute('''
    SELECT name, date 
    FROM Exam, Discipline
    WHERE Exam.idDiscipline=Discipline.idDiscipline
    ORDER BY date(date) 
    ASC Limit 1;
    ''')
    
    return c.fetchone()




