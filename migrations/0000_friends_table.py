import sqlite3
con = sqlite3.connect("friendly_database.db")
cur = con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS friends (
    name TEXT PRIMARY KEY,
    last_contacted TEXT,
    frequency TEXT,
    birthday TEXT,
    gift_received TEXT,
    gift_given TEXT

)''')

cur.execute('''
INSERT INTO friends (name, birthday)
VALUES ('Skyler', 'February 22');

''')