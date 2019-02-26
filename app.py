from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handler.user import UserHandler
from handler.Chat import ChatHandler
from handler.ContactList import ContactListHandler
from handler.PostHandler import PostHandler
from handler.hashtagHandler import HashtagHandler
from handler.mediaHandler import MediaHandler


app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True # Debug Mode. Server is reloaded on any code change
                           # and provides detailed error messages.

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

  ########## CRUDS User ##########

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

@app.route('/Pictochat/user/<int:uid>/posts', methods=['GET'])
def getAllUserPosts(uid):
    if request.method == 'GET':
        return PostHandler().getPostsFromUser(uid)

# @app.route('/Pictochat/user/<int:uid>/chats', methods=['GET'])
# def getAllUserChats(uid):
#     if request.method == 'GET':
#         return UserHandler().getAllUserChats(uid)

@app.route('/Pictochat/user/<int:uid>/reaction', methods=['GET'])
def getUserAllReaction(uid):
    if request.method == 'GET':
        return UserHandler().getUserAllReaction(uid)

@app.route('/Pictochat/user/<int:uid>/username', methods=['GET'])
def getUsername(uid):
    if request.method == 'GET':
        return UserHandler().getUsername(uid)

###################### Contacts ######################################

@app.route('/Pictochat/user/<int:uid>/contacts', methods=['GET'])
def getUserContacts(uid):
    if request.method == 'GET':
        return ContactListHandler().getContactsByUserId(uid)

# CRUDS
@app.route('/Pictochat/user/<int:owner>/contacts/addUser/<int:uid>', methods=['PUT'])
def addUsertoContactList(owner, uid):
    if request.method == 'PUT':
        handler = ContactListHandler()
        return handler.contactAddition(owner, uid)
@app.route('/Pictochat/user/<int:owner>/contacts/removeUser/<int:uid>', methods=['DELETE'])
def removeUserFromContactList(owner, uid):
    if request.method == 'DELETE':
        handler = ContactListHandler()
        return handler.removeContact(owner, uid)

############################################################
# CHAT ROUTES - Renier

@app.route('/Pictochat/chat', methods=['GET', 'POST'])
def getAllChatName():
    if request.method == 'GET':
        return ChatHandler().getAllChat()

@app.route('/Pictochat/chat/<int:chat_id>', methods=['GET', 'POST'])
def getChatById(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatById(chat_id)

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


######################### Post ###################################
# TODO: Finish message REST
@app.route('/Pictochat/posts', methods=['GET', 'POST'])
def getAllPost():
    if request.method == 'GET':
        return PostHandler().getAllPosts()


@app.route('/Pictochat/post/<int:postid>', methods=['GET', 'POST'])
def getPostById(postid):
    if request.method == 'GET':
        return PostHandler().getPostById(postid)

@app.route('/Pictochat/post/<int:postid>/reaction', methods=['GET'])
def getPostAllReaction(postid):
    if request.method == 'GET':
        return PostHandler().getPostAllReaction(postid)


@app.route('/Pictochat/post/<int:pid>/message', methods=['GET'])
def getPostMessage(pid):
    if request.method == 'GET':
        return PostHandler().getPostMessage(pid)

@app.route('/Pictochat/post/<int:pid>/media', methods=['GET'])
def getPostMedia(pid):
    if request.method == 'GET':
        return PostHandler().getPostMedia(pid)

@app.route('/Pictochat/user/<int:uid>/posts', methods=['GET'])
def getPostByUserId(uid):
    if request.method == 'GET':
        return PostHandler().getPostsFromUser(uid)


###### Hashtags ######
@app.route('/Pictochat/hashtags', methods=['GET', 'POST'])
def getAllHashtags():
    if request.method == 'GET':
        return HashtagHandler().getAllHashtags()

@app.route('/Pictochat/hashtags/<int:hashtag_id>', methods=['GET'])
def getHashtagById(hashtag_id):
    if request.method == 'GET':
        return HashtagHandler().getHashtagById(hashtag_id)

@app.route('/Pictochat/hashtags/text/<int:hashtag_id>', methods=['GET'])
def getHashtagText(hashtag_id):
    if request.method == 'GET':
        return HashtagHandler().getHashtagText(hashtag_id)

# CRUDS
@app.route('/Pictochat/hashtags/<string:hashtag_text>', methods=['POST'])
def createHashtag(hashtag_text):
    if request.method == 'POST':
        return HashtagHandler().createHashtag(hashtag_text)

@app.route('/Pictochat/hashtags/<int:hashtag_id>/<string:hashtag_text>', methods=['PUT'])
def updateHashtag(hashtag_id, hashtag_text):
    if request.method == 'PUT':
        return HashtagHandler().updateHashtag(hashtag_id, hashtag_text)

@app.route('/Pictochat/hashtags/<int:hashtag_id>', methods=['DELETE'])
def deleteHashtag(hashtag_id):
    if request.method == 'DELETE':
        return HashtagHandler().deleteHashtag(hashtag_id)

###### Media ######
@app.route('/Pictochat/media', methods=['GET', 'POST'])
def getAllMedia():
    if request.method == 'GET':
        return MediaHandler().getAllMedia()

@app.route('/Pictochat/media/<int:media_id>', methods=['GET'])
def getMediaById(media_id):
    if request.method == 'GET':
        return MediaHandler().getMediaById(media_id)

@app.route('/Pictochat/media/type/<int:media_id>', methods=['GET'])
def getMediaType(media_id):
    if request.method == 'GET':
        return MediaHandler().getMediaType(media_id)

@app.route('/Pictochat/media/location/<int:media_id>', methods=['GET'])
def getMediaLocation(media_id):
    if request.method == 'GET':
        return MediaHandler().getMediaLocation(media_id)

# CRUDS
@app.route('/Pictochat/media/<string:media_type>/<string:location>', methods=['POST'])
def createMedia(media_type, location):
    if request.method == 'POST':
        return MediaHandler().createMedia(media_type, location)

@app.route('/Pictochat/media/<int:media_id>/<string:media_type>/<string:location>', methods=['PUT'])
def updateMedia(media_id, media_type, location):
    if request.method == 'PUT':
        return MediaHandler().updateMedia(media_id, media_type, location)

@app.route('/Pictochat/media/<int:media_id>', methods=['DELETE'])
def deleteMedia(media_id):
    if request.method == 'DELETE':
        return MediaHandler().deleteMedia(media_id)

if __name__ == '__main__':
    app.run()
