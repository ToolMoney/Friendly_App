# list of friends
# last time contacted
# frequency of desired contact
# headings or something

# name, contacted log, frequency desired, birthday, last gift received, last gift given

from flask import Flask, request, render_template, g
from markupsafe import escape
import json
import sqlite3
from repository import FriendRepository






with open('friends.json') as friend_file:
    friends = json.load(friend_file)
    

def sync_friends():
    with open('friends.json', 'w') as friend_file:
        json.dump(friends, friend_file)


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
    FriendRepository.create(friend)
    return friend


@app.route('/api/friends/<friend_name>', methods=['PUT'])
def update_friend(friend_name):
    friend = request.json
    FriendRepository.update(friend)
    return friend


@app.route('/friends', methods=['GET'])
def list_friends():
    friends = FriendRepository.list()
    return render_template('friends.html', friends=friends)


@app.route('/api/friends/<friend_name>', methods=['DELETE'])
def delete_friend(friend_name):
    FriendRepository.delete({'name': friend_name})
    return ({}, 204)