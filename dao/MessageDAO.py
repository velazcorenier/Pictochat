# import psycopg2
# from config.dbconfig import pg_config

class MessageDAO:
    def __init__(self):
        # user_id, first_name, last_name, email, phone
        self.users = [[1, "Renier", "Velazco", "renier.velazco@upr.edu", "787-247-4930"],
                      [2, "Cristian", "Torres", "cristian.torres2@upr.edu", "787-218-2447"],
                      [3, "Julian", "Cuevas", "julian.cuevas1@upr.edu", "7876074678"]]

        # message_id, text, message_date
        self.messages = [[1, "Vamos a janguear", "23-2-2019"],
                         [2, "Para donde vamos", "24-3-2019"],
                         [3, "DIMELO CONSUL", "25-4-2019"]]

        # post_id, chat_id, message_id, location, owner_id
        self.post = [[1, 3, 44, "c://localhost/photos/dog.jpeg", 2],
                     [2, 2, 2, "c://localhost/photos/cat.jpeg", 1],
                     [3, 1, 25, "c://localhost/photos/cow.jpeg", 3]]
        # chat_id, chat_name, admin_id
        self.chat = [[1, "Maquinas", 3],
                     [2, "Jangueadores", 2],
                     [3, "Memes", 1]]

    def allMessages(self):
        cursor = self.messages
        return cursor

    def messageById(self, mid):
        result = self.messages[1]

        return result

    # def hashtagList(self):
    #     cursor = self.conn.cursor()
    #     query = 'select array_agg(hashname), array_agg(hid) from hashtag;'
    #     cursor.execute(query)
    #     result = cursor.fetchone()
    #     self.conn.commit()
    #     print(result)
    #     return result


    def messagesFromChat(self, cid):
        messages = self.messages
        chat = self.chat[1]
        result = []
        for m in messages:
            if m[0] == chat[0]:
                result.append(m)
        return result

    def messagesFromPostId(self, pid):
        messages = self.messages
        post = self.post[1]
        result = []
        for m in messages:
            if m[0] == post[0]:
                result.append(m)
        return result

    def messagesFromUser(self, uid):
        messages = self.messages
        user = self.users[1]
        result = []
        for m in messages:
            if m[0] == user[0]:
                result.append(m)
        return result

    def messageReply(self, mid):
        cursor = self.conn.cursor()
        query = 'select m2.text, u.username  from message as m1, reply as r, message as m2, "user" as u where u.uid=m2.uid and m1.mid=r.mid and m2.mid=r.reply and m1.mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countRepliesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message as m1, reply as r, message as m2, "user" as u where u.uid=m2.uid and m1.mid=r.mid and m2.mid=r.reply and m1.mid=%s;'
        cursor.execute(query, (mid, ))
        return cursor.fetchone()[0]

    def getLikes(self):
        cursor = self.conn.cursor()
        query = 'select mid, username from "like" natural inner join "user";'
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messageLikes(self, mid):
        cursor = self.conn.cursor()
        query = 'select username from message as m, "like" as l, "user" as u where m.mid=l.mid and u.uid=l.uid and m.mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def getDislikes(self):
        cursor = self.conn.cursor()
        query = 'select mid, username from "user" natural inner join dislike;'
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messagesDislikes(self, mid):
        cursor = self.conn.cursor()
        query = 'select username from message as m, dislike as d, "user" as u where m.mid=d.mid and u.uid=d.uid and m.mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countLikesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message as m, "like" as l, "user" as u where m.mid=l.mid and u.uid=l.uid and m.mid=%s;'
        cursor.execute(query, (mid, ))
        return cursor.fetchone()[0]

    def countDislikesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message as m, dislike as d, "user" as u where m.mid=d.mid and u.uid=d.uid and m.mid=%s;'
        cursor.execute(query, (mid, ))
        return cursor.fetchone()[0]

    def insertlike(self, uid, mid):
        cursor = self.conn.cursor()
        query = 'insert into "like" values (%s, %s)'
        cursor.execute(query, (uid, mid))
        self.conn.commit()
        return "Done"

    def insertdislike(self, uid, mid):
        cursor = self.conn.cursor()
        query = 'insert into dislike values (%s, %s)'
        cursor.execute(query, (uid, mid))
        self.conn.commit()
        return "Done"

    def insertreply(self, mid, reply):
        cursor = self.conn.cursor()
        query = 'insert into reply values (%s, %s)'
        cursor.execute(query, (mid, reply))
        self.conn.commit()
        return "Done"