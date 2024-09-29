from dotenv import load_dotenv
import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def main():
    """void"""
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
        print(client.status)

if __name__ == "__main__":
    main()
    load_dotenv()
    client.run(os.getenv("TOKEN"))
else:
    print("This module not for import")