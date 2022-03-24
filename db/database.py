from abc import ABC, abstractmethod
import json
import requests 

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

    def get(self):
        #return "hello world!!!"  # Query the database here

        url = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'

        res=requests.api.get(url)
        if(res.status_code):
            print (res.json())
            return res.json().get("list")

        return []