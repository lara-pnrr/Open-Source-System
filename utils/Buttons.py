from tkinter.ttk import Style
import discord
from discord.ui.button import ButtonStyle
from discord.ui import View

class HelpMenu(View):
    def __init__(self, pages, member, *items):
        super().__init__(*items)
        self.pages = pages
        self.i = 0
        self.member = member

    @discord.ui.button(label="Back", style=ButtonStyle.blurple, emoji="◀", custom_id="HelpMenuBack")
    async def callback_back(self, button: discord.Button, interaction: discord.Interaction):
        if not self.member == interaction.user:
            await interaction.response.send_message(content="You cannot use the menu", ephemeral=True)
            return
        
        if self.i > 0:
            self.i -= 1
            await interaction.response.edit_message(embed=self.pages[self.i])

    @discord.ui.button(label="Next", style=ButtonStyle.blurple, emoji="▶", custom_id="HelpMenuNext")
    async def callback_next(self, button: discord.Button, interaction: discord.Interaction):
        if not self.member == interaction.user:
            await interaction.response.edit_message(content="You cannot use the menu", ephemeral=True)
            return
        if self.i < 1:
            self.i += 1
            await interaction.response.edit_message(embed=self.pages[self.i])