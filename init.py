from dotenv import load_dotenv
import os
import discord

# Set up Intents (SImilar to set up permission for the bot)
#   this'll be use as argument when create object of the client
intents = discord.Intents.default()
intents.message_content = True

# Create Object of the bot
client = discord.Client(intents=intents)

# Event will call after bot have been ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(client.status)

load_dotenv()
client.run(os.getenv("TOKEN"))
