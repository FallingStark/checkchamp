import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from ..riot_api.all_request import *
import json


guilds_ids = [528138762006560789, 931591823485468713]


class set_user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="set_user",
        guild_ids=guilds_ids,
        description="set your summoner name",
        options=[
            create_option(
                name="summoner_name",
                required=True,
                description="give your summoner name",
                option_type=3,
            )
        ],
    )
    async def set_user(self, ctx: SlashContext, summoner_name: str):
        data = get_user()
        response = data.get_summers_id(summoner_name)
        if response.status_code == 200:
            with open("data.json", "r") as file:
                file_data = file.read()
                file_data = file_data.replace("'", '"')
                data = json.loads(file_data)
            content = response.json()
            data[str(ctx.author.id)] = content
            with open("data.json", "w") as file:
                file.write(str(data))
            await ctx.send("data set")
        else:
            await ctx.send(f"Erreur {response.status_code}")

    @cog_ext.cog_slash(
        name="get_user",
        guild_ids=guilds_ids,
        description="give user info",
    )
    async def get_user(self, ctx: SlashContext):
        with open("data.json", "r") as file:
            content = file.read()
        content = content.replace("'", '"')
        data = json.loads(content)
        functions_mastery = get_mastery()
        functions_rank = get_rank()
        try:
            with open("champion_id.json", "r") as file:
                champ_ids = file.read()
                champ_ids = json.loads(champ_ids)

            user_data = data[str(ctx.author.id)]

            response = functions_mastery.get_summoners_mastery(user_data["id"])
            mastery_data = response.json()
            main_data = mastery_data[0]
            main_id = str(main_data["championId"])
            name_main = champ_ids[main_id]

            response = functions_rank.get_summoners_rank(user_data["id"])
            rank_data = response.json()
            rank_data = rank_data[0]
            rank = f"{rank_data['tier']} {rank_data['rank']} {rank_data['leaguePoints']} LP"

            embed = (
                discord.Embed(title=f"Info sur {user_data['name']}")
                .set_thumbnail(
                    url=f"http://ddragon.leagueoflegends.com/cdn/12.3.1/img/profileicon/{user_data['profileIconId']}.png"
                )
                .add_field(
                    name=f"Level", value=user_data["summonerLevel"], inline=False
                )
                .add_field(
                    name=f"Main {name_main}",
                    value=f"Mastery {main_data['championLevel']} avec {main_data['championPoints']} points",
                    inline=False,
                )
                .add_field(name="Rank", value=rank, inline=False)
                .add_field(name="test", value=f"{rank_data['inactive']}")
            )

            await ctx.send(embed=embed)
        except:
            await ctx.send("Tu na pas set ton summers")

    @cog_ext.cog_slash(
        name="get_mastery",
        guild_ids=guilds_ids,
        description="give info mastery",
    )
    async def get_mastery(self, ctx: SlashContext):
        with open("data.json", "r") as file:
            content = file.read()
        content = content.replace("'", '"')
        data = json.loads(content)
        try:
            with open("champion_id.json", "r") as file:
                champ_ids = file.read()
                champ_ids = json.loads(champ_ids)
            info = data[str(ctx.author.id)]
            functions_mastery = get_mastery()
            response = functions_mastery.get_summoners_mastery(info["id"])
            mastery_data = response.json()
            main_data = mastery_data[0]
            main_id = str(main_data["championId"])
            name_main = champ_ids[main_id]
            embed = discord.Embed(
                title=f"Top 25 des mastery de {info['name']}"
            ).set_thumbnail(
                url=f"http://ddragon.leagueoflegends.com/cdn/12.3.1/img/champion/{name_main}.png"
            )
            for champ in mastery_data:
                champ_want = str(champ["championId"])
                embed.add_field(
                    name=f"Mastery de {champ_ids[champ_want]}",
                    value=f"Mastery {champ['championLevel']} avec {champ['championPoints']} points",
                )
            await ctx.send(embed=embed)
        except Exception as err:
            await ctx.send("Summoner not set (or error)")
            print(err)


def setup(bot):
    bot.add_cog(set_user(bot))
