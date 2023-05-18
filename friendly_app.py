# list of friends
# last time contacted
# frequency of desired contact
# headings or something

# name, contacted log, frequency desired, birthday, last gift received, last gift given

from flask import Flask, request, render_template, g
from markupsafe import escape
import json
import sqlite3
from repository import FriendRepository, ContactLogRepository, GiftRepository



app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/Florida")
def florida():
    return "<p>Welcome to the Florida</p>"


@app.route('/api/friends', methods=['POST'])
def create_friend():
    friend = request.json
    return FriendRepository.create(friend)


@app.route('/api/friends/<friend_id>', methods=['PUT'])
def update_friend(friend_id):
    friend = request.json
    FriendRepository.update(friend)
    return friend


@app.route('/friends', methods=['GET'])
def list_friends():
    friends = FriendRepository.list()
    return render_template('friends.html', friends=friends)


@app.route('/api/friends/<friend_id>', methods=['DELETE'])
def delete_friend(friend_id):
    FriendRepository.delete({'id': friend_id})
    return ({}, 204)


@app.route('/api/friends/<friend_id>/contact_log', methods=['POST'])
def create_contact_log(friend_id):
    friend = request.json
    ContactLogRepository.create(friend)
    return friend




@app.route('/api/friends/<friend_id>/gifts', methods=['GET'])
def list_gift(friend_id):
    return GiftRepository.list(friend_id)

@app.route('/api/friends/<friend_id>/gifts', methods=['POST'])
def create_gift(friend_id):
    gift_idea = request.json
    gift_idea['friend_id'] = friend_id
    return GiftRepository.create(gift_idea)

@app.route('/api/friends/<friend_id>/gifts/<id>', methods=['PUT'])
def update_gift_status(friend_id, id):
    gift = request.json
    gift['id'] = id
    return GiftRepository.update(gift)

@app.route('/api/friends/<friend_id>/gifts/<id>', methods=['DELETE'])
def delete_gift(friend_id, id):
    GiftRepository.delete(id)
    # breakpoint()
    return ({}, 204)