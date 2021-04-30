# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')

@bot.command()
async def cld(ctx, member):
	quote= "waiter bhaiya {} ka cheque la do".format(member)
	await ctx.send(quote)

@bot.command()
async def gaandu(ctx):
	quote = "@{} tu gaandu".format(ctx.author)
	await ctx.send(quote)


bot.run(TOKEN)