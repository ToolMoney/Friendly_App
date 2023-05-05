import sqlite3
con = sqlite3.connect("friendly_database.db")
cur = con.cursor()

try:

    cur.execute('''
    CREATE TABLE IF NOT EXISTS friends2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        last_contacted TEXT,
        frequency TEXT,
        birthday TEXT,
        gift_received TEXT,
        gift_given TEXT
    )''')

    cur.execute(f'''
        INSERT INTO friends2 (
        name,
        last_contacted,
        frequency,
        birthday,
        gift_received,
        gift_given)
        SELECT * FROM friends
    ''')

    cur.execute('''
        DROP TABLE friends 
    ''')

    cur.execute('''
        ALTER TABLE friends2
        RENAME TO friends
    ''')

    con.commit()

finally:
    con.close()