from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
import discord
import os

SERVER = discord.Object(id=1285544666149687396)

class MyClient(discord.Client):
    """Constructor for Client(Bot)"""
    def __init__(self, *, intents: discord.Intents):
        """Initialize and Link command tree"""
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self) # sync command tree

    async def setup_hook(self) -> None:
        """Copy command from global into server"""
        self.tree.copy_global_to(guild=SERVER)
        await self.tree.sync(guild=SERVER)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

#   Slash command example
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

try:
    load_dotenv()
    client.run(os.getenv("TOKEN"))
except Exception as error:
    print(error)
