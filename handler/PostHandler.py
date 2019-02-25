from dao.PostDAO import PostDAO
from flask import jsonify, make_response

class MessageHandler:

    def build_post_dict(self, p):
        mapped = {'PostId': p[0], 'Message': p[1], 'Chat': p[2], 'Date': p[3], 'Username': p[4]}
        return mapped

    def searchDic(self, p):
        mapped = {'MessageId': p[3], 'Message': p[5], 'ChatId': p[2], 'UserId': p[4], 'Username': p[0], 'HashtagName': p[1]}
        return mapped

    def mapChatMessage(self, p):
        return {'Username': m[0], 'MessageID': p[1], 'Time': p[2], 'Text': p[3], 'Likedby': p[4], 'Dislikedby': p[5], 'Reply': p[6], 'Likes': p[7], 'Dislikes': p[8], 'ReplyId': p[9]}

    def mapUserPost(self, p):
        return {'Chatname': p[0], 'ChatID': p[1], 'PostID': p[2], 'Time': p[3], 'Text': p[4]}


    def getPostById(self, postid):
        post = PostDAO().postById(postid)
        if not post:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for p in post:
            result.append(self.build_post_dict(p))
            return jsonify(Post=result)

    def getAllPosts(self):
        posts = PostDAO().getAllPosts()
        if not posts:
            return jsonify(Error="NOT FOUND POSTS"), 404
        result = []
        for p in posts:
            result.append(self.build_post_dict(p))
        return jsonify(AllPosts=result)

    def getPostsFromChat(self, cid):
        posts = PostDAO().getAllPostsFromChatId(cid)
        if not posts:
            return jsonify(Error="NOT FOUND POSTS"), 404
        result = []
        for p in posts:
            result.append(self.mapChatMessage(p))
        return jsonify(PostsFromChat=result)

    def getPostsFromUser(self, uid):
        posts = PostDAO().postsFromUser(uid)
        if not posts:
            return jsonify(Error="NOT FOUND POSTS FROM USER"), 404
        result = []
        for p in posts:
            result.append(self.mapUserPost(p))
        return jsonify(PostsFromUser=result)

    def getPostPerDay(self, day):
        posts = PostDAO().getPostsPerDay(day)
        if not posts:
            return jsonify(Error="NOT FOUND POSTS ON THIS DAY."), 404
        result = []
        for p in posts:
            result.append(self.build_post_dict(p))
        return jsonify(PostsFromUser=result)
