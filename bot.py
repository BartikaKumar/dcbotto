from dotenv import load_dotenv
import discord
from threading import Thread
import os
from flask import Flask

from commands import *

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

# Get PREFIX from environment variables. If not found, use $.
PREFIX=os.getenv("PREFIX","$")

commands={
    "hello":hello,
    "choose":choose,
    "invite":invite,
    "summon":summon,
    "dm":dm,
}

# called when message sent in server
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    content= message.content.strip() # removes whitespaces in the beginning and end
    if not content.startswith(PREFIX):
        return
    
    #split from length of prefix onward (accounts for prefix with multiple characters)
    parts= content[len(PREFIX):].split()

    if not parts:
        return
    
    command= parts[0].lower()
    args= parts[1:]

    if command in commands:
        await commands[command](message,args,client)

# dummy webserver
app = Flask(__name__)

@app.route("/")
def home():
    return "bot running >.<"

def run_web():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

Thread(target=run_web).start()

client.run(token)
