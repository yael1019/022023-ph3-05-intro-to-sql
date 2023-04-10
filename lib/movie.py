from . import CONN
from . import CURSOR

# as an orm im creating a one-to-one relationship
# we are taking a bunch of rows from db and can create a list of python objects from those rows 
# or we can take a python obj and set it as a row in our db

class Movie:
    def __init__(self, title, year, id = None):
        # we want to start an id as none
        # sql (our db) assigns our id's
        # signaling an intent that a movie will have an id 
        # like a placeholder
        self.id = None
        self.title = title
        self.year = year

    def __repr__(self):
        # repr fn will show this string instead of object location in memory
        return f'<Movie id={self.id} title={self.title} year={self.year} >'

# object relational mapping / ORM 
# everytime i have a table in my db, there is a class i use in python to match up with that table
# decorator allows me to call this fn on the class
    @classmethod
    def create_table(cls):
        # sql is creating a table with these columns
        sql = """ CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            year INTEGER
        )
        """
        # the cursor is comming from a diff file
        # this is what is actually making our table in the db
        # this gets commited right away
        CURSOR.execute(sql)

    # take attributes from the instance and add it to our table
    def save(self):
        sql = """
            INSERT INTO movies (title, year)
            VALUES (?, ?)
        """
        # we put question marks in place of where our values go
        # we do not use {self.title} because sql does not read that properly
        # the question marks are the safe way to do this

        # cursor will take a second argument passing in the title and year
        # the order in which you list the values matter 
        CURSOR.execute(sql, [self.title, self.year])
        # the curser added our change/row
        # we want to commit the change to the db
        CONN.commit()
        # this will return the id
        # setting the id of the instance 
        self.id = CURSOR.execute('SELECT * FROM movies ORDER BY id DESC LIMIT 1').fetchone()[0]

    #we are looking to get all of the movies 
    @classmethod
    def fetch_all(cls):
        sql = """
            SELECT * FROM movies
        """
        all = CURSOR.execute(sql).fetchall()
    # how do we take all the data from db and map them (show a list of data)
        # we need to map through the list all - the movies that were returned from cursor.execute
        # we loop through it and make a new instance of each by calling Movie
        # we append the instance to a new array
        # this is to make sure we get all of the movies and do not miss any even though the instances for these prob already exist, we just make the insatnce again
        movie_list = []
        for movie_data in all:
            movie = Movie(movie_data[1], movie_data[2])
            movie.id = movie_data[0]
            movie_list.append(movie)
        return movie_list






# to see the table in the terminal 
    # var = CURSOR.execute('SELECT * FROM movies')
    # res.fetchall()
    # or fetchone() will get the first result u see
    # res.fetchall()[-1] will you give you the last movie or CURSOR.execute('SELECT * FROM movies ORDER BY id DESC LIMIT 1').fetchone()
    # we can add index 0 to the end of that to get the id out of the tuple that is returned
