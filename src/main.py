import os
import discord
# import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


class DiscordClient(discord.Client):
    async def on_read(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        match message.content:
            case '!ping':
                await message.reply("pong")


intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)
client.run(TOKEN)
