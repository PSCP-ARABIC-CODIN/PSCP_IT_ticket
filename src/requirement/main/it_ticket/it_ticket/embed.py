import discord

def embed_cmd(client: discord.Client) -> None:
    """init embed command"""
    class MyView(discord.ui.View):  # Create a class called MyView that subclasses discord.ui.View
        @discord.ui.button(style=discord.ButtonStyle.primary, emoji="✉️")  # Create a button with the label "✉️" with color Blurple 
        #(you can set text in button by using lebel="brabrabra")
        async def button_callback(self,interaction:discord.Interaction,button:discord.ui.Button):
            # Ensuring a response to the button interaction
            await interaction.response.send_message("BRuh")

    # Create a slash command
    @client.tree.command(name="embedstart", description="Send ticket message")
    async def ticket(interaction: discord.Interaction):
        embed = discord.Embed(
            description=(
                "**สอบถามพี่ ๆ แบบส่วนตัว**\n\n"
                "ปัญหา/สอบถามทั่วไป เช่น:\n"
                "• ปัญหาด้านเทคนิค\n"
                "• ปัญหาด้านข้อมูลส่วนตัว\n"
                "• สอบถามรายละเอียดกิจกรรม\n\n"
                "หากต้องการสอบถามพี่ ๆ แบบส่วนตัว สามารถกดปุ่มด้านล่างได้เลย"
            ),
            color=0x2ecc71  # Green color
        )
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_wx9ytkWpaORplO5wMqeYtEtP23Wb3bSigw&s")
        embed.set_footer(text="Testing 101")
        # Send the embed message using interaction.response
        await interaction.response.send_message(embed=embed, view=MyView())
