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

        # message_id, text, message_date
        self.messages = [[1, "Vamos a janguear", "23-2-2019"],
                         [2, "Para donde vamos", "24-3-2019"],
                         [3, "DIMELO CONSUL", "25-4-2019"]]

        # chat_id, chat_name
        self.chat = [[1, "Maquinas"],
                     [2, "Jangueadores"],
                     [3, "Memes"]]

        # cid, uid, pdate, ptime
        self.participants = [[1, 1, "2018-1-15", "16:02:13"], [1, 4, "2018-1-15", "16:02:13"],
                             [1, 5, "2018-1-17", "13:14:54"], [2, 3, "2018-1-10", "06:04:13"],
                             [2, 2, "2018-1-10", "06:04:13"], [3, 6, "2018-1-20", "12:43:41"],
                             [3, 2, "2018-1-20", "12:43:41"], [3, 3, "2018-1-20", "12:43:41"],
                             [4, 4, "2018-1-25", "16:34:27"], [4, 2, "2018-1-25", "16:34:27"]]

    def getALLChat(self):
        return self.chat[0:2]
