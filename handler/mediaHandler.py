from flask import jsonify
from dao.MediaDAO import MediaDAO

class MediaHandler:

	# hashtag_id, hash_text
	def build_media_dict(self, row):
		result = {}
		result['media_id'] = row[0]
		result['media_type'] = row[1]
		result['media_location'] = row[1]

		return result

	def getAllMedia(self):
		dao = MediaDAO()
		media_list = dao.getAllMedia()
		results_list = []

		for row in media_list:
			result = self.build_media_dict(row)
			results_list.append(result)

		return jsonify(Media=results_list)

	def getMediaById(self, media_id):
		media = MediaDAO().getMediaById(media_id)

		if not media:
			return jsonify(Error="NOT FOUND"), 404
		
		result = []
		result.append(media)

		media = self.build_media_dict(result[0])

		return jsonify(Media=media)

	def getMediaType(self, media_id):
		media_type = MediaDAO().getMediaType(media_id)

		if not media_type:
			return jsonify(Error="NOT FOUND"), 404
		
		result = {}
		result['media_type'] = media_type

		return jsonify(Media_Type=result)

	def getMediaLocation(self, media_id):
		media_location = MediaDAO().getMediaLocation(media_id)

		if not media_location:
			return jsonify(Error="NOT FOUND"), 404
		
		result = {}
		result['media_location'] = media_location

		return jsonify(Media_Location=result)

	def createMedia(self, media_type, media_location):
		return jsonify(CreateStatus="Created"), 201

	def updateMedia(self, media_id, media_type, media_location):
		return jsonify(UpdateStatus="Updated"), 200

	def deleteMedia(self, media_id):
		return jsonify(DeleteStatus="Deleted"), 200