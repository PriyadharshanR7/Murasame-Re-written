import disnake
from disnake.ext import commands
import asyncio
from main import *

class staff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def purge(self, inter:disnake.CommandInteraction , amount:int = None):
        if amount is None:
            amount = 1

        await inter.channel.purge(limit= amount + 1)

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def embed(self, inter:disnake.CommandInteraction, title):
        await inter.channel.send("Process started, answer within a minute!")

        questions = ["Channel it should be sent in?", "Content of the Embed?",
                     "Confirm?"]

        answers = []

        def check(m):
            return m.author == inter.author and m.channel == inter.channel

        for i in questions:
            await inter.channel.send(i)

            try:
                msg = await self.bot.wait_for('message', timeout=60, check=check)
            except asyncio.TimeoutError:
                await inter.channel.send('You didn\'t answer in time, please be quick the next time')
                return
            else:
                answers.append(msg.content)

        
        c_id = answers[0]
        

        channel = self.bot.get_channel(c_id)
        content = answers[1]

        emb = disnake.Embed(title=f"{title}", description=f"{content}", color=0xb31c1c)
        emb.set_footer(text=f"{inter.guild.name}")

        await channel.send(embed=emb)
        await inter.channel.purge(limit=8)
        await inter.response.send_message(f"The embed has been sent in {answers[0]}")


    @commands.slash_command()
    async def osban(self, inter:disnake.CommandInteraction, member:disnake.User=None):
      if member is None:
        await inter.channel.send("Enter a valid user to ban!")

      else: 
        json_string = """{"member.id": 1}"""

        with open("bans.json", "w") as f:
          a_dict = json.dump(json_string, f)
          return True   

        
def setup(bot):
    bot.add_cog(staff(bot))