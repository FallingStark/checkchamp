import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from ..riot_api.setup_summoner import get_user
import json


guilds_ids = [528138762006560789, 931591823485468713]


class set_user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="set_user",
        guild_ids=guilds_ids,
        description="give ping of bot",
        options=[
            create_option(
                name="summoner_name",
                required=True,
                description="give your summoner name",
                option_type=3,
            )
        ],
    )
    async def _ping(self, ctx: SlashContext, summoner_name: str):
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
        description="give ping of bot",
    )
    async def get_user(self, ctx: SlashContext):
        with open("data.json", "r") as file:
            content = file.read()
        content = content.replace("'", '"')
        data = json.loads(content)
        try:
            await ctx.send(str(data[str(ctx.author.id)]))
        except:
            await ctx.send("Tu na pas set ton summers")

    @cog_ext.cog_slash(
        name="get_mastery",
        guild_ids=guilds_ids,
        description="give ping of bot",
    )
    async def get_user(self, ctx: SlashContext):
        with open("data.json", "r") as file:
            content = file.read()
        content = content.replace("'", '"')
        data = json.loads(content)
        info = data[str(ctx.author.id)]
        
    


def setup(bot):
    bot.add_cog(set_user(bot))
