"""Main du selecteur"""

from pprint import pprint
from stats import Player
import json


def main():
    """Demande quelle option l'user veut utilisé"""
    choice_bool = False

    #SummonerName = input("Quelle est ton summoner name ? ")
    SummonerName = "FallingSt4rk"
    SummonerData = Player(SummonerName)
    if SummonerData.code != 200:
        print(f"Code : {SummonerData.code}")
        return

    while choice_bool is not True:
        print("Que veut tu faire")
        print("Check tes mastery [1]")
        print("Check mastery score [2]")
        print("Ceck champion mastery [3]")
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
        get_champion_mastery(SummonerData)


def get_mastery(SummonerData):
    content = SummonerData.get_mastery()
    with open("mastery.json", "w") as file:
        content_formated = str(content).replace("'", '"')
        content_formated = content_formated.replace("True", "true")
        content_formated = content_formated.replace("False", "false")
        file.write(content_formated)
    print("Check mastery in mastery.json")


def get_mastery_score(SummonerData):
    content = SummonerData.get_all_mastery()
    print(f"Total champion mastery score : {content}")

def get_champion_mastery(SummonerData):
    content = SummonerData.get_champion_mastery("pyke")


if __name__ == "__main__":
    main()
