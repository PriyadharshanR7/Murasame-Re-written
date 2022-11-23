import disnake
import aiohttp
from disnake.ext import commands
import requests, json
import jokes
import random
from random import randint
from main import open_account
from main import get_bank_data

async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(aliases=['pussy', 'pussycat'])
    async def cat(self, inter:disnake.CommandInteraction):
        await open_account(inter.author)
        async with inter.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    users = await get_bank_data()
                    data = await r.json()
                    embed = disnake.Embed(title="Hello Mr.Kitty cat!", color=0xb91f1f)
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="meow!!")

                    user = inter.author
                    users[str(user.id)]["Balance"] += 10
                    with open("coins.json", "w") as f:
                        json.dump(users, f)
                    await inter.response.send_message(embed=embed)

    @commands.slash_command(aliases=['doggy', 'dogge'])
    async def dog(self, inter:disnake.CommandInteraction):
        async with inter.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = disnake.Embed(title="Mr.Doggo!", color=0xb91f1f)
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="bark!!")

                    await inter.response.send_message(embed=embed)
                    await open_account(inter.author)

                    users = await get_bank_data()

                    user = inter.author
                    users[str(user.id)]["Balance"] += 10
                    with open("coins.json", "w") as f:
                        json.dump(users, f)
                        

    @commands.slash_command()
    async def poll(self, inter:disnake.CommandInteraction, object1, object2):

        emoji1 = "🍕"
        emoji2 = "🍔"
        embed = disnake.Embed(title = f"Poll by {inter.author.name}", color = 0xb91f1f)
        embed.add_field(name = f"{emoji1} for", value = object1)
        embed.add_field(name = f"{emoji2} for", value = object2 )
        embed.set_footer(text="Murasame")

        msg = await inter.response.send_message(embed=embed)

        await msg.add_reaction(emoji1)
        await msg.add_reaction(emoji2)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command(pass_context=True)
    async def joke(self, inter:disnake.CommandInteraction):

        response = requests.get('https://api.chucknorris.io/jokes/random')
        joke1 = json.loads(response.text)
        the_joke = joke1['value']

        embed = disnake.Embed(title="Random Joke", description = the_joke, color = 0xb91f1f)
        embed.set_footer(text="Murasame")
        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command()
    async def howgay(self, inter:disnake.CommandInteraction, user:disnake.User = None):
        if user is None:
            user = inter.author

        embed = disnake.Embed(title = f"Gay rating of {user.name}", description = f"{user.mention} is {randint(0,100)}% a Gay", color = 0xb91f1f)
        embed.set_footer(text="Murasame")
        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command()
    async def howles(self, inter:disnake.CommandInteraction, user:disnake.User = None):
        if user is None:
            user = inter.author

        embed = disnake.Embed(title = f"Lesbian rating of {user.name}", description = f"{user.mention} is {randint(0,100)}% a Les", color = 0xb91f1f)
        embed.set_footer(text="Murasame")
        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command()
    async def pp(self, inter:disnake.CommandInteraction, user: disnake.User = None):
        if user is None:
            user = inter.author

        list1 = ["8========D","8=======D", "8======D", "8======D", "8=====D", "8====D", "8===D", "8==D", "8=D", "8D"]

        choice = random.choice(list1)

        embed = disnake.Embed(title=f"PP size calculator | {user.name}",
                              description=f"{user.mention}'s pp is {choice} long!!", color=0xb91f1f)
        embed.set_footer(text="Murasame")
        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command(aliases=["cf"])
    async def coinflip(self, inter:disnake.CommandInteraction):
        list1 = ["head", "tail"]
        choice = random.choice(list1)

        embed7 = disnake.Embed(title="", description=f"I chose {choice}",
                                       color=0xb91f1f)

        embed7.set_author(name="Coin Flip!")
        embed7.set_thumbnail(url="https://cdn.discordapp.com/attachments/934777769861206016/937607366617215016/goldcoin1.png")
        embed7.set_footer(text="Murasame")
        await inter.response.send_message(embed=embed7)

        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
                json.dump(users, f)
  
    @commands.slash_command() 
    async def ship(self, inter:disnake.CommandInteraction, member:disnake.User = None):
        if member is None:
            await inter.response.send_message("Provide a valid user to ship with!", ephemeral=True)
            return

        list1 = ["https://cdn.discordapp.com/attachments/941914604089528373/941963753522614313/2Q.png", "https://cdn.discordapp.com/attachments/941914604089528373/941963784338149386/Z.png", "https://cdn.discordapp.com/attachments/941914604089528373/941963797298577418/images.png", "https://cdn.discordapp.com/attachments/941914604089528373/941963830878142464/2Q.png", "https://cdn.discordapp.com/attachments/941914604089528373/941963860364116058/images.png", "https://cdn.discordapp.com/attachments/941914604089528373/941963879091695626/images.png", "https://cdn.discordapp.com/attachments/941914604089528373/941963898901393478/images.png"]
        choice = random.choice(list1)
        embed = disnake.Embed(title = f"{inter.author.name} x {member.name}", description = f"{inter.author.mention} and {member.mention} are {randint(1,100)}% in Love <3", color = 0xeb51f7)
        embed.set_thumbnail(url=choice)

        embed.set_footer(text="Murasame")
        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    

                              
      
  
def setup(bot):
    bot.add_cog(fun(bot))
