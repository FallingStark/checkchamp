"""Start bot"""

import os
from dotenv import load_dotenv
from Bot.main import app

load_dotenv()


def main():
    TOKEN = os.environ.get("TOKEN")
    RIOT_API_KEY = os.environ.get("RIOT_API_KEY")

    bot = app(TOKEN, RIOT_API_KEY)
    bot.run()


if __name__ == "__main__":
    main()
