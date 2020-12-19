async def send_resp_nextexam(ctx, database_resp, has_discipline):
    """This functions sends a message to discord with the date of the next exam

    Parameters:
    ctx : The context (provided by discord)

    database_resp (tuple) : the response of the database with the next exam date

    has_discipline (bool) : If the user provided a discipline

    """
    
    response = ''
    if database_resp == None and not has_discipline:
        response = 'There aren\'t any more exams! Enjoy your vacations :partying_face:'

    elif database_resp == None and has_discipline:  
        response = 'This class does not have any more exams! You\'re free!'

    elif has_discipline:
        response = f'The next exam of {database_resp[0]} is at {database_resp[1]}'

    else:
        response = f'The next exam is of {database_resp[0]} at {database_resp[1]}'

    await ctx.send(response)


async def send_resp_allexams(ctx, database_resp, has_discipline):
    """This functions sends a message to discord with the dates of all exams

    Parameters:
    ctx : The context (provided by discord)
    
    database_resp (tuple) : the response of the database with all exams dates

    has_discipline (bool) : If the user provided a discipline

    """

    response = ''
    if database_resp == None and not has_discipline:
        response = 'There aren\'t any more exams! Enjoy your vacations :partying_face:'

    elif database_resp == None and has_discipline:  
        response = 'This class does not have any more exams! You\'re free!'

    else:
        for exam in database_resp:
            response = response + f'{exam[0]} - {exam[1]}\n'

    await ctx.send(response)
    

async def send_resp_nextdd(ctx, database_resp, has_discipline):

    """This functions sends a message to discord with the date of the next deadline

    Parameters:
    ctx : The context (provided by discord)
    
    database_resp (tuple) : the response of the database with the date of the next deadline

    has_discipline (bool) : If the user provided a discipline

    """

    response = ''
    if database_resp == None and not has_discipline:
        response = 'There aren\'t any more assigments! Enjoy your vacations :partying_face:'
    elif database_resp == None and has_discipline:  
        response = 'This class does not have any more assigments! You\'re free!'
    elif has_discipline:
        response = f'The next assigments of {database_resp[0]} is due to {database_resp[1]}'
    else:
        response = f'The next assigment is of {database_resp[0]} and it\'s due to {database_resp[1]}'

    await ctx.send(response)


async def send_resp_alldd(ctx, database_resp, has_discipline):
    """This functions sends a message to discord with the dates of all deadlines

    Parameters:
    ctx : The context (provided by discord)
    
    database_resp (tuple) : the response of the database with all deadline dates

    has_discipline (bool) : If the user provided a discipline

    """

    response = ''
    if database_resp == None and not has_discipline:
        response = 'There aren\'t any more assigments! Enjoy your vacations :partying_face:'
    elif database_resp == None and has_discipline:  
        response = 'This class does not have any more assigments! You\'re free!'
    else:
        for deadline in database_resp:
            response = response + f'{deadline[0]} - {deadline[1]}\n'

    await ctx.send(response)