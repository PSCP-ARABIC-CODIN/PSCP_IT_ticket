import discord

class archive_thread_btn(discord.ui.View):
    @discord.ui.button(style=discord.ButtonStyle.blurple, emoji="💾", label="Archive")
    async def ar_callback(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.response.send_message(f"## Thread has been closed by {interaction.user.mention}")

        # edit stat inside channel
        await interaction.channel.edit(
            archived = True,
            locked = True
        )

class create_thread_btn(discord.ui.View):  # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(style=discord.ButtonStyle.primary, emoji="🎟️", label="Create Ticket Here")  # Create a button
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a Thread
        thread = await interaction.channel.create_thread(name="template")
        await thread.edit(name=f"{interaction.user.name}[{thread.id}]")
        await thread.join()
        await thread.add_user(interaction.user)

        # response and delete the response
        await interaction.response.send_message("Thread Created", ephemeral=True)
        await interaction.delete_original_response()

        # Send Embed for Archiving
        await thread.send(
            embed = discord.Embed(
                title = "**Archive the thread**",
                description = "When finished your question use button below\n to archive thread",
                color=0x025FE5,
            ),
            view = archive_thread_btn()
        )

def embed_cmd(client: discord.Client) -> None:
    """init embed command"""

    # Create a slash command
    @client.tree.command(name="ticket", description="Send ticket message")
    async def text_box(interaction: discord.Interaction, text: str = "", link: str = ""):
        if interaction.channel.type != discord.ChannelType.text:
            await interaction.response.send_message("## Can't use inside thread")
            return

        aduse = interaction.user.mention
        embed = discord.Embed(
            description=(
                f"**{aduse}**\n"
                f"**Hello with message \"{text}\"**\n"
                "ต้องการสอบถามพี่ๆ แบบส่วนตัว\n"
                "สามารถกดปุ่มด้านล่างได้เลย !!!"
            ),
            color=0xF75306,  # Orange color
        )
        if link:
            embed.set_image(url=f"{link}")
        embed.set_footer(text="With hate by ...")
        # Send the embed message using interaction.response
        await interaction.response.send_message(interaction.channel.type, embed=embed, view=create_thread_btn())
