class UserDao:
     def getAllUser(self):
         users = []
         users.append({'id': 1, 'username': 'Renier', 'password': '3425252', 'person_id': '4', 'active': 'Y'})
         users.append({'id': 2, 'username': 'Julian', 'password': '34523452', 'person_id': '2', 'active': 'N'})
         return users