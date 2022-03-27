import discord
from discord.ext import commands
import asyncio

class Status(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.client.loop.create_task(status(self))

async def status(self):
    while True:
        await self.client.wait_until_ready()
        member_count = 0
        for i in self.client.guilds:
            member_count += i.member_count
        await self.client.change_presence(activity=discord.Activity(type= discord.ActivityType.watching, name=f"{member_count} User"))
        await asyncio.sleep(15)

def setup(client):
    client.add_cog(Status(client))
