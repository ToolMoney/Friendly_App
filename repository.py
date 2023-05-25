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
        SELECT friends.id, name, MAX(timestamp), frequency, birthday
        FROM friends
        LEFT JOIN contact_log ON friends.id = contact_log.friend_id
        GROUP BY friends.id
        ORDER BY timestamp ASC
        ''').fetchall()

        friends = []
        for id, name, last_contacted, frequency, birthday in rows:
            friends.append({
                'id': id, 
                'name': name, 
                'lastContacted': last_contacted, 
                'frequency': frequency, 
                'birthday': birthday, 
            })
        return friends
    
    @staticmethod
    def create(friend):
        database = get_db()
        row = database.cursor().execute(f'''
        INSERT INTO friends (name)
        VALUES ('{friend['name']}')
        RETURNING id, name
        ''').fetchone()

        id, name = row
        friend = {'id': id, 'name': name}
        database.commit()
        return friend

    @staticmethod
    def delete(friend):
        database = get_db()
        database.cursor().execute(f'''
        DELETE FROM friends 
        WHERE id = '{friend['id']}'
        ''')
        database.commit()

    @staticmethod
    def update(friend):
        database = get_db()
        if 'birthday' in friend:
            database.cursor().execute(f'''
            UPDATE friends
            SET birthday = '{friend['birthday']}'
            WHERE id = '{friend['id']}'
            ''')
        if 'frequency' in friend:
            database.cursor().execute(f'''
            UPDATE friends
            SET frequency = '{friend['frequency']}'
            WHERE id = '{friend['id']}'
            ''')
        database.commit()


class ContactLogRepository:
    @staticmethod
    def create(friend):
        database = get_db()
        database.cursor().execute(f'''
        INSERT INTO contact_log (friend_id, timestamp)
        VALUES ({friend['id']}, '{friend['lastContacted']}')
        ''')
        database.commit()


class GiftRepository:
    @staticmethod
    def list(friend_id):
        rows = get_db().cursor().execute(f'''
        SELECT id, gift, friend_id, status FROM gift_ideas
        WHERE friend_id = '{friend_id}'
        ''').fetchall()

        gift_ideas = []
        for id, gift, friend_id, status in rows:
            gift_ideas.append({
                'id': id,
                'gift': gift,
                'friendId': friend_id,
                'status': status
            })
        return gift_ideas
    

    @staticmethod
    def create(gift_idea):
        database = get_db()
        row = database.cursor().execute('''
        INSERT INTO gift_ideas (friend_id, gift, status)
        VALUES (:friend_id, :gift, :status)
        RETURNING id, gift, friend_id, status
        ''', gift_idea).fetchone()

        id, gift, friend_id, status = row
        gift = {'id': id, 'gift': gift, 'friendId': friend_id, 'status': status}
        database.commit()
        return gift
    
    @staticmethod
    def delete(gift_id):
        database = get_db()
        database.cursor().execute(f'''
        DELETE FROM gift_ideas 
        WHERE id = '{gift_id}'
        ''')
        database.commit()

    @staticmethod
    def update(gift):
        database = get_db()
        row = database.cursor().execute('''
        UPDATE gift_ideas
        SET status = :status
        WHERE id = :id
        RETURNING id, gift, friend_id, status
        ''', gift).fetchone()

        id, gift, friend_id, status = row
        gift = {'id': id, 'gift': gift, 'friendId': friend_id, 'status': status}
        database.commit()
        return gift
        