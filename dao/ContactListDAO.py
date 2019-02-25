from dao.UserDAO import UserDao


# import psycopg2
# from config.dbconfig import pg_config

class ContactListDAO:
    def __init__(self):
        # user_id, first_name, last_name, email, phone
        self.users = [[1, "Renier", "Velazco", "renier.velazco@upr.edu", "787-247-4930"],
                      [2, "Cristian", "Torres", "cristian.torres2@upr.edu", "787-218-2447"],
                      [3, "Julian", "Cuevas", "julian.cuevas1@upr.edu", "7876074678"]]

    # TODO: Implement
    def allContactLists(self):
        result = []
        return result

    def getContactsByUserId(self, uid):
        users = []
        if uid == 1:
            users.append(self.users[0])
            users.append(self.users[1])

        return users

    def insertContactToList(self, owner, uid):

        print("Contact Inseted to list.")
