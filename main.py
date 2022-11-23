import disnake
from disnake.ext import commands
import os
import json
import keep_alive

keep_alive.keep_alive()

bot = commands.Bot(command_prefix=";", case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name="Murasame"))
    print("Murasame has logged in!")


@bot.slash_command()
async def balance(inter: disnake.CommandInteraction, person:disnake.User=None):

    if person is None:
      person = inter.author
      
    await open_account(person)

    users = await get_bank_data()
    user = person
    wallet_amt = users[str(user.id)]["Balance"]
    embed = disnake.Embed(title="Balance!", color=disnake.Colour.red())
    embed.add_field(name="wallet", value=wallet_amt)
    await inter.response.send_message(embed=embed)


@bot.slash_command()
async def vote(inter:disnake.CommandInteraction):
    if inter.guild.id == "941914602776715294":
        await open_account(inter.author)

        users = await get_bank_data()

        earnings = 100

        await inter.response.send_message("Success!")

        channel = bot.get_channel(942059787422679060)

        em = disnake.Embed(
            title="Vote has been registered",
            description=f"{inter.author.mention} has voted for the bot",
            color=0xb31c1c)
        await channel.send(embed=em)
        user = inter.author
        users[str(user.id)]["Balance"] += earnings

        with open("coins.json", "w") as f:
            json.dump(users, f)

    else:
        await inter.response.send_message("Join the community server to use this command!")


@bot.slash_command()
@commands.is_owner()
async def give(inter:disnake.CommandInteraction, member: disnake.User, amount: int):

    await open_account(member)

    users = await get_bank_data()

    await inter.response.send_message("Done!")

    user = member
    users[str(user.id)]["Balance"] += amount
    with open("coins.json", "w") as f:
        json.dump(users, f)


async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Balance"] = 0
        users[str(user.id)]["ban"] = 0

    with open("coins.json", "w") as f:
        json.dump(users, f)
        return True


async def get_bank_data():
    with open("coins.json", "r") as f:
        users = json.load(f)

    return users
  
@bot.slash_command()
async def loadcog(inter:disnake.CommandInteraction, cog):
    if inter.author.id == 752403250975604756:
        bot.load_extension(f"cogs.{cog}")
        await inter.response.send_message("loaded")
    else:
        await inter.response.send_message("No sufficient permissions.")


@bot.slash_command(pass_context=True)
async def unloadcog(inter:disnake.CommandInteraction, cog):
    if inter.author.id == 752403250975604756:
        bot.unload_extension(f"cogs.{cog}")
        await inter.response.send_message("unloaded")
    else:
        await inter.response.send_message("No sufficient permissions")


@bot.slash_command(pass_context=True)
async def reloadcog(inter:disnake.CommandInteraction, cog):
    if inter.author.id == 752403250975604756:
        bot.unload_extension(f"cogs.{cog}")
        bot.load_extension(f"cogs.{cog}")
        await inter.response.send_message("reloaded")
    else:
        await inter.response.send_message("No sufficient permissions")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
bot.run("OTQxODk0NDI1MjM0MjU1OTM0.Ygclig.zkVRILxNyaVEafPdNSP2qcJtMCI")
