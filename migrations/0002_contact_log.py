import sqlite3
con = sqlite3.connect("friendly_database.db")
cur = con.cursor()

try:

    cur.execute('''
        CREATE TABLE IF NOT EXISTS contact_log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        friend_id INTEGER,
        FOREIGN KEY (friend_id) REFERENCES friends (id)
        )
    ''')

    cur.execute('''
        INSERT INTO contact_log (timestamp, friend_id)
        SELECT last_contacted, id FROM friends
    ''')

    cur.execute('''
        ALTER TABLE friends
        DROP COLUMN last_contacted
    ''')

    con.commit()

finally:
    con.close()