class PostDAO:
    def __init__(self):
        # user_id, first_name, last_name, email, phone
        self.users = [[1, "Renier", "Velazco", "renier.velazco@upr.edu", "787-247-4930"],
                      [2, "Cristian", "Torres", "cristian.torres2@upr.edu", "787-218-2447"],
                      [3, "Julian", "Cuevas", "julian.cuevas1@upr.edu", "7876074678"]]

        # message_id, text, message_date
        self.messages = [[1, "Vamos a janguear", "23-2-2019"],
                         [2, "Para donde vamos", "24-3-2019"],
                         [3, "DIMELO CONSUL", "25-4-2019"],]

        # chat_id, chat_name, admin_id
        self.chat = [[1, "Maquinas", 3],
                     [2, "Jangueadores", 2],
                     [3, "Memes", 1]]

        # post_id, chat_id, caption, media_id, owner_id, post_date
        self.post = [[1, 3, "Vamos a janguear", 10, 2, "25-2-2019"],
                     [2, 2, "Para donde vamos", 20, 1, "23-2-2019"],
                     [3, 1, "DIMELO CONSUL", 30, 3, "24-3-2019"]]

        # media_id, media_type, location
        self.media = [[1, "photo", "c://localhost/photos/dog.jpeg"],
                      [2, "photo", "c://localhost/photos/cat.jpeg"],
                      [3, "photo", "c://localhost/photos/cow.jpeg"]]

        # reply_id, text, post_id, message_date, user_id
        self.reply = [[1, "Donde sea", 3, "28-2-2019", 1],
                      [2, "Tu me dice y le llegamos", 1, "27-3-2019", 2],
                      [3, "BROTHEL tu sae como eh", 2, "26-4-2019", 3]]

        # hashtag_id, hash_text
        self.hashtags = [[0, 'travel'],
                         [1, 'beautiful'],
                         [2, 'food'],
                         [3, 'art']]

    def getAllPosts(self):
        posts = self.post

        return posts

    def getAllPostsFromChatId(self, chatId):
        result = []
        for r in self.post.__iter__():
            if r[1] == chatId:
                result.append(r)

        return result

    def postById(self, postId):
        result = []
        for r in self.post.__iter__():
            if r[0] == postId:
                result = r

        return result

    def getPostMessage(self,postId):
        result = []
        for r in self.post.__iter__():
            if r[0] == postId:
                result = r[2]

        return result

    def getPostOwner(self, postId):
        result = []
        for r in self.post.__iter__():
            if r[0] == postId:
                result = r[4]

        return result

    def getPostMedia(self, postId):
        result = []
        for r in self.post.__iter__():
            if r[0] == postId:
                result = r[3]

        return result

    def getReplysByPostId(self, postId):
        result = []
        for r in self.reply.__iter__():
            if r[2] == postId:
                result.append(r)

        return result

    def getHashtagsByPostId(self, postId):
        result = []
        for r in self.hashtags.__iter__():
                result.append(r)

        return result

    def getPostsPerDay(self, day):
        result = self.post[0]
        return result

    def insertPost(self):
        result = self.post[2]
        return result

