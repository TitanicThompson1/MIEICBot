import os

from discord.ext import commands
from dotenv import load_dotenv

from dbfunctions import *
from bot_aux import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')




@bot.command(name='nextExam', help='[class] Gets with the next exam in general or of a certain class')
async def nextExam(ctx, discipline: str = None):
    """This function implements the nextExam command

    Parameters:
    ctx : The context

    class (str) : Optional. If present, searches the next exam of a specific class

    """

    conn = connect_database()
    
    database_resp = get_next_exam(conn, discipline)
    if database_resp == "Error":
        raise commands.CommandError()

    await send_resp_nextexam(ctx, database_resp, discipline != None)
    
    close_db(conn)


@nextExam.error
async def nextExam_error(ctx, error):
    await ctx.send("I'm sorry, but that class does not exist!")




@bot.command(name='allExams', help='[discipline] Gets all exams in general or of a certain class')
async def allExams(ctx, discipline: str = None):
    """This function implements the allExams command

    Parameters:
    ctx : The context

    class (str) : Optional. If present, searches all exams of a specific class

    """
    conn = connect_database()
    
    database_resp = get_all_exams(conn, discipline)
    if database_resp == "Error":
        raise commands.CommandError()
    

    await send_resp_allexams(ctx, database_resp, discipline != None)
    
    close_db(conn)

@allExams.error
async def allExam_error(ctx, error):
    await ctx.send("I'm sorry, but that class does not exist!")



@bot.command(name='nextDeadline', help='[class] Gets the next deadline in general or of a certain class')
async def nextDeadline(ctx, discipline: str = None):
    """This function implements the nextDeadline command

    Parameters:
    ctx : The context

    class (str) : Optional. If present, searches the next deadline of a specific class
    """

    conn = connect_database()
    
    database_resp = get_next_deadline(conn, discipline)
    if database_resp == "Error":
        raise commands.CommandError()
    

    await send_resp_nextdd(ctx, database_resp, discipline != None)
    
    close_db(conn)


@nextDeadline.error
async def nextDeadline_error(ctx, error):
    await ctx.send("I'm sorry, but that class does not exist!")



@bot.command(name='allDeadlines', help='[class] Gets all deadlines in general or of a certain class')
async def allDeadlines(ctx, discipline: str = None):
    """This function implements the allDeadlines command

    Parameters:
    ctx : The context

    class (str) : Optional. If present, searches all the deadline of a specific class
    """

    conn = connect_database()
    
    database_resp = get_all_deadlines(conn, discipline)

    if database_resp == "Error":
        raise commands.CommandError()
    

    await send_resp_alldd(ctx, database_resp, discipline != None)
    
    close_db(conn)

@allDeadlines.error
async def allDeadlines_error(ctx, error):
    await ctx.send("I'm sorry, but that class does not exist!")





bot.run(TOKEN)