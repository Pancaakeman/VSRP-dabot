import discord
from discord.ext import commands, tasks
from discord import app_commands, Interaction, Embed

class Ping(commands.Cog):  # Initializes Ping Cog
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()  # Syncs commands
        await print(self.__class__.__name__, " is online!")

    @app_commands.command(name="ping", description="Calculates and Send the bots Latency")
    async def ping(self, interaction: Interaction):
        
        embed = Embed(title="Pong 🏓", description=f"Ping is {int(self.bot.latency * 1000)} ms", color=discord.Color.dark_teal())
        embed.set_footer(text="The VSRP Open Source Discord Bot!")
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/15749/15749453.png")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))
