from dao.MessageDAO import MessageDAO
from flask import jsonify, make_response


# from dao.HashtagDAO import HashtagDao

class MessageHandler:
    def build_message_dict(self, row):
        result = row
        # result['user_id'] = row[0]
        # result['username'] = row[1]
        # result['password'] = row[2]
        # result['person_id'] = row[3]
        # result['is_Active'] = row[4]
        return result

    def getAllMessages(self):
        messages = MessageDAO().allMessages()
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.build_message_dict(m))
        return jsonify(AllMessages=result)

    def getMessageById(self, mid):
        messages = MessageDAO().messageById(mid)
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.build_message_dict(m))
        return jsonify(Message=result)

    def getMessagePost(self, cid):
        messages = MessageDAO().messagesFromPostId(cid)
        if not messages:
            return jsonify(Error="POST MESSAGE NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.build_message_dict(m))
        return jsonify(MessagesOfPost=result)

    def getMessagesByUserId(self, uid):
        messages = MessageDAO().messagesFromUser(uid)
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.build_message_dict(m))
        return jsonify(MessagesFromUser=result)

    def getAllLikes(self):
        dao = MessageDAO().getLikes()
        if not dao:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.maplikesall(l))
        return jsonify(AllLikes=result)

    def getAllDislikes(self):
        dao = MessageDAO().getDislikes()
        if not dao:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.mapdislikesall(l))
        return jsonify(AllDislikes=result)

    def getMessageReplies(self, mid):
        messages = MessageDAO().messageReply(mid)
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.mapreply(m))
        return jsonify(MessageReplies=result)
