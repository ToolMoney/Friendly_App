import sqlite3
con = sqlite3.connect("friendly_database.db")
cur = con.cursor()

try:

    cur.execute('''
        ALTER TABLE friends
        DROP gift_received
    ''')

    cur.execute('''
        ALTER TABLE friends
        DROP gift_given
    ''')

    con.commit()

finally:
    con.close()

