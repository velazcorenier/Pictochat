from flask import jsonify
from dao.ChatDAO import ChatDAO


class ChatHandler:

    # chat_id, chat_name, admin_id
    def build_chat_name_dict(self, row):
        result = {}
        result['chat_id'] = row[0]
        result['name'] = row[1]
        result['admin_id'] = row[2]
        return result

    # participant_id chat_id, user_id
    def build_chat_participant_dict(self, row):
        result = {}
        result['participant_id'] = row[0]
        result['chat_id'] = row[1]
        result['user_id'] = row[2]
        return result

    # post_id, chat_id, message_id, media_id, owner_id, post_date
    def build_chat_post_dict(self, row):
        result = {}
        result['post_id'] = row[0]
        result['chat_id'] = row[1]
        result['message_id'] = row[2]
        result['media_id'] = row[3]
        result['owner_id'] = row[4]
        result['post_date'] = row[5]
        return result

    # message_id, text, message_date
    def build_chat_message_dict(self, row):
        result = {}
        result['message_id'] = row[0]
        result['text'] = row[1]
        result['message_date'] = row[2]
        return result

    # media_id, media_type, location
    def build_chat_media_dict(self, row):
        result = {}
        result['media_id'] = row[0]
        result['media_type'] = row[1]
        result['location'] = row[2]
        return result

    def getAllChat(self):
        dao = ChatDAO()
        chatlist = dao.getAllChat()
        resultlist = []
        for row in chatlist:
            result = self.build_chat_name_dict(row)
            resultlist.append(result)
        return jsonify(Chat_Name=resultlist)

    def getChatParticipant(self, chat_id):
        dao = ChatDAO()
        participantlist = dao.getChatParticipant(chat_id)
        resultlist = []
        for row in participantlist:
            result = self.build_chat_participant_dict(row)
            resultlist.append(result)
        return jsonify(Participant=resultlist)

    def getChatPost(self, chat_id):
        dao = ChatDAO()
        postlist = dao.getChatPost(chat_id)
        resultlist = []
        for row in postlist:
            result = self.build_chat_post_dict(row)
            resultlist.append(result)
        return jsonify(Post=resultlist)

    def getChatAllMessage(self, chat_id):
        dao = ChatDAO()
        messagelist = dao.getChatAllMessage(chat_id)
        resultlist = []
        for row in messagelist:
            result = self.build_chat_message_dict(row)
            resultlist.append(result)
        return jsonify(Message=resultlist)

    def getChatMedia(self, chat_id):
        dao = ChatDAO()
        mediaList = dao.getChatMedia(chat_id)
        resultlist = []
        for row in mediaList:
            result = self.build_chat_media_dict(row)
            resultlist.append(result)
        return jsonify(Media=resultlist)


    #def getChatHashtag(self, chat_id, chat_message):

    #def getChatReply(self, chat_id, chat_message):
