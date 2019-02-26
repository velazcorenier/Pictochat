from dao.PostDAO import PostDAO
from flask import jsonify, make_response


class PostHandler:
    def build_post_dict(self, row):
        result = {}
        result['post_id'] = row[0]
        result['chat_id'] = row[1]
        result['caption'] = row[2]
        result['media_id'] = row[3]
        result['user_id'] = row[4]
        result['post_date'] = row[5]
        return result

        # user_id, first_name, last_name, email, phone

    def build_chat_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        return result

        # hashtag_id, hash_text
    def build_hashtag_dict(self, row):
        result = {}
        result['hashtag_id'] = row[0]
        result['hash_text'] = row[1]
        return result
    # reply_id, text, post_id, message_date, user_id
    def build_reply_dict(self, row):
        result = {}
        result['reply_id'] = row[0]
        result['text'] = row[1]
        result['post_id'] = row[2]
        result['reply_date'] = row[3]
        result['user_id'] = row[4]
        return result

    # GET's
    def getPostById(self, postid):
        post = PostDAO().postById(postid)
        if not post:
            return jsonify(Error="POST NOT FOUND"), 404

        resultlist = []
        result = self.build_post_dict(post)
        resultlist.append(result)
        return jsonify(Post=resultlist)

    def getAllPosts(self):
        posts = PostDAO().getAllPosts()
        if not posts:
            return jsonify(Error="NOT FOUND POSTS"), 404
        result = []
        for p in posts:
            result.append(self.build_post_dict(p))
        return jsonify(AllPosts=result)

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

    def getPostOwner(self, postid):
        postOwner = PostDAO().getPostOwner(postid)

        if not postOwner:
            return jsonify(Error="NOT FOUND OWNER POST"), 404

        return jsonify(PostOwner=postOwner)


    def getPostMedia(self, postid):
        media = PostDAO().getPostMedia(postid)

        if not media:
            return jsonify(Error="Media NOT FOUND"), 404

        return jsonify(MediaOfPost=media)

    def getReplysByPostId(self, postid):
        replys = PostDAO().getReplysByPostId(postid)

        if not replys:
            return jsonify(Error="Replys NOT FOUND"), 404

        result = []
        for p in replys:
            result.append(self.build_reply_dict(p))

        return jsonify(PostReplys=result)


    def getAllHashtagsByPostsId(self, postid):
        hashtags = PostDAO().getHashtagsByPostId(postid)

        if not hashtags:
            return jsonify(Error="Hashtags NOT FOUND"), 404
        result = []
        for p in hashtags:
            result.append(self.build_hashtag_dict(p))
        return jsonify(HashtagsOnPost=result)
#     CRUD'S

    def insertPost(self):
        dao = PostDAO()
        post = dao.insertPost()
        result = post
        return jsonify(User=result), 201

    def deletePost(self, postid):
        return jsonify(DeleteStatus="OK"), 200

