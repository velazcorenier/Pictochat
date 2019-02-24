from flask import jsonify
from dao.UserDAO import UserDao


class UserHandler:

    # Dictionaries
    def build_user_dict(self, row):
        result = row
        # result['user_id'] = row[0]
        # result['username'] = row[1]
        # result['password'] = row[2]
        # result['person_id'] = row[3]
        # result['is_Active'] = row[4]
        return result

    def build_user_attributes(self, uid, username, password, person_id, is_active):
        result = {}
        result['uid'] = uid
        result['username'] = username
        result['password'] = password
        result['person_id'] = person_id
        result['is_active'] = is_active
        return result

    # Gets

    def getAllUser(self):
        dao = UserDao()
        user_list = dao.getAllUser()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getUserById(self, pid):
        dao = UserDao()
        row = dao.getUserById(pid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)
    #TODO: Finish search method.
    def searchUsers(self, args):
        username = args.get("username")
        firstName = args.get("firstName")
        lastName = args.get("lastName")
        dao = UserDao()
        user_list = []
        if (len(args) == 2) and firstName and lastName:
            user_list = dao.getUserByFirstNameAndLastName(firstName, lastName)
        elif (len(args) == 1) and firstName:
            user_list = dao.getUserByFirstName(firstName)
        elif (len(args) == 1) and lastName:
            user_list = dao.getUserByLastName(lastName)
        elif (len(args) == 1) and username:
            user_list = dao.getUserByUsername(username)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    # This method return all users in a group chat.
    def getAllUserByChat(self, chatId):
        dao = UserDao()
        user_list = dao.getAllUserByChat(chatId)
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)



    # CRUDS

    def updateUser(self, uid, form):
        dao = UserDao()
        if not dao.getUserById(uid):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                username = form['username']
                password = form['password']
                person_id = form['person_id']
                is_active = form['is_active']
                if username and password and person_id and is_active:
                    dao.update(uid, username, password, person_id, is_active)
                    result = self.build_user_attributes(uid, username, password, person_id, is_active)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteUser(self, uid):
        dao = UserDao()
        if not dao.getUserById(uid):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(uid)
        return jsonify(DeleteStatus="OK"), 200
