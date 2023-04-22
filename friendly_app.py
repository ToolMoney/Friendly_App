# list of friends
# last time contacted
# frequency of desired contact
# headings or something

# name, contacted log, frequency desired, birthday, last gift received, last gift given

from flask import Flask, request, render_template
from markupsafe import escape
import json



with open('friends.json') as friend_file:
    friends = json.load(friend_file)
    

def sync_friends():
    with open('friends.json', 'w') as friend_file:
        json.dump(friends, friend_file)


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/Florida")
def florida():
    return "<p>Welcome to the Florida</p>"


@app.route('/api/friends', methods=['POST'])
def create_friend():
    friend = request.json
    friends.append(friend)
    sync_friends()
    return friend


@app.route('/api/friends/<friend_name>', methods=['PUT'])
def update_friend(friend_name):
    for i, friend_dict in enumerate(friends):
        if friend_name == friend_dict['name']:
            friend_index = i
    friend = friends[friend_index]
    print(friends)
    friend_update = request.json
    friend.update(friend_update)
    print(friends)
    sync_friends()
    return friend


@app.route('/friends', methods=['GET'])
def list_friends():
    return render_template('friends.html', friends=friends)


@app.route('/api/friends/<friend_name>', methods=['DELETE'])
def delete_friend(friend_name):
    found = False
    for i, friend_dict in enumerate(friends):
        if friend_dict['name'] == friend_name:
            found = True
            friend_index= i
    if not found:
        return ({}, 404)
    
    del friends[friend_index]
    sync_friends()
    return ({}, 204)