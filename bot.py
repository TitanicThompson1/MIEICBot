import os

from discord.ext import commands
from dotenv import load_dotenv

from dbfunctions import *
from bot_aux import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='nextExam', help='[discipline] Gets with the next exam')
async def nextExam(ctx, discipline: str = None):
    conn = connect_database()
    
    server_resp = get_next_exam(conn, discipline)
    if server_resp == "Error":
        raise commands.CommandError()

    await send_resp_nextexam(ctx, server_resp, discipline != None)
    
    close_db(conn)


@bot.command(name='allExams', help='[discipline] Gets all exams')
async def allExams(ctx, discipline: str = None):
    conn = connect_database()
    
    server_resp = get_all_exams(conn, discipline)
    if server_resp == "Error":
        raise commands.CommandError()
    

    await send_resp_allexams(ctx, server_resp, discipline != None)
    
    close_db(conn)



@bot.command(name='nextDeadline', help='Responds with the next exam')
async def nextDeadline(ctx, discipline: str = None):
    conn = connect_database()
    
    server_resp = get_next_deadline(conn, discipline)
    if server_resp == "Error":
        raise commands.CommandError()
    

    await send_resp_nextdd(ctx, server_resp, discipline != None)
    
    close_db(conn)




@nextExam.error
async def nextExam_error(ctx, error):
    await ctx.send("I'm sorry, but that discipline does not exist!")


@allExams.error
async def allExam_error(ctx, error):
    await ctx.send("I'm sorry, but that discipline does not exist!")


bot.run(TOKEN)