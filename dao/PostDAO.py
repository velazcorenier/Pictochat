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

        # post_id, chat_id, message_id, location, owner_id
        self.post = [[1, 3, "Mensaje 1", "c://localhost/photos/dog.jpeg", 2],
                     [2, 2, "Mensaje 2", "c://localhost/photos/cat.jpeg", 1],
                     [3, 1, "Mensaje 3", "c://localhost/photos/cow.jpeg", 3]]

        # reaction_id, post_id, user_id reaction_date, reaction_type
        self.reaction = [[1, 2, 2, "25-3-2019", 1],
                         [2, 1, 1, "26-3-2019", -1],
                         [3, 3, 3, "27-3-2019", 1]]



    def getAllPosts(self):
        posts = self.post

        return posts

    def getAllPostsFromChatId(self, chatId):
        result = []
        for r in self.post.__iter__():
            if r[1] == chatId:
                result.append(r)

        return result

    def postsFromUser(self, userId):
        result = []
        for r in self.post.__iter__():
            if r[4] == userId:
                result = r

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

    def getPostMedia(self, postId):
        result = []
        for r in self.post.__iter__():
            if r[0] == postId:
                result = r[3]

        return result

    def getPostsPerDay(self, day):
        result = self.post[0]
        return result

    def insertPost(self):
        result = self.post[2]
        return result

    def getPostReaction(self, postid):
        if postid == 1:
            return self.reaction[1:2]
        elif postid == 2:
            return self.reaction[0:1]
        elif postid == 3:
            return self.reaction[2:3]
        return []

