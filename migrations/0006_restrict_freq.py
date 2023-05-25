import sqlite3
con = sqlite3.connect("friendly_database.db")
cur = con.cursor()

try:

    cur.execute('''
        ALTER TABLE friends
        ADD frequency2 DECIMAL(4, 2)
        CONSTRAINT chk_freq CHECK (frequency2 BETWEEN 0 and 24)
    ''')

    cur.execute('''
        UPDATE friends
        SET frequency2 = CAST(frequency AS DECIMAL)
        WHERE frequency IS NOT NULL
    ''')

    cur.execute('''
        ALTER TABLE friends
        DROP frequency
    ''')

    cur.execute('''
        ALTER TABLE friends
        RENAME COLUMN frequency2 TO frequency
    ''')

    con.commit()

finally:
    con.close()