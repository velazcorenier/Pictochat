from dao.PostDAO import PostDAO
from flask import jsonify, make_response


class PostHandler:
    # GET's
    def getPostById(self, postid):
        post = PostDAO().postById(postid)
        if not post:
            return jsonify(Error="POST NOT FOUND"), 404

        return jsonify(Post=post)


    def getAllPosts(self):
        posts = PostDAO().getAllPosts()
        if not posts:
            return jsonify(Error="NOT FOUND POSTS"), 404
        result = []
        for p in posts:
            result.append(p)
        return jsonify(AllPosts=result)

    def getPostsFromChat(self, cid):
        posts = PostDAO().getAllPostsFromChatId(cid)
        if not posts:
            return jsonify(Error="NOT FOUND POSTS ON CHAT"), 404
        result = []
        for p in posts:
            result.append(p)
        return jsonify(PostsFromChat=result)

    def getPostsFromUser(self, uid):
        posts = PostDAO().postsFromUser(uid)
        if not posts:
            return jsonify(Error="NOT FOUND POSTS FROM USER"), 404
        result = []
        for p in posts:
            result.append(p)
        return jsonify(PostsFromUser=result)

    def getPostPerDay(self, day):
        posts = PostDAO().getPostsPerDay(day)
        if not posts:
            return jsonify(Error="NOT FOUND POSTS ON THIS DAY."), 404
        result = []
        for p in posts:
            result.append(p)
        return jsonify(PostsPerDay=result)

    def getPostMessage(self, postid):
        message = PostDAO().getPostMessage(postid)

        if not message:
            return jsonify(Error="Message NOT FOUND"), 404

        return jsonify(MessageOfPost=message)

    def getPostMedia(self, postid):
        message = PostDAO().getPostMedia(postid)

        if not message:
            return jsonify(Error="Media NOT FOUND"), 404

        return jsonify(MediaOfPost=message)

#     CRUD'S

    def insertPost(self):
        dao = PostDAO()
        post = dao.insertPost()
        result = post
        return jsonify(User=result), 201

    def deletePost(self, postid):
        return jsonify(DeleteStatus="OK"), 200

