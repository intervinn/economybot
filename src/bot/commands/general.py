import disnake
import math
from ..db.session import users
from disnake.ext import commands

class General(commands.Cog):
    
    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name="ping", description="Get bot's latency")
    async def _ping(self, inter : disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            embed=disnake.Embed(title="Pong", description=f"The client's latency is `{math.floor(self.bot.latency * 1000)}`ms")
        )

def setup(bot):
    bot.add_cog(General(bot))