from ..main import app
import requests
import os


class get_user():
    def __init__(self):
        self.api_key = "RGAPI-b3fd660b-ffdf-4725-a0d8-0b6b0f5d7f83"
        self.header = {"X-Riot-Token": self.api_key}

    def get_summers_id(self, sum_name):
        request_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{sum_name}"
        response = requests.get(request_url, headers=self.header)
        return response