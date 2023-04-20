# list of friends
# last time contacted
# frequency of desired contact
# headings or something


from flask import Flask, request, render_template
from markupsafe import escape


friends = []
with open('friends.txt') as friend_file:
    for line in friend_file:
        friends.append(line.strip())


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/Florida")
def florida():
    return "<p>Welcome to the Florida</p>"


@app.route('/api/friends', methods=['POST'])
def create_friend():
    friend = request.json['name']
    
    with open('friends.txt', 'a') as friend_file:
        if friends:
            friend_file.write(f'\n{friend}')
        else:
            friend_file.write(friend)
    friends.append(friend)
    return {'name': friend}


@app.route('/friends', methods=['GET'])
def list_friends():
    return render_template('friends.html', friends=friends)



@app.route('/api/friends/<friend_name>', methods=['DELETE'])
def delete_friend(friend_name):
    if friend_name not in friends:
        return ({}, 404)
    friends.remove(friend_name)

    with open('friends.txt', 'w') as friend_file:
        friend_file.write('\n'.join(friends))
    return ({}, 204)