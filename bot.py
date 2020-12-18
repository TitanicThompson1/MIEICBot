import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from dbfunctions import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='nextExam', help='Responds with the next exam')
async def nextExam(ctx):
    
    server_resp = get_next_exam()
    response = f'The next exam is of {server_resp[0]} at {server_resp[1]}'
    await ctx.send(response)

bot.run(TOKEN)