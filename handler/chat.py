from flask import jsonify
from dao.chat import ChatDAO

class ChatHandler:

    def build_chat_name_dict(self, row):
        result = {}
        result['chat_id'] = row[0]
        result['name'] = row[1]
        result['admin'] = row[2]
        return result

    def build_chat_participant_dict(self, row):
        result = {}
        result['chat_id'] = row[0]
        result['user_id'] = row[1]
        return result

    # post_id, chat_id, message_id, location, owner_id
    def build_chat_post_dict(self, row):
        result = {}
        result['post_id'] = row[0]
        result['chat_id'] = row[1]
        result['message_id'] = row[2]
        result['location'] = row[3]
        result['owner_id'] = row[4]
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

   # def getChatMessage(self, chat_id, chat_post):

   # def getChatPhoto(self, chat_id, chat_post):

   # def getChatHashtag(self, chat_id, chat_message):

   # def getChatReply(self, chat_id, chat_message):