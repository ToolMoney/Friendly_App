import sqlite3
con = sqlite3.connect("friendly_database.db")
cur = con.cursor()

try:

    cur.execute('''
        CREATE TABLE IF NOT EXISTS gift_ideas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gift TEXT NOT NULL,
        friend_id INTEGER NOT NULL,
        FOREIGN KEY (friend_id) REFERENCES friends (id)
        )
    ''')

    con.commit()

finally:
    con.close()