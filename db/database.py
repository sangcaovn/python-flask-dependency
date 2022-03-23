from abc import ABC, abstractmethod
import json
import aiohttp

class DatabaseBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get(self):
        pass


class PostgresDatabase(DatabaseBase):
    def __init__(self):
        super().__init__()

    def connect(self):
        # TODO: implementation for a Postgres database connection
        print("Successfully connected to Postgres database!")

    async def get(self):
        # return "hello world!!!"  # Query the database here
        async with aiohttp.ClientSession() as session:
            pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
            async with session.get(pokemon_url,ssl=False) as resp:
                pokemon = await resp.json()
                return pokemon