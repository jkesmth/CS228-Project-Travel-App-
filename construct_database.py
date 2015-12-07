import sqlite3 as lite
import sys
import os

# Set our working directory to our project folder

os.chdir(sys.path[0])





# Values of venues and venue_data tables

venues = (
    (1, 'Aurora Inn'),
    (2, 'Dories'),
    (3, 'Well'),
    (4, 'Market'),
    (5, 'Grind'),
    (6, 'Fargo'),
    (7, 'D Hall'),
    (8, 'Pumpkin'),
)

venue_data = (
    (1, 30),
    (2, 10),
    (3, 7),
    (4, 4),
    (5, 6),
    (6, 20),
    (7, 8),
    (8, 25)
)

# Connect to our database

con = lite.connect('test_database.db')

# Initialize values
# Deleting tables if they exist because we are remaking them

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS venues")
    cur.execute("CREATE TABLE venues(Id INT, name TEXT)")
    cur.executemany("INSERT INTO venues VALUES(?, ?)", venues)

    cur.execute("DROP TABLE IF EXISTS venue_data")
    cur.execute("CREATE TABLE venue_data(Id INT, cost INT)")
    cur.executemany("INSERT INTO venue_data VALUES(?, ?)", venue_data)



    
    
