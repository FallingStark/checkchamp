import requests

Header ={
    "X-Riot-Token": "RGAPI-3d246307-bbdb-420a-8e50-22cbeb2bbbf9"
}


class Player():
    def __init__(self,summonerName):
        """Get basic informations like ID,AccountID and puuid from the League API"""
        self.sum = summonerName
        request_player = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ str(self.sum)
        response = requests.get(request_player,headers=Header)
        content = response.json()
        self.id = content['id']
        self.accountId = content['accountId']
        self.puuid = content['puuid']
    def get_championmastery():
        """"""
        

Sum = Player("TheOrjis")