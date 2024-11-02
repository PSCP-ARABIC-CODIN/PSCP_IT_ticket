import os
import discord

from dotenv import load_dotenv
from discord import ChannelType
from discord.ext import commands

load_dotenv()
intents : discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True

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

# latency
@client.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong! Latency: {latency} ms")

@client.tree.command(name="cleanhouse", description="Archive all acctive thread")
async def clean_thread(interaction : discord.Interaction):
    await interaction.channel.typing()
    for thread in interaction.channel.threads:
        await thread.edit(
            archived = True,
            locked = True
        )
    await interaction.response.send_message("Your home is clean")

@client.tree.command(name="cat", description="cat everywhere")
async def cat(interaction : discord.Interaction):
    await interaction.response.send_message(f"{interaction.channel.threads}")

try:
    # import initialize function of embed
    from embed import embed_cmd
    # pass the client object into the imported function
    embed_cmd(client)
    load_dotenv()
    client.run(os.getenv("TOKEN"))
except Exception as error:
    print(error)
