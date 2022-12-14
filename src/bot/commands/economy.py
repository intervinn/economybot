import disnake
import random
from disnake.ext import commands
from ..db.session import users

class Economy(commands.Cog):

    def __init__(self, bot : commands.InteractionBot):
        self.bot = bot

    async def check_for_user(self, member : disnake.Member) -> dict | None: 
        pattern = {
            "id": member.id,
            "wallet": 0,
            "bank": 0,
            "cool?": True
        }

        user = await users.find_one({"id" : member.id})

        if not user:
            await users.insert_one(
                pattern
            )
            return None
        
        if len(user) != len(pattern)+1: # include _id
            for k,_ in pattern.items():
                if not k in user:
                    user[k] = pattern[k]
        
        await users.find_one_and_replace(
            {"id" : member.id},
            user
        )
        return await users.find_one({"id" : member.id})



    @commands.slash_command(name="balance", description="view your balance")
    async def _balance(self, inter : disnake.ApplicationCommandInteraction) -> None:

        user = await self.check_for_user(inter.author)
        wallet = user["wallet"]
        bank = user["bank"]

        await inter.response.send_message(
            embed=disnake.Embed(
                title="Your money",
                description=
                f"""
                Wallet: `{wallet}`;
                Bank: `{bank}`;
                Total: `{wallet + bank}`;
                """
            )
        )
        

        
    @commands.slash_command(name="work", description="work and get money")
    async def _work(self, inter : disnake.ApplicationCommandInteraction) -> None:

        salary : int = random.randint(1,200)
        wallet : int
        user = await self.check_for_user(inter.author)

        user["wallet"] += salary

        await users.find_one_and_replace(
            {"id" : inter.author.id},
            user,
            upsert=True
        )

        wallet = user["wallet"]

        await inter.response.send_message(
            embed=disnake.Embed(
                title="You worked so hard",
                description=f"You got paid `{salary}`$, and now you have `{wallet}`$"
            )
        )

def setup(bot):
    bot.add_cog(Economy(bot))