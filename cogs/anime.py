import datetime
import disnake
from disnake.ext import commands
import animec
import aiohttp
import random
from random import randint
from main import *


class anime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command()
  async def anime(self, inter: disnake.CommandInteraction, *, anime):
    async with inter.channel.typing():
      try:
        anime = animec.Anime(anime)
      except:
        await inter.response.send_message(embed=disnake.Embed(
          description="No such anime is found!", color=disnake.Colour.random())
                                          )
        return

      if anime.is_nsfw() == True:
        await inter.response.send_message(
          "The given anime is NSFW and cannot be shared the details of!")
        return

      else:

        Genres = anime.genres
        producers = anime.producers

        gen = ','.join([str(elem) for elem in Genres])
        pro = ','.join([str(elem) for elem in producers])
        if anime.is_nsfw() == False:
          s = "No"
        embed = disnake.Embed(title=anime.title_english,
                              url=anime.url,
                              description=f"{anime.description[:200]}...",
                              color=disnake.Colour.random())
        embed.add_field(name="Total Episodes", value=anime.episodes)
        embed.add_field(name="Rating", value=str(anime.rating))
        embed.add_field(name="Genres", value=str(gen))
        embed.add_field(name="Airing time", value=str(anime.aired))
        embed.add_field(name="Broadcast day", value=str(anime.broadcast))
        embed.add_field(name="Popularity", value=str(anime.popularity))
        embed.add_field(name="Ranking", value=str(anime.ranked))
        embed.add_field(name="Producers", value=str(pro))
        embed.add_field(name="NSFW ?", value=s)
        embed.set_thumbnail(url=str(anime.poster))
        embed.set_footer(text="Anime Information | Murasame")

        await inter.response.send_message(embed=embed)

        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 20
        with open("coins.json", "w") as f:
          json.dump(users, f)

  @commands.slash_command()
  async def image(self, inter: disnake.CommandInteraction, *, character):
    async with inter.channel.typing():
      try:
        char = animec.Charsearch(character)
      except:
        await inter.response.send_message(
          embed=disnake.Embed(description="No such character is found!",
                              color=disnake.Colour.random()))
        return

      embed = disnake.Embed(title=char.title,
                            url=char.url,
                            color=disnake.Colour.random())
      embed.set_image(url=char.image_url)
      embed.set_footer(text=", ".join(list(char.references.keys())[:2]))
      await inter.response.send_message(embed=embed)

      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def animenews(self,
                      inter: disnake.CommandInteraction,
                      amount: int = 3):
    async with inter.channel.typing():
      news = animec.Aninews(amount)
      links = news.links
      titles = news.titles
      descriptions = news.description

      embed = disnake.Embed(title="Latest Anime updates!!",
                            color=0xb91f1f,
                            timestamp=datetime.datetime.utcnow())
      embed.set_thumbnail(url=news.images[0])

      for i in range(amount):
        embed.add_field(
          name=f"{i+1}) {titles[i]}",
          value=f"{descriptions[i][:200]}...\n[Read more]({links[i]})",
          inline=False)

      await inter.response.send_message(embed=embed)

      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def waifu(self, inter: disnake.CommandInteraction):
    async with inter.channel.typing():
      embed = disnake.Embed(title="Waifu!", color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.waifu())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)

      await open_account(ctx.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def shinobu(self, inter: disnake.CommandInteraction):
    async with inter.channel.typing():
      embed = disnake.Embed(title="Shinobu!", color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.shinobu())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)

      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def megumin(self, inter: disnake.CommandInteraction):
    async with inter.channel.typing():
      embed = disnake.Embed(title="Megumin!", color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.megumin())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)

      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def random(self, inter: disnake.CommandInteraction):
    async with inter.channel.typing():
      embed = disnake.Embed(title="Random waifu!",
                            color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.random())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)
      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def pat(self,
                inter: disnake.CommandInteraction,
                user: disnake.User = None):
    async with inter.channel.typing():
      if user is None:
        user = inter.author
        return

      embed = disnake.Embed(title=f"{inter.author.name} Pats {user.name}",
                            color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.pat())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)
      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def kiss(self,
                 inter: disnake.CommandInteraction,
                 user: disnake.User = None):
    async with inter.channel.typing():

      if user is None:
        user = inter.author
        return

      embed = disnake.Embed(title=f"{inter.author.name} Kisses {user.name}",
                            color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.kiss())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)

      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def hug(self,
                inter: disnake.CommandInteraction,
                user: disnake.User = None):
    async with inter.channel.typing():
      if user is None:
        user = inter.author
        return

      embed = disnake.Embed(title=f"{inter.author.name} Hugs {user.name}",
                            color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.hug())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)
      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def dance(self, inter: disnake.CommandInteraction):
    async with inter.channel.typing():
      embed = disnake.Embed(title="Waifu dance!",
                            color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.dance())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)

      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)

  @commands.slash_command()
  async def kill(self,
                 inter: disnake.CommandInteraction,
                 user: disnake.User = None):
    async with inter.channel.typing():
      if user is None:
        user = inter.author
        return

      embed = disnake.Embed(title=f"{inter.author.name} Kills {user.name}",
                            color=disnake.Colour.random())
      embed.set_image(url=animec.waifu.Waifu.kill())
      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)

      await open_account(inter.author)

      users = await get_bank_data()

      user = inter.author
      users[str(user.id)]["Balance"] += 20
      with open("coins.json", "w") as f:
        json.dump(users, f)


def setup(bot):
  bot.add_cog(anime(bot))
