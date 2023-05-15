# list of friends
# last time contacted
# frequency of desired contact
# headings or something

# name, contacted log, frequency desired, birthday, last gift received, last gift given

from flask import Flask, request, render_template, g
from markupsafe import escape
import json
import sqlite3
from repository import FriendRepository, ContactLogRepository, GiftIdeaRepository



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




@app.route('/api/friends/<friend_id>/gift_ideas', methods=['GET'])
def list_gift_ideas(friend_id):
    gift_ideas = GiftIdeaRepository.list(friend_id)
    return gift_ideas

@app.route('/api/friends/<friend_id>/gift_ideas', methods=['POST'])
def create_gift_idea(friend_id):
    gift_idea = request.json
    gift_idea['friend_id'] = friend_id
    return GiftIdeaRepository.create(gift_idea)

@app.route('/api/friends/<friend_id>/gift_ideas', methods=['DELETE'])
def delete_gift_idea(friend_id):
    gift_idea = request.json
    GiftIdeaRepository.delete(gift_idea)
    return ({}, 204)  # unsure of return