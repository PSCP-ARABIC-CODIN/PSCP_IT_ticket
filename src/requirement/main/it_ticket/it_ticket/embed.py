import discord

def embed_cmd(client: discord.Client) -> None:
    """init embed command"""
    class MyView(discord.ui.View):  # Create a class called MyView that subclasses discord.ui.View
        @discord.ui.button(style=discord.ButtonStyle.primary, emoji="🎟️", label="Create Ticket Here")  # Create a button
        async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
            # Ensuring a response to the button interaction
            await interaction.response.send_message("English or Spanish?")
            # Attempt to create a thread [Ja]
            channel = client.get_channel(1290323018102476811)
            thread = await channel.create_thread(name="UES", message=None, )
            thread.join()
            await thread.send("Pls wait for TA to respond")
            await thread.add_user(interaction.user)

    # Create a slash command
    @client.tree.command(name="ticket", description="Send ticket message")
    async def text_box(interaction: discord.Interaction, text: str, link: str):
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
        embed.set_image(url=f"{link}")
        embed.set_footer(text="With hate by Sapsereechai")
        # Send the embed message using interaction.response
        await interaction.response.send_message(embed=embed, view=MyView())
