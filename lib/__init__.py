import sqlite3

CONN = sqlite3.connect('db/movies.db')
CURSOR = CONN.cursor()
