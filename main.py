# main.py
import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
my_secret = os.environ['discord-token']

bot = commands.Bot(command_prefix='-')


@bot.command()
async def cld(ctx, member):
  cheque = discord.File("cheque.png")   
  quote= "waiter bhaiya {} ka cheque la do\nwaiter:".format(member)
  await ctx.send(quote, file = cheque)

@bot.command()
async def gaandu(ctx):
	quote = "@{} tu gaandu".format(ctx.author)
	await ctx.send(quote)

keep_alive()
bot.run(my_secret)