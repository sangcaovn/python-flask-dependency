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