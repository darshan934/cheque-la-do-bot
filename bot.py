# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content == '-check la do':
		repsonse = "bhaiya iska cheque la do"
		await message.channel.send(repsonse)
client.run(TOKEN)