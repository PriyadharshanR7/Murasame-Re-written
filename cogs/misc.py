import asyncio
import random
from random import randint
import disnake
from disnake.ext import commands
import datetime
from main import *
from disnake.utils import get


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(pass_context=True, aliases = ['av'])
    async def avatar(self, inter:disnake.CommandInteraction, member:disnake.User = None):
        if member is None:
          member = inter.author
        embed = disnake.Embed(title = f"Avatar of {member.name}", color = 0xb91f1f)
        embed.set_image(url = member.avatar_url)
        embed.set_footer(text="Avatar | Murasame")
        await inter.response.send_message(embed=embed)

        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command()
    async def remindme(self, inter:disnake.CommandInteraction, tm=None, *, text):
        if tm is None:
            await inter.response.send_message("Provide a valid amount of time to remind you in!", ephemeral=True)
        elif text is None:
            await inter.response.send_message("Enter a valid text you remind you of!", ephemeral=True)
        else:
            def convert(time1):
                pos = ["s", "m", "h", "d"]

                time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

                unit = time1[-1]

                if unit not in pos:
                    return -1
                try:
                    val = int(time1[:-1])
                except:
                    return -2

                return val * time_dict[unit]

            time1 = convert(tm)

            await inter.channel.send("Reminder set!")

            await asyncio.sleep(time1)

            await inter.channel.send(f"{inter.author.mention}, You reminder for : {text}")

            await open_account(inter.author)

            users = await get_bank_data()

            user = inter.author
            users[str(user.id)]["Balance"] += 10
            with open("coins.json", "w") as f:
                json.dump(users, f)

    @commands.command()
    async def roll(self, inter:disnake.CommandInteraction, target:int = None):
        if target is None:
            target = 100

        num = randint(0,target)

        embed = disnake.Embed(title="Dice rolled", description = f"{inter.author.name} has rolled {num}", color = 0xb91f1f)
        embed.set_footer(text="Murasame")

        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command(aliases = ['whois'])
    async def userinfo(self, inter:disnake.CommandInteraction, member:disnake.User = None):
        if member is None:
            member = inter.author

        embed = disnake.Embed(title=f"Member info | {member.name}", color = 0xb91f1f)

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Issued by {inter.author} | Murasame")
        embed.add_field(name="Tag", value=f"{member}")
        embed.add_field(name="ID", value=f"{member.id}", inline=True)
        embed.add_field(name="Created On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.add_field(name="Joined On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"), inline=True)

        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command()
    async def serverinfo(self, inter:disnake.CommandInteraction):
        embed = disnake.Embed(title = f"Server info | {inter.guild.name}", color = 0xb91f1f)
        embed.set_thumbnail(url = inter.guild.icon.url)
        embed.set_footer(text = f"Issued by {inter.author} | Murasame")

        embed.add_field(name="Server Owner", value=f"{inter.guild.owner}", inline=True)
        embed.add_field(name="Server ID", value=f"{inter.guild.id}", inline=True)
        embed.add_field(name="Members count", value=f"{inter.guild.member_count}", inline=True)
        embed.add_field(name="Channels count", value=f"{len(inter.guild.channels)}", inline=True)
        embed.add_field(name="Text channels", value=f"{len(inter.guild.text_channels)}", inline=True)
        embed.add_field(name="Voice channels", value=f"{len(inter.guild.voice_channels)}", inline=True)
        embed.add_field(name="Roles", value=f"{len(inter.guild.roles)}", inline=True)

        await inter.response.send_message(embed=embed)
        await open_account(inter.author)

        users = await get_bank_data()

        user = inter.author
        users[str(user.id)]["Balance"] += 10
        with open("coins.json", "w") as f:
            json.dump(users, f)

    """"@commands.command()
    async def suggest(self,ctx, suggestion = None):
        if suggestion is None:
            await ctx.replly("Provide a valid suggestion!")

        embed = discord.Embed(title = f"Suggestion from {ctx.author}", description = f"{suggestion}", color = 0xb31c1c)

        embed2 = discord.Embed(title= "", description="Sent the suggestion to developer!", color = 0xb31c1c)
        await ctx.send(embed=embed2)

        for guild in bot.guilds:
            dev = discord.utils.get(guild.members, "752403250975604756")

            await dev.send(embed=embed)"""
    @commands.slash_command(aliases=['membercn'])
    async def membercount(self, inter:disnake.CommandInteraction):
      embed = disnake.Embed(title=f"{inter.guild.name} | Member Count", description = f"Current member count -> {inter.guild.member_count}", color = disnake.Colour.random())

      embed.set_footer(text="Murasame")

      await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(misc(bot))



