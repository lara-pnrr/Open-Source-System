import sys
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@client.event
async def on_ready():
    print("I´m now online!")

extensionss = ["modules.commands.help"]

if __name__ == '__main__':
    for i in extensionss:
        try:
            client.load_extension(i)
            print(f"{i} was loaded successfully")
        except Exception as i:
            print(f"{i} could not be loaded", file=sys.stderr)

client.run("")