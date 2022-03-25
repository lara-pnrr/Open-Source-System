import discord
from discord.ext import commands

class Main(commands.Bot):
    def __init__(self, command_prefix="!", help_command=None, **options):
        super().__init__(command_prefix, help_command, **options)

client = Main()

@client.event
async def on_ready():
    print("I´m now online!")

client.run("")