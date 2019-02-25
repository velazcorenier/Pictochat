from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handler.user import UserHandler
from handler.Chat import ChatHandler
from handler.ContactList import ContactListHandler
from handler.MessageHandler import MessageHandler
from handler.PostHandler import PostHandler

app = Flask(__name__)
CORS(app)


@app.route('/')  # OK
def home():
    return "Welcome to Pictochat!"


@app.route('/Pictochat/')  # OK
def homeforApp():
    return "Welcome to Pictochat"

###################### User ######################################
@app.route('/Pictochat/register', methods=['POST'])
def register():
    if request.method =='POST':
        return UserHandler().insertUser()

@app.route('/Pictochat/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # return UserHandler().getCredentials(request.get_json('data'))
        return UserHandler().getCredentials()

@app.route('/Pictochat/users', methods=['GET', 'POST'])
def getAllUsers():
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

@app.route('/Pictochat/user/<int:uid>/contacts')
def getUserContacts(uid):
        return ContactListHandler().getContactsByUserId(uid)

@app.route('/Pictochat/user/<int:uid>/posts', methods=['GET'])
def getAllUserPosts(uid):
    if request.method == 'GET':
        return PostHandler().getPostsFromUser(uid)

@app.route('/Pictochat/user/<int:uid>/chats', methods=['GET'])
def getAllUserChats(uid):
    if request.method == 'GET':
        return UserHandler().getAllUserChats(uid)


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

@app.route('/Pictochat/chat/<int:chat_id>/admin', methods=['GET', 'POST'])
def getChatAdmin(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatAdmin(chat_id)

@app.route('/Pictochat/chat/<int:chat_id>/post', methods=['GET', 'POST'])
def getChatPost(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatPost(chat_id)

@app.route('/Pictochat/chat/<int:chat_id>/media', methods=['GET', 'POST'])
def getChatMedia(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatMedia(chat_id)

# CRUDS
@app.route('/Pictochat/chat/<string:chat_name>/<int:admin_id>', methods=['POST'])
def createChat(chat_name,admin_id):
    if request.method == 'POST':
        return ChatHandler().createChat(chat_name,admin_id)

@app.route('/Pictochat/chat/<int:chat_id>/<string:chat_name>/<int:admin_id>', methods=['PUT'])
def updateChat(chat_id,chat_name,admin_id):
    if request.method == 'PUT':
        return ChatHandler().updateChat(chat_id,chat_name,admin_id)

@app.route('/Pictochat/chat/<int:chat_id>', methods=['DELETE'])
def deleteChat(chat_id):
    if request.method == 'DELETE':
        return ChatHandler().deleteChat(chat_id)


############################################################
# TODO: Finish message REST
@app.route('/Pictochat/messages', methods=['GET', 'POST'])
def getAllMessages():
    if request.method == 'GET':
        return MessageHandler().getAllMessages()


@app.route('/Pictochat/message/<int:mid>', methods=['GET', 'POST'])
def getMessageById(mid):
    if request.method == 'GET':
        return MessageHandler().getMessageById(mid)

@app.route('/Pictochat/post/<int:pid>/message', methods=['GET'])
def getPostMessage(pid):
    if request.method == 'GET':
        return MessageHandler().getMessagePost(pid)

@app.route('/Pictochat/user/<int:uid>/messages', methods=['GET'])
def getMessagesByUserId(uid):
    if request.method == 'GET':
        return MessageHandler().getMessagesByUserId(uid)


if __name__ == '__main__':
    app.run()
