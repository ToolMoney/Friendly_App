import sqlite3
import json

with open('friends.json') as friends_json:
    friends = json.load(friends_json)


con = sqlite3.connect("friendly_database.db")
cur = con.cursor()

for friend in friends:
    if 'lastContacted' in friend:
        last_contacted = f"'{friend['lastContacted']}'"
    else:
        last_contacted = 'NULL'
    cur.execute(f'''
    INSERT INTO friends (name, last_contacted)
    VALUES ('{friend['name']}', {last_contacted});

    ''')

con.commit()


