class PostDAO:
    def __init__(self):
        # user_id, first_name, last_name, email, phone
        self.users = [[1, "Renier", "Velazco", "renier.velazco@upr.edu", "787-247-4930"],
                      [2, "Cristian", "Torres", "cristian.torres2@upr.edu", "787-218-2447"],
                      [3, "Julian", "Cuevas", "julian.cuevas1@upr.edu", "7876074678"]]

        # message_id, text, message_date
        self.messages = [[1, "Vamos a janguear", "23-2-2019"],
                         [2, "Para donde vamos", "24-3-2019"],
                         [3, "DIMELO CONSUL", "25-4-2019"]]

        # chat_id, chat_name, admin_id
        self.chat = [[1, "Maquinas", 3],
                     [2, "Jangueadores", 2],
                     [3, "Memes", 1]]

        # post_id, chat_id, message_id, location, owner_id
        self.post = [[1, 3, 44, "c://localhost/photos/dog.jpeg", 2],
                     [2, 2, 12, "c://localhost/photos/cat.jpeg", 1],
                     [3, 1, 25, "c://localhost/photos/cow.jpeg", 3]]



    def getAllPosts(self):
        posts = self.post

        return posts

    def getAllPostsFromChatId(self, chatId):
        result = self.post[0:1]
        return result

    def postsFromUser(self, userId):
        result = self.post
        return result

    def postById(self, postId):
        result = self.post[3]
        return result

    def getPostsPerDay(self, day):
        result = self.post[0]
        return result

    def insertPost(self):
        result = self.post[2]
        return result

