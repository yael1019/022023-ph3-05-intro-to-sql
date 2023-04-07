from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title, year):
        self.id = None
        self.title = title
        self.year = year

    def __repr__(self):
        return f'<Movie id={self.id} title={self.title} runtime={self.runtime}>'

# object relational mapping / ORM 
# everytime i have a table in my db, there is a class i use in python to match up with that table
    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            year INTEGER
        )
        """
        CURSOR.execute(sql)

