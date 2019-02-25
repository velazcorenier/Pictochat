class ChatDAO:
    def __init__(self):
        # user_id, first_name, last_name, email, phone
        self.users = [[1, "Renier", "Velazco", "renier.velazco@upr.edu", "787-247-4930"],
                      [2, "Cristian", "Torres", "cristian.torres2@upr.edu", "787-218-2447"],
                      [3, "Julian", "Cuevas", "julian.cuevas1@upr.edu", "7876074678"]]

        # credentials_id, username, password
        self.credentials = [[1, "renier.velazco134", "herhewiofw"],
                            [2, "julian.cuevas32", "jogioiwpg"],
                            [3, "cristian.torres45", "ojgirjtpw"]]

        # reply_id, text, post_id, message_date
        self.reply = [[1, "Donde sea", 3, "28-2-2019"],
                     [2, "Tu me dice y le llegamos", 1, "27-3-2019"],
                     [3, "BROTHEL tu sae como eh", 2, "26-4-2019"]]


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

        # hashtag, post_id
        self.topic = [["mindblowing", 2], ["wtf", 3], ["doyouevenlift?", 1]]

        # reaction_id, post_id, reaction_date, reaction_type
        self.reaction = [[1, 2, "25-3-2019", 1],
                        [2, 1, "26-3-2019", -1],
                        [3, 3, "27-3-2019", 1]]


        # paticipant_id chat_id, user_id
        self.participant = [[1, 1, 1], [2, 1, 2], [3, 1, 3], [4, 2, 1],
                             [5, 2, 3], [6, 3, 1], [7, 3, 2], [8, 3, 3]]


    def getAllChat(self):
        return self.chat[0:3]

    def getChatById(self,chat_id):
        if chat_id == 1:
            return self.chat[0:1]
        elif chat_id == 2:
            return self.chat[1:2]
        elif chat_id == 3:
            return self.chat[2:3]
        return []

    def getChatParticipant(self, chat_id):
        if chat_id == 1:
            return self.participant[0:3]
        elif chat_id == 2:
            return self.participant[3:5]
        elif chat_id == 3:
            return self.participant[5:8]
        return []

    def getChatAdmin(self, chat_id):
        if chat_id == 1:
            return self.users[2:3]
        elif chat_id == 2:
            return self.users[1:2]
        elif chat_id == 3:
            return self.users[0:1]
        return []

    def getChatPost(self, chat_id):
        if chat_id == 1:
            return self.post[2:3]
        elif chat_id == 2:
            return self.post[1:2]
        elif chat_id == 3:
            return self.post[0:1]
        return []


    def getChatMedia(self, chat_id):
        if chat_id == 1:
            return self.media[0:1]
        elif chat_id == 2:
            return self.media[1:2]
        elif chat_id == 3:
            return self.media[2:3]
        return []










