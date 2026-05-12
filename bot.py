from dotenv import load_dotenv
import discord
import os

# load env variables
load_dotenv()

# get the bot token
token = os.getenv('TOKEN')

# set message intent
intents = discord.Intents.default()
intents.message_content = True

# init the bot client
client = discord.Client(intents=intents)


# bot startup code
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# called when message sent in server
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)