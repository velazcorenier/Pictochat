from flask import jsonify
from dao.HashtagDAO import HashtagDAO

class HashtagHandler:

	# hashtag_id, hash_text
	def build_hashtag_dict(self, row):
		result = {}
		result['hashtag_id'] = row[0]
		result['hash_text'] = row[1]

		return result
	def getAllHashtags(self):
		dao = HashtagDAO()
		hashtags_list = dao.getAllHashtags()
		results_list = []

		for row in hashtags_list:
			result = self.build_hashtag_dict(row)
			results_list.append(result)

		return jsonify(Hashtags=results_list)

	def getHashtagById(self, hashtag_id):
		hashtag = HashtagDAO().getHashtagById(hashtag_id)

		if not hashtag:
			return jsonify(Error="NOT FOUND"), 404
		
		result = []
		result.append(hashtag)

		hashtag = self.build_hashtag_dict(result[0])

		return jsonify(Hashtag=hashtag)

	def getHashtagText(self, hashtag_id):
		hashtag_text = HashtagDAO().getHashtagText(hashtag_id)

		if not hashtag_text:
			return jsonify(Error="NOT FOUND"), 404
		
		result = {}
		result['hashtag_text'] = hashtag_text

		return jsonify(Hashtag_text=result)

	def createHashtag(self, hashtag_text):
		return jsonify(CreateStatus="Created"), 201

	def updateHashtag(self, hashtag_id, hashtag_text):
		return jsonify(UpdateStatus="Updated"), 200

	def deleteHashtag(self, hashtag_id):
		return jsonify(DeleteStatus="Deleted"), 200