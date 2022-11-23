import disnake
from disnake.ext import commands
import json
import os


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def help(self, inter:disnake.CommandInteraction):
        with open("json/help.json") as f:
            data = json.load(f)
        helpemb = disnake.Embed(title="Murasame | Help Panel", description="List of currently available command Genres!",
                                color=0xb91f1f)
        helpemb.set_image(url="https://cdn.discordapp.com/attachments/881562029972938802/942006840064094248/banner.png")
        helpemb.set_footer(text="Murasame")
        helpemb.set_thumbnail(url=inter.guild.icon.url)
        data = json.load(open("json/help.json"))
        for key, value in data.items():
            helpemb.add_field(name=key, value=value, inline=False)
        await inter.response.send_message(embed=helpemb)

    @commands.slash_command()
    async def mischelp(self, inter:disnake.CommandInteraction):

        with open("json/misc.json") as f:
            data = json.load(f)
        helpemb = disnake.Embed(title="Murasame | Help Panel",
                                description="List of currently available `Misc` commands!",
                                color=0xb91f1f)
        helpemb.set_image(url="https://media.discordapp.net/attachments/942007568836988958/942044820082417674/misc.png")
        helpemb.set_footer(text=f"Issued by {inter.author.name} | Murasame",
                           icon_url=inter.author.avatar.url)
        helpemb.set_thumbnail(url=inter.guild.icon.url)
        data = json.load(open("json/misc.json"))
        for key, value in data.items():
            helpemb.add_field(name=key, value=value, inline=False)
        await inter.response.send_message(embed=helpemb)

    @commands.slash_command()
    async def funhelp(self, inter:disnake.CommandInteraction):

        with open("json/fun.json") as f:
            data = json.load(f)
        helpemb = disnake.Embed(title="Murasame | Help Panel",
                                description="List of currently available `Fun` commands!",
                                color=0xb91f1f)
        helpemb.set_image(url="https://media.discordapp.net/attachments/942007568836988958/942044819864289290/fun.png")
        helpemb.set_footer(text=f"Issued by {inter.author.name} | Murasame",
                           icon_url=inter.author.avatar.url)
        helpemb.set_thumbnail(url=inter.guild.icon.url)
        data = json.load(open("json/fun.json"))
        for key, value in data.items():
            helpemb.add_field(name=key, value=value, inline=False)
        await inter.response.send_message(embed=helpemb)


    @commands.slash_command()
    async def animehelp(self, inter:disnake.CommandInteraction):

        with open("json/anime.json") as f:
            data = json.load(f)
        helpemb = disnake.Embed(title="Murasame | Help Panel",
                                description="List of currently available `Anime` commands!",
                                color=0xb91f1f)
        helpemb.set_image(url="https://media.discordapp.net/attachments/942007568836988958/942044819654594590/anime.png")
        helpemb.set_footer(text=f"Issued by {inter.author.name} | Murasame",
                           icon_url=inter.author.avatar.url)
        helpemb.set_thumbnail(url=inter.guild.icon.url)
        data = json.load(open("json/anime.json"))
        for key, value in data.items():
            helpemb.add_field(name=key, value=value, inline=True)
        await inter.response.send_message(embed=helpemb)

def setup(bot):
    bot.add_cog(help(bot))