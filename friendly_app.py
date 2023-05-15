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
    gift_ideas = GiftRepository.list(friend_id)
    return gift_ideas

@app.route('/api/friends/<friend_id>/gifts', methods=['POST'])
def create_gift(friend_id):
    gift_idea = request.json
    gift_idea['friend_id'] = friend_id
    return GiftRepository.create(gift_idea)

@app.route('/api/friends/<friend_id>/gifts', methods=['DELETE'])
def delete_gift(friend_id):
    gift_idea = request.json
    GiftRepository.delete(gift_idea)
    return ({}, 204)  # unsure of return



# @app.route('/api/friends/<friend_id>/gift_given', methods=['GET'])
# def list_gift_given(friend_id):
#     gift_given = GiftGivenRepository.list(friend_id)
#     return gift_given

# @app.route('/api/friends/<friend_id>/gift_given', methods=['POST'])
# def create_gift_given(friend_id):
#     gift_given = request.json
#     gift_given['friend_id'] = friend_id
#     return GiftGivenRepository.create(gift_given)

# @app.route('/api/friends/<friend_id>/gift_given', methods=['DELETE'])
# def delete_gift_given(friend_id):
#     gift_given = request.json
#     GiftGivenRepository.delete(gift_given)
#     return ({}, 204)  # unsure of return



# @app.route('/api/friends/<friend_id>/gift_received', methods=['GET'])
# def list_gift_received(friend_id):
#     gift_received = GiftGivenRepository.list(friend_id)
#     return gift_received

# @app.route('/api/friends/<friend_id>/gift_received', methods=['POST'])
# def create_gift_received(friend_id):
#     gift_received = request.json
#     gift_received['friend_id'] = friend_id
#     return GiftGivenRepository.create(gift_received)

# @app.route('/api/friends/<friend_id>/gift_received', methods=['DELETE'])
# def delete_gift_received(friend_id):
#     gift_received = request.json
#     GiftGivenRepository.delete(gift_received)
#     return ({}, 204)  # unsure of return