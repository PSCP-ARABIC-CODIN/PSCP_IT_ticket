import os
import discord

from dotenv import load_dotenv
from discord import ChannelType
from discord.ext import commands

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(
    command_prefix = '<COMMANDS>',
    intents = intents,
    activity = discord.Game('on Vscode')
)

@client.event
async def on_ready():

    try:
        n_sync = await client.tree.sync()
        print(f'Synced: {n_sync} commands')

    except Exception as e:
        print(f'Exception detected while syncing the commands: \n{e}')
    
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

#   respond message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

#   Slash command example
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@client.tree.command()
async def setroom(interaction: discord.Interaction, channel: discord.TextChannel, thread: discord.Thread):
    """Says hello!"""
    await interaction.response.send_message(f'{interaction.channel_id}')

client.run(os.getenv("TOKEN"))
