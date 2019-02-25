class UserDao:
    def __init__(self):
        # user_id, first_name, last_name, email, phone
        self.users = [[1, "Renier", "Velazco", "renier.velazco@upr.edu", "787-247-4930"],
                      [2, "Cristian", "Torres", "cristian.torres2@upr.edu", "787-218-2447"],
                      [3, "Julian", "Cuevas", "julian.cuevas1@upr.edu", "7876074678"]]

        # credentials_id, username, password
        self.credentials = [[1, "renier.velazco134", "herhewiofw"],
                            [2, "julian.cuevas32", "jogioiwpg"],
                            [3, "cristian.torres45", "ojgirjtpw"]]

        # message_id, text, message_date
        self.messages = [[1, "Vamos a janguear", "23-2-2019"],
                         [2, "Para donde vamos", "24-3-2019"],
                         [3, "DIMELO CONSUL", "25-4-2019"]]

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
        # chat_id, user_id
        self.participant = [[1, 1], [1, 2], [1, 3], [2, 1],
                            [2, 3], [3, 1], [3, 2], [3, 3]]

    def getAllUser(self):
        users = self.users
        return users

    def getUserById(self, uid):
        result = []
        for r in self.users.__iter__():
            if r[0] == uid:
                result = r

        return result

    def getUsername(self, uid):
        result = []
        for r in self.users.__iter__():
            if r[0] == uid:
                result = r[3]

        return result

    def postsFromUser(self, userId):
        result = []
        for r in self.post.__iter__():
            if r[4] == userId:
                result.append(r)

        return result

    # CRUDS

    def insert(self, username, password, firstName, lastName):
        uid = 0
        return uid

    def delete(self, uid):

        return uid

    def update(self, uid):
        result = []
        for r in self.users.__iter__():
            if r[0] == uid:
                result = r

        return result

    def getCountByUserId(self):

        result = []

        return result

    def getCredentials(self, username, password):
        user = self.users[1]

        return user

    def insertUser(self):
        user = self.users[1]
        return user
