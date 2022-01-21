"""Give stats of league player"""

import os
from pprint import pprint
import requests
from dotenv import load_dotenv

__version__ = '1.0'


load_dotenv()
Header = {"X-Riot-Token": os.environ.get("API_KEY")}


class Player:
    """Setup for get league player info"""

    def __init__(self, summonerName):
        """Get basic informations like ID,AccountID and puuid from the League API"""
        self.sum = summonerName
        request_player = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.sum}"
        response = requests.get(request_player, headers=Header)
        self.code = response.status_code
        if self.code == 200:
            content = response.json()
            self.id = content["id"]
            self.accountId = content["accountId"]
            self.puuid = content["puuid"]

    def get_mastery(self):
        """Get all champion mastery entries sorted by number of champion points descending"""
        request_mastery = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{self.id}"
        response = requests.get(request_mastery, headers=Header)
        self.code = response.status_code
        if self.code == 200:
            content = response.json()
            return content

    def get_all_mastery(self):
        """Get a player's total champion mastery score, which is the sum of individual champion mastery levels"""
        request_all_mastery = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{self.id}"
        response = requests.get(request_all_mastery, headers=Header)
        self.code = response.status_code
        if self.code == 200:
            content = response.json()
            return content
