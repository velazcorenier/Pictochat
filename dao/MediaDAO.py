class MediaDAO:
	def __init__(self):
		# media_id, media_type, location
		self.medias = [[0, 'photo', '/home/jdcuevas/Photos/mountain.jpg'],
						 [1, 'photo', '/home/jdcuevas/Photos/spain.jpg'],
						 [2, 'video', '/home/jdcuevas/Photos/mydog.mp4'],
						 [3, 'photo', '/home/jdcuevas/Photos/italy.jpg']]

		# message_id, text, date
		self.posts = [[0, '24-2-2019'],
						 [1, '24-2-2019'],
						 [2, '25-2-2019'],
						 [3, '26-2-2019']]

		# post_id, media_id
		self.postMedia = [[0, 0],
							   [1, 1],
							   [2, 2],
							   [3, 3]]

	def getAllMedia(self):
			return self.medias

	def getMediaById(self, media_id):
			return self.medias[media_id]

	def getMediaType(self, media_id):
			return self.medias[media_id][1]

	def getMediaLocation(self, media_id):
			return self.medias[media_id][2]
