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

        # post_id, chat_id, message_id, location, owner_id
        self.post = [[1, 3, 44, "c://localhost/photos/dog.jpeg", 2],
                     [2, 2, 12, "c://localhost/photos/cat.jpeg", 1],
                     [3, 1, 25, "c://localhost/photos/cow.jpeg", 3]]

        # chat_id, user_id
        self.participant = [[1, 1], [1, 2], [1, 3], [2, 1],
                            [2, 3], [3, 1], [3, 2], [3, 3]]

    def getAllUser(self):
        users = self.users
        return users

    def getUserById(self, uId):
        user = self.users[1]

        return user

    def getUserByFirstName(self, firstName):
        # cursor = self.conn.cursor()
        # query = "select * from user where firstName = %s;"
        # cursor.execute(query, (color,))
        result = []
        # for row in cursor:
        #     result.append(row)
        return result

    def getUserByLastName(self, lastName):
        # cursor = self.conn.cursor()
        # query = "select * from user where lastNme = %s;"
        # cursor.execute(query, (material,))
        result = []
        # for row in cursor:
            # result.append(row)
        return result

    def getUserByFirstNameAndLastName(self, firstName, lastName):

        result = []
        # for row in cursor:
        #     result.append(row)
        return result

    def getUserByUsername(self, username):
        # cursor = self.conn.cursor()
        # query = "select * from user where username = %s;"
        # cursor.execute(query, (material, color))
        result = []
        # for row in cursor:
        #     result.append(row)
        return result

    def getAllUserChats(self, uid):
        result = self.chat[0:2]
        return result

    # CRUDS

    def insert(self, username, password, firstName, lastName):
        uid = 0
        return uid

    def delete(self, uid):

        return uid

    def update(self):
        user = self.users[1]

        return user

    def getCountByUserId(self):

        result = []

        return result

    def getCredentials(self, username, password):
        user = self.users[1]

        return user

    def insertUser(self):
        user = self.users[1]
        return user
