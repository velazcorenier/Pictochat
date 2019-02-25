from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handler.user import UserHandler
from handler.Chat import ChatHandler
from handler.ContactList import ContactListHandler

app = Flask(__name__)
CORS(app)


@app.route('/')  # OK
def home():
    return "Welcome to Pictochat!"


@app.route('/Pictochat/')  # OK
def homeforApp():
    return "Welcome to Pictochat"


# TODO: Implement Dashboard
# @app.route('/Pictochat/dashboard')  # OK
# def dashboardsiplay():
#     handler = DashboardHandler()
#     return handler.dashboard()


@app.route('/Pictochat/users', methods=['GET', 'POST'])
def getAllUserName():
    if request.method == 'GET':
        return UserHandler().getAllUser()


@app.route('/Pictochat/user/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return UserHandler().getUserById(uid)
    elif request.method == 'PUT':
        return UserHandler().updateUser(uid, request.form)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Pictochat/users/chat/<int:chatId>', methods=['GET', 'POST'])
def getAllUserByChat(chatId):
    if request.method == 'GET':
        return UserHandler().getAllUserByChat(chatId)


@app.route('/Pictochat/user/<int:uid>/contacts', methods=['GET', 'POST'])
def getUserContacts(uid):
    if request.method == 'GET':
        return ContactListHandler().getContactsByUserId(uid)

############################################################
# CHAT ROUTES - Renier

@app.route('/Pictochat/chat', methods=['GET', 'POST'])
def getAllChatName():
    if request.method == 'GET':
        return ChatHandler().getAllChat()

@app.route('/Pictochat/chat/<int:chat_id>/participant', methods=['GET', 'POST'])
def getChatParticipants(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatParticipant(chat_id)

@app.route('/Pictochat/chat/<int:chat_id>/post', methods=['GET', 'POST'])
def getChatPost(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatPost(chat_id)

@app.route('/Pictochat/chat/<int:chat_id>/message', methods=['GET', 'POST'])
def getChatMessage(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatAllMessage(chat_id)

@app.route('/Pictochat/chat/<int:chat_id>/media', methods=['GET', 'POST'])
def getChatMedia(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatMedia(chat_id)
############################################################

## KAKI
## KAKI2

if __name__ == '__main__':
    app.run()
