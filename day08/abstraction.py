from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class PostgreSQL(Database):
    def connect(self):
        print("Connected to PostgreSQL database")


db = PostgreSQL()
db.connect()
