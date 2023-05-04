import sqlite3
from flask import g

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('friendly_database.db')
    return db


class FriendRepository:
    @staticmethod
    def list():
        rows = get_db().cursor().execute('''
        SELECT name, last_contacted FROM friends;
        ''').fetchall()

        friends = []
        for name, last_contacted in rows:
            friends.append({'name': name, 'lastContacted': last_contacted})
        return friends
    
    @staticmethod
    def create(friend):
        database = get_db()
        database.cursor().execute(f'''
        INSERT INTO friends (name)
        VALUES ('{friend['name']}')
        ''')
        database.commit()

    @staticmethod
    def delete(friend):
        database = get_db()
        database.cursor().execute(f'''
        DELETE FROM friends 
        WHERE name = '{friend['name']}'
        ''')
        database.commit()

    @staticmethod
    def update(friend):
        database = get_db()
        database.cursor().execute(f'''
        UPDATE friends
        SET last_contacted = '{friend['lastContacted']}'
        WHERE name = '{friend['name']}'
        ''')
        database.commit()