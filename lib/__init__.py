import sqlite3
# importing sql package

# creating a connection to specific db
CONN = sqlite3.connect('db/movies.db')

# built in method that connections have 
# it looks at data and brings it back 
# creates new rows 
# delete movies 
# it is like our agent 
# it is the way we use sql while in our python file
CURSOR = CONN.cursor()

# the curser is like git add .
# conn = connection is the thing that actually commits it to the db
