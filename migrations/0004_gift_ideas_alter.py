import sqlite3
con = sqlite3.connect("friendly_database.db")
cur = con.cursor()

try:

    cur.execute('''
        ALTER TABLE gift_ideas
        ADD status TEXT
        CONSTRAINT chk_status CHECK (status IN ('idea', 'given', 'received'))
    ''')

    con.commit()

finally:
    con.close()

