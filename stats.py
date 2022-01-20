import os
import requests
from dotenv import load_dotenv

load_dotenv()
Header ={
    "X-Riot-Token": os.environ.get("API_KEY")
}


class Player():
    def __init__(self,summonerName):
        """Get basic informations like ID,AccountID and puuid from the League API"""
        self.sum = summonerName
        request_player = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ str(self.sum)
        response = requests.get(request_player,headers=Header)
        self.code = response.status_code
        if self.code == 200:
            content = response.json()
            self.id = content['id']
            self.accountId = content['accountId']
            self.puuid = content['puuid']