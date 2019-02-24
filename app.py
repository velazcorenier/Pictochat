from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handler.user import UserHandler
from handler.chat import ChatHandler

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Pictochat/user', methods=['GET', 'POST'])
def getAllUserName():
    if request.method == 'GET':
        return UserHandler().getAllUser()

@app.route('/Pictochat/chat', methods=['GET','POST'])
def getAllChatName():
    if request.method == 'GET':
        return ChatHandler().getAllChat()

if __name__ == '__main__':
    app.run()
