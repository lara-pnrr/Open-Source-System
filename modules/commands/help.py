import discord
from discord.ext import commands
from discord.commands import slash_command

from utils.Buttons import HelpMenu

### Cog Class ###

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    ### Slash ###
    @slash_command(guild_ids=[953379025311641640])
    async def help(self, ctx: commands.Context):
        """Its a help menu"""

        site = discord.Embed(description="Development: <@728224308312146011>", colour=discord.Color.light_gray())
        if ctx.author.avatar is not None:
            site.set_author(name="1/2 | Startsite", icon_url=ctx.author.avatar.url)
        else:
            site.set_author(name="1/2 | Startsite")
        
        if ctx.guild.icon is not None:
            site.set_thumbnail(url = ctx.guild.icon.url)

        site2 = discord.Embed(description="Development: <@728224308312146011>", colour=discord.Color.light_gray())
        if ctx.author.avatar is not None:
            site2.set_author(name="2/2 | Startsite", icon_url=ctx.author.avatar.url)
        else:
            site2.set_author(name="2/2 | Startsite")
        
        if ctx.guild.icon is not None:
            site.set_thumbnail(url = ctx.guild.icon.url)

        
        pages = [site, site2]
        await ctx.respond(embed=site, view=HelpMenu(pages, ctx.author))
    
    ### Prefix. Example:  !help###
    @commands.command(name="help")
    async def help1(self, ctx: commands.Context):
        site = discord.Embed(description="Development: <@728224308312146011>", colour=discord.Color.light_gray())
        if ctx.author.avatar is not None:
            site.set_author(name="1/2 | Startsite", icon_url=ctx.author.avatar.url)
        else:
            site.set_author(name="1/2 | Startsite")
        
        if ctx.guild.icon is not None:
            site.set_thumbnail(url = ctx.guild.icon.url)

        site2 = discord.Embed(description="Development: <@728224308312146011>", colour=discord.Color.light_gray())
        if ctx.author.avatar is not None:
            site2.set_author(name="2/2 | Startsite", icon_url=ctx.author.avatar.url)
        else:
            site2.set_author(name="2/2 | Startsite")
        
        if ctx.guild.icon is not None:
            site.set_thumbnail(url = ctx.guild.icon.url)

        
        pages = [site, site2]
        await ctx.send(embed=site, view=HelpMenu(pages, ctx.author))

def setup(client):
    client.add_cog(Help(client))
