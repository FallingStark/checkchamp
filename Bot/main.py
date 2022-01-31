import discord
from discord.ext import commands
from discord_slash import SlashCommand
import os


class app:
    def __init__(self, token, riot_api_key):
        self.token = token
        self.riot_api_key = riot_api_key

        intents = discord.Intents.default()
        intents.members = True

        DESCRIPTION = """An example Client to showcase the discord.ext.commands extension
        module.
        There are a number of utility commands being showcased here."""

        self.client = commands.Bot(
            command_prefix="!",
            description=DESCRIPTION,
            intents=intents,
            owner_ids=[212593654819323904],
        )
        self.slash = SlashCommand(self.client, sync_commands=True)

        category_list = ["admin", "events"]
        self.add_category(category_list)

    def add_category(self, category_list):
        for category in category_list:
            for file in os.listdir(f"./Bot/{category}"):
                if file.endswith(".py"):
                    name = file[:-3]
                    self.client.load_extension(f"Bot.{category}.{name}")

    def run(self):
        self.client.run(self.token)
