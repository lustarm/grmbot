import os
import discord
# import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

PREFIX = ";"


class DiscordClient(discord.Client):
    async def on_read(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

        # ew code python ass
        if not message.content or message.content[0] != PREFIX: return

        message_array = message.content[1:]
        message_array = message_array.split()

        match message_array[0]:
            case 'ping': await message.reply("pong")

            case 'tell':
                # Create message into vector
                array = message.content.split()
                array.pop(0)
                await message.reply(' '.join(array))


intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)
client.run(TOKEN)
