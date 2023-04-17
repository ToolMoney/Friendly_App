# list of friends
# last time contacted
# frequency of desired contact
# be able to go to get request page after post
# see list of friends in bulleted list
# add additional friends from get reqeust page
# headings or something


from flask import Flask, request

friends = []
with open('friends.txt') as friend_file:
    for line in friend_file:
        friends.append(line)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
    <h1 style="color: rebeccapurple;">World of Friends</h1>
    <h2>Hellow, World!</h2>
    <form action="friends" method="POST">
    <input type="text" name="friend_name" />
    <input type="submit" value="Add a Friend"/> </form>
    '''

@app.route("/Florida")
def florida():
    return "<p>Welcome to the Florida</p>"

@app.route('/friends', methods=['POST'])
def create_friend():
    friend = request.form['friend_name']
    
    with open('friends.txt', 'a') as friend_file:
        if friends:
            friend_file.write(f'\n{friend}')
        else:
            friend_file.write(friend)
    friends.append(friend)
    return f'''
    <h2>Friend Added!</h2>
    <p>{friend} should be added to your list of friends!</p>
    <form method="GET">
    <input type="submit" value="List of Friends" /> </form>
    '''

@app.route('/friends', methods=['GET'])
def list_friends():
    
    string_to_return = ''
    for friend in friends:
        string_to_return += f'<li>{friend}</li>\n'
    return f'''
    <ul>{string_to_return}</ul>
        <form action="/friends" method="POST">
        <input type="text" name="friend_name" />
        <input type="submit" value="Add Another Friend?"/> </form>
        '''
