"""Main du selecteur"""

from pprint import pprint
from datetime import datetime
import os
from time import time
from stats import Player
import json
import locale


def main():
    """Demande quelle option l'user veut utilisé"""
    choice_bool = False
    os.system("cls")
    locale.setlocale(locale.LC_ALL, "")

    # SummonerName = input("Quelle est ton summoner name ? ")
    SummonerName = "FallingSt4rk"
    SummonerData = Player(SummonerName)
    if SummonerData.code != 200:
        print(f"Code : {SummonerData.code}")
        return

    while choice_bool is not True:
        print("Que veut tu faire")
        print("Check tes mastery [1]")
        print("Check mastery score [2]")
        print("Check champion info [3]")
        try:
            choice = int(input(""))
        except:
            choice = 0
        if 1 <= choice <= 3:
            choice_bool = True
    print(f"ton choice est {choice}")
    if choice == 1:
        get_mastery(SummonerData)
    if choice == 2:
        get_mastery_score(SummonerData)
    if choice == 3:
        champion_wanted_name = input("Champion Name Wanted : ")
        get_champion_mastery(SummonerData, champion_wanted_name)


def get_mastery(SummonerData):
    content = SummonerData.get_mastery()
    if SummonerData.code != 200:
        print(f"Code : {SummonerData.code}")
        return f"Code : {SummonerData.code}"
    with open("mastery.json", "w") as file:
        content_formated = str(content).replace("'", '"')
        content_formated = content_formated.replace("True", "true")
        content_formated = content_formated.replace("False", "false")
        file.write(content_formated)
    print("Check mastery in mastery.json")


def get_mastery_score(SummonerData):
    content = SummonerData.get_all_mastery()
    if SummonerData.code != 200:
        print(f"Code : {SummonerData.code}")
        return f"Code : {SummonerData.code}"
    print(f"Total champion mastery score : {content}")


def get_champion_mastery(SummonerData, champion_wanted_name):
    content = SummonerData.get_champion_mastery(champion_wanted_name)
    if SummonerData.code != 200:
        print(f"Code : {SummonerData.code} \nInvalide champion name")
        return f"Code : {SummonerData.code}"
    with open("champion_id.json", "r") as file:
        file_content = file.read()
    list_champion = json.loads(file_content)
    for champion_id in list_champion:
        if int(champion_id) == content["championId"]:
            champion_name = list_champion[champion_id]

    mastery = content["championLevel"]
    mastery_points = content["championPoints"]
    last_play_timestamp = content["lastPlayTime"]
    last_play_timestamp = int(str(last_play_timestamp)[:-3])
    last_play_time = datetime.fromtimestamp(float(last_play_timestamp))
    last_play_time = last_play_time.strftime("%H:%M:%S - %d/%m/%Y")
    print("")
    print("--------------------------------------")
    print(f"{champion_name}")
    print(f"Mastery {mastery}")
    print(f"Mastery points : {mastery_points:n} pts")
    print(f"Last play time : {last_play_time}")
    print("--------------------------------------")
    print("")


if __name__ == "__main__":
    main()
