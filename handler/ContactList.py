from dao.ContactListDAO import ContactListDAO
from flask import jsonify


class ContactListHandler:

    def build_contactList_dict(self, cl):
        mapped = {'uid': cl[0], 'username': cl[1], 'Number of contacts': cl[2]}
        return mapped

        # Dictionaries

    def build_user_dict(self, row):
        result = row
        # result['user_id'] = row[0]
        # result['username'] = row[1]
        # result['password'] = row[2]
        # result['person_id'] = row[3]
        # result['is_Active'] = row[4]
        return result

    def mapToDict(self, row):
        result = {'contactid': row[0], 'contactusername': row[1]}
        return result

    def getAllContactLists(self):
        contactList = ContactListDAO().allContactLists()
        if not contactList:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for cl in contactList:
            result.append(self.build_contactList_dict(cl))
        return jsonify(AllContactList=result)

        # This method return a contact list of an user.

    def getContactsByUserId(self, uid):
        dao = ContactListDAO()
        contact_list = dao.getContactsByUserId(uid)
        result_list = []
        for row in contact_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def contactAddition(self, owner, uid):
        dao = ContactListDAO().insertContactToList(owner, uid)
        return jsonify(Result=dao), 200
