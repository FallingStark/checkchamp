"""Main du selecteur"""

from pprint import pprint
from stats import Player
import json

from test import Sum


def main():
    """Demande quelle option l'user veut utilisé"""
    choice_bool = False

    SummonerName = input("Quelle est ton summoner name ? ")
    SummonerData = Player(SummonerName)
    if SummonerData.code != 200:
        print(f"Code : {SummonerData.code}")
        return

    while choice_bool is not True:
        print("Que veut tu faire")
        print("Check tes stats lol [1]")
        try:
            choice = int(input(""))
        except:
            choice = 0
        if 1 <= choice <= 2:
            choice_bool = True
    print(f"ton choice est {choice}")
    if choice == 1:
        print("")


if __name__ == "__main__":
    main()