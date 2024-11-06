import os
import discord
import enum

from dotenv import load_dotenv
from discord.ext import commands
from tdb import ticket_tab

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
async def on_message(message : discord.Message):
    if message.author == client.user:
        return

    cur_channel = message.channel
    if cur_channel.type == discord.ChannelType.private_thread:
        tab = ticket_tab(message.guild.id)
        tab.ft_update_participant(cur_channel.id, message.author.name)



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

class console_opt(enum.Enum):
    log = 1
    clear = 2

@client.tree.command(name="console", description="list all log of thread")
async def lst_thrd(interaction : discord.Interaction, option : console_opt):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("## Console avaliable for administrator only!")
        return
    tab = ticket_tab(interaction.guild_id)
    match option:
        case console_opt.log:
            if not tab:
                await interaction.response.send_message("No Table Exist")
            else:
                msg = ""
                for rec in tab.ft_get_all():
                    msg += str(rec) + "\n"
                await interaction.response.send_message(msg if msg else "Nothing exist in table")
        case console_opt.clear:
            tab.ft_clear()
            await interaction.response.send_message("Table have been clear")
        case _:
            await interaction.response.send_message("Option Error")

@client.tree.command(name="log_all", description="log every records in the server")
async def cb(interaction : discord.Interaction):
    tab = ticket_tab(interaction.guild_id)
    if not tab:
        await interaction.response.send_message("No Table Exist")
    else:
        msg = ""
        for rec in tab.ft_get_all():
            msg += str(rec) + "\n"
        await interaction.response.send_message(msg if msg else "Nothing exist in table")

@client.tree.command(name="log_user", description="log specific user")
async def cb(interaction : discord.Interaction, user : discord.User):
    tab = ticket_tab(interaction.guild_id)
    msg = ""
    for obj in tab.ft_get_by_user(user.id):
        msg += str(obj) + "\n"
    await interaction.response.send_message(msg if msg else f"No record from {user.name} in table")

@client.tree.command(name="log_thread", description="Log specific thread")
async def cb(interaction : discord.Interaction, thread : discord.Thread):
    tab = ticket_tab(interaction.guild_id)
    res = tab.ft_get_by_thread(thread.id)
    await interaction.response.send_message(res if res else "This Thread isn't record in table")

@client.tree.command(name="log_stat", description="Log by thread status")
async def cb(interaction : discord.Interaction, status : bool):
    tab = ticket_tab(interaction.guild_id)
    msg = ""
    for obj in tab.ft_get_by_stat(status):
        msg += str(obj) + "\n"
    await interaction.response.send_message(msg if msg else "None of specific thread exist")

try:
    # import initialize function of embed
    from embed import embed_cmd
    # pass the client object into the imported function
    embed_cmd(client)
    load_dotenv()
    client.run(os.getenv("TOKEN"))
except Exception as error:
    print(error)
