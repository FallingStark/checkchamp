"""
    Setup all needed for work
"""

import os

os.system("cls")

TOKEN = input("Token : ")
RIOT_API_KEY = input("Riot api key : ")

with open(".env", "w") as file:
    file.write(f"TOKEN={TOKEN}\nRIOT_API_KEY={RIOT_API_KEY}")
