uclass UserDao:
    def getAllUser(self):
        users = []
        users.append({'id': 1, 'username': 'Renier', 'password': '3425252', 'person_id': '4', 'active': 'Y'})
        users.append({'id': 2, 'username': 'Julian', 'password': '34523452', 'person_id': '2', 'active': 'N'})
        return users

    def getUserById(self, uId):
        user = {'id': 1, 'username': 'Renier', 'password': '3425252', 'person_id': '4', 'active': 'Y'}

        return user

    def getAllUserByChat(self, chatId):
        users = []
        users.append({'id': 1, 'username': 'Renier', 'password': '3425252', 'person_id': '4', 'active': 'Y'})
        users.append({'id': 2, 'username': 'Julian', 'password': '34523452', 'person_id': '2', 'active': 'N'})
        return users

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
        # cursor = self.conn.cursor()
        # query = "select * from user where firstName = %s and lastName = %s;"
        # cursor.execute(query, (material, color))
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

    # CRUDS

    def insert(self, username, password, firstName, lastName):
        # cursor = self.conn.cursor()
        # query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        # cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        # uid = cursor.fetchone()[0]
        # self.conn.commit()
        uid = 0
        return uid

    def delete(self, uid):
        # cursor = self.conn.cursor()
        # query = "delete from parts where pid = %s;"
        # cursor.execute(query, (pid,))
        # self.conn.commit()
        return uid

    def update(self, uid, password, firstName, lastName):
        # cursor = self.conn.cursor()
        # query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        # cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        # self.conn.commit()
        return uid

    def getCountByUserId(self):
        # cursor = self.conn.cursor()
        # query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        # cursor.execute(query)
        result = []
        # for row in cursor:
            # result.append(row)
        return result

    def getCredentials(self, username, password):
        # cursor = self.conn.cursor()
        # query = 'select uid,username from "user" where username = %s and password = %s;'
        # cursor.execute(query, (username, password,))
        # result = cursor.fetchone()
        result = 0
        return result

    def insertUser(self, firstname, lastname, phone, email, password, username):
        # cursor = self.conn.cursor()
        # query = 'insert into "user"(firstname, lastname, phone, email, password, username) values (%s, %s, %s, %s, %s, %s) returning uid;'
        # cursor.execute(query, (firstname, lastname, phone, email, password, username,))
        # uid = cursor.fetchone()[0]
        # self.conn.commit()
        # return uid
        return 0