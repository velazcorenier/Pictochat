from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handler.user import UserHandler


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/PhotoMessagingAPP/user', methods=['GET', 'POST'])
def getAllUserName():
    if request.method == 'GET':
        return UserHandler().getAllUser()

if __name__ == '__main__':
    app.run()
