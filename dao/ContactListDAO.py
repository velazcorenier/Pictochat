from dao.UserDAO import UserDao


# import psycopg2
# from config.dbconfig import pg_config

class ContactListDAO:
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
    #     self.conn = psycopg2.connect(connection_url)

    def allContactLists(self):
        # cursor = self.conn.cursor()
        # query = query = 'select uid, username, count(*) from contactlist natural inner join "user" group by uid, username;'
        # cursor.execute(query)
        result = []
        # for row in cursor:
        #     result.append(row)
        # self.conn.close()
        return result

    def getContactsByUserId(self, uid):
        users = []
        if uid == 1:
            users.append({'id': 1, 'username': 'Renier', 'password': '3425252', 'person_id': '4', 'active': 'Y'})
        if uid == 2:
            users.append({'id': 1, 'username': 'Renier', 'password': '3425252', 'person_id': '4', 'active': 'Y'})
            users.append({'id': 2, 'username': 'Julian', 'password': '34523452', 'person_id': '2', 'active': 'N'})
        return users

    def insertContactToList(self, owner, uid):
        # cursor = self.conn.cursor()
        # query = 'insert into contactlist values(%s, %s);'
        # cursor.execute(query, (owner, uid))
        # self.conn.commit()
        print("Contact Inseted to list.")
