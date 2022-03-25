from abc import ABC, abstractmethod


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
        return "hello world!!!PHATHtml"  # Query the database here