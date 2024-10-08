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

class MyView(discord.ui.View):  # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(style=discord.ButtonStyle.primary, emoji="✉️")  # Create a button with the label "✉️" with color Blurple 
    #(you can set text in button by using lebel="brabrabra")
    async def button_callback(self,interaction:discord.Interaction,button:discord.ui.Button):
        # Ensuring a response to the button interaction
        await interaction.response.send_message("Bruh")

#Create a slash command
@client.tree.command(name="button")  # The name of the slash command
async def button(interaction: discord.Interaction):
    # Send an initial message with the button
    await interaction.response.send_message(view=MyView())

try:
    # import initialize function of embed
    from embed import embed_cmd
    # pass the client object into the imported function
    embed_cmd(client)
    load_dotenv()
    client.run(os.getenv("TOKEN"))
except Exception as error:
    print(error)
