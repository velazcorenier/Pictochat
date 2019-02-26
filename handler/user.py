from flask import jsonify
from dao.UserDAO import UserDao


class UserHandler:

    # Dictionaries
    # user_id, first_name, last_name, email, phone
    def build_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        return result

    def build_post_dict(self, row):
        result = {}
        result['post_id'] = row[0]
        result['chat_id'] = row[1]
        result['caption'] = row[2]
        result['media_id'] = row[3]
        result['user_id'] = row[4]
        result['post_date'] = row[5]
        return result

    def build_credential_dict(self, row):
        result = {'UserId': row[0], 'Username': row[3]}
        return result

    # reaction_id, post_id, user_id reaction_date, reaction_type
    def build_user_reaction_dict(self, row):
        result = {}
        result['reaction_id'] = row[0]
        result['post_id'] = row[1]
        result['user_id'] = row[2]
        result['reaction_id'] = row[3]
        result['reaction_type'] = row[4]
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

    def getUserAllReaction(self,uid):
        dao = UserDao()
        user_reaction_list = dao.getUserReaction(uid)
        result_list = []
        for row in user_reaction_list:
            result = self.build_user_reaction_dict(row)
            result_list.append(result)
        return jsonify(ReactionsByUser=result_list)

    def getUserById(self, uid):
        dao = UserDao()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    # def getAllUserChats(self, uid):
    #     dao = UserDao()
    #     row = dao.getAllUserChats(uid)
    #     if not row:
    #         return jsonify(Error="Not Found Chats for this user."), 404
    #     else:
    #         chats = self.build_user_dict(row)
    #         return jsonify(Chats=chats)

    def getUsername(self, uid):
        username = UserDao().getUsername(uid)

        if not username:
            return jsonify(Error="USER NOT FOUND"), 404

        result = {}
        result['username'] = username
        return jsonify(Username=result)

    # TODO: Finish search method.
    # def searchUsers(self, args):
    #     username = args.get("username")
    #     firstName = args.get("firstName")
    #     lastName = args.get("lastName")
    #     dao = UserDao()
    #     user_list = []
    #     if (len(args) == 2) and firstName and lastName:
    #         user_list = dao.getUserByFirstNameAndLastName(firstName, lastName)
    #     elif (len(args) == 1) and firstName:
    #         user_list = dao.getUserByFirstName(firstName)
    #     elif (len(args) == 1) and lastName:
    #         user_list = dao.getUserByLastName(lastName)
    #     elif (len(args) == 1) and username:
    #         user_list = dao.getUserByUsername(username)
    #     else:
    #         return jsonify(Error="Malformed query string"), 400
    #     result_list = []
    #     for row in user_list:
    #         result = self.build_user_dict(row)
    #         result_list.append(result)
    #     return jsonify(User=result_list)

    def getPostsFromUser(self, uid):
        posts = UserDao().postsFromUser(uid)
        if not posts:
            return jsonify(Error="NOT FOUND POSTS FROM USER"), 404
        result = []
        for p in posts:
            result.append(self.build_post_dict(p))
        return jsonify(PostsFromUser=result)

    # CRUDS
    def insertUser(self):
        dao = UserDao()
        user = dao.insertUser()
        result = self.build_user_dict(user)
        return jsonify(User=result), 201

    def updateUser(self, uid, form):
        dao = UserDao()
        user = dao.update(uid)
        if not user:
            return jsonify(Error="USER NOT FOUND"), 404

        result = self.build_user_dict(user)
        return jsonify(User=result), 200

    def deleteUser(self, uid):
        return jsonify(DeleteStatus="OK"), 200

    def getCredentials(self):
        dao = UserDao()
        result = dao.getCredentials('', '')
        return jsonify(User=self.build_credential_dict(result))
