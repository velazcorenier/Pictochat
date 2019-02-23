from flask import jsonify
from dao.user import UserDao


class UserHandler:
    def build_user_dict(self, row):
        result = row
        #result['user_id'] = row[0]
        #result['username'] = row[1]
        #result['password'] = row[2]
        #result['person_id'] = row[3]
        #result['is_Active'] = row[4]
        return result


    def getAllUser(self):
        dao = UserDao()
        user_list = dao.getAllUser()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)
