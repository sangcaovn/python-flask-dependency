from injector import inject

from db.database import DatabaseBase

import asyncio
import aiohttp
import json

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()

    def get_git_data():
        pass

    async def push_data_api_pokemon(self):
        async with aiohttp.ClientSession() as session:
            pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                pokemon_json = json.dumps(pokemon, indent=4)
                return pokemon_json

    async def get_current_weather(self):
        token = "95289c9af590f050a40422493b1e9565"
        async with aiohttp.ClientSession() as session:
            weather_url = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
            async with session.get(weather_url) as resp:
                weather = await resp.json()
                weather = weather["list"]
                    # weather = weather["weather"]
                weather_json = json.dumps(weather, indent=4)
                return weather
