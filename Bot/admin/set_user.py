import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option


guilds_ids = [528138762006560789, 931591823485468713]

class set_user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ping", guild_ids=guilds_ids, description="give ping of bot")
    async def _ping(self, ctx: SlashContext):
        await ctx.send(f"Ping : {self.bot.latency*1000}ms")


def setup(bot):
    bot.add_cog(set_user(bot))