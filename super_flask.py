# list of friends
# last time contacted
# frequency of desired contact


from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hellow, World!</p>"

@app.route("/Florida")
def florida():
    return "<p>Welcome to the Florida</p>"

@app.route('/friends', methods=['POST'])
def create_friend():
    return request.data
