from abc import ABC, abstractmethod
import aiohttp
import json

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
        async with aiohttp.ClientSession() as session:
            pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
            async with session.get(pokemon_url, ssl=False) as resp:
                pokemon = await resp.json()
                return pokemon
                # Query the database here

    async def get_weather_data(self):
        print("\nData Weather\n")
        api_key = '35de292dfc07f722d7563237777d7b9e'
        city_name = 'London'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        weather_url = base_url + 'appid=' + api_key + '&q=' + city_name

        async with aiohttp.ClientSession() as session:
            async with session.get(weather_url, ssl=False) as resp:
                weather_json = await resp.json()
                return weather_json
                # Query the database here

    async def get_general_weather_data(self):
        print("\nGeneral Data Weather\n")
        weather_url = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
        async with aiohttp.ClientSession() as session:
            async with session.get(weather_url, ssl=False) as resp:
                weather_json = await resp.json()
                return weather_json
                # Query the database here