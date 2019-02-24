from flask import jsonify
from dao.chat import ChatDAO

class ChatHandler:

    def build_user_dict(self, row):
        result = {}
        result['chat_id'] = row[0]
        result['name'] = row[1]
        return result

    def getAllChat(self):
        dao = ChatDAO()
        chatlist = dao.getALLChat()
        resultlist = []
        for row in chatlist:
            result = self.build_user_dict(row)
            resultlist.append(result)
        return jsonify(Chat=resultlist)