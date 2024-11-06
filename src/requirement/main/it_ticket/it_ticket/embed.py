from tdb import ticket_tab
import discord

class archive_thread_btn(discord.ui.View):
    @discord.ui.button(style=discord.ButtonStyle.blurple, emoji="💾", label="Close")
    async def ar_callback(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.response.send_message(f"## Thread has been closed by {interaction.user.mention}")

        # edit stat inside channel
        tab = ticket_tab(interaction.guild_id)
        tab.ft_close_thread(interaction.channel_id)
        await interaction.channel.edit(
            name=f"[CLOSED]{interaction.channel.name[interaction.channel.name.find("]") + 1:]}",
            locked = True,
            archived = True
        )

class create_thread_btn(discord.ui.View):  # Create a class called MyView that subclasses discord.ui.View
    def __init__(self, *, timeout: float | None = 180, responder : discord.Role | None = None):
        super().__init__(timeout=timeout)
        self.responder = responder

    @discord.ui.button(style=discord.ButtonStyle.primary, emoji="🎟️", label="Create Ticket Here")  # Create a button
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a Thread
        tab = ticket_tab(interaction.guild_id)
        thread = await interaction.channel.create_thread(name="template")
        await thread.edit(name=f"[OPEN]{interaction.user.name}[{thread.id}]")
        await thread.join()
        await thread.add_user(interaction.user)

        # response and delete the response
        await interaction.response.send_message("Thread Created", ephemeral=True)
        await interaction.delete_original_response()

        # Send Embed for Archiving
        await thread.send(
            content=f"{self.responder.mention if self.responder else ""} มีคนกำลังต้องการความช่วยเหลือ",
            embed = discord.Embed(
                title = "**Archive the thread**",
                description = "When finished your question use button below\n to archive thread",
                color=0x025FE5,
            ),
            view = archive_thread_btn()
        )
        tab.ft_ins_thread(thread.id, interaction.user.name,interaction.user.id, True, True, [])

def embed_cmd(client: discord.Client) -> None:
    """init embed command"""

    # Create a slash command
    @client.tree.command(name="ticket", description="Send ticket message")
    async def text_box(interaction: discord.Interaction, header: str = "",descriptions: str = "", link: str = "", mentionrole: discord.Role = None, hex_color: str = ""):
        if interaction.channel.type != discord.ChannelType.text:
            await interaction.response.send_message("## Can't use inside thread")
            return
        if not hex_color:
            hex_color = "3868e0"
        embed = discord.Embed(
            title=header,
            description=descriptions,
            color=discord.Color(int(hex_color, 16)),
        )
        if link:
            embed.set_image(url=f"{link}")
        embed.set_footer(text="made by arabic code team")
        # Send the embed message using interaction.response
        await interaction.response.send_message(embed=embed, view=create_thread_btn(responder=mentionrole))
