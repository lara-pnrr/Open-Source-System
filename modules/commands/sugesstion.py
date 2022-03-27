import discord
from discord.ext import commands
from discord.commands import slash_command
import datetime

class Sugesstion(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @slash_command(guild_ids=[953379025311641640])
    async def sugesstion(self, ctx: commands.Context, sugesstion: discord.Option(str, "Write a suggestion", required=True), channel: discord.Option(discord.TextChannel, "Choose in which channel the proposal should be sent", required=True)):
        """Send a sugesstion"""
        sugesstion_embed = discord.Embed(title=f"Sugesstion from {ctx.author}", description=sugesstion, colour=discord.Color.blurple(), timestamp=datetime.datetime.now())
        if ctx.author.avatar is not None:
            sugesstion_embed.set_thumbnail(url=ctx.author.avatar.url)
        if ctx.guild.icon is not None:
            sugesstion_embed.set_footer(text="Created at", icon_url=ctx.guild.icon.url)
        else:
            sugesstion_embed.set_footer(text="Created at")
        
        message = await channel.send(embed = sugesstion_embed)
        await message.add_reaction("⭐")
        await message.add_reaction("❌")
        await ctx.respond(f"The suggestion was successfully sent in {channel.mention}", ephemeral=True)
        
            



def setup(client):
    client.add_cog(Sugesstion(client))