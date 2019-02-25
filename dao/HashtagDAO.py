class HashtagDAO:
	def __init__(self):
		# hashtag_id, hash_text
		self.hashtags = [[0, 'travel'],
						 [1, 'beautiful'],
						 [2, 'food'],
						 [3, 'art']]

		# message_id, text, date
		self.messages = [[0, 'Out here in Bali!', '24-2-2019'],
						 [1, 'Look at this picture of Scarlett Johansson', '24-2-2019'],
						 [2, 'Dining at Satellite Diner!', '25-2-2019'],
						 [3, 'Finally got to see the Mona Lisa', '26-2-2019']]

		self.messageHashtag = [[1, 1],
							   [2, 2],
							   [3, 3],
							   [4, 4]]

	def getAllHashtags(self):
			return self.hashtags

	def getHashtagById(self, hashtag_id):
			return self.hashtags[hashtag_id]

	def getHashtagText(self, hashtag_id):
			return self.hashtags[hashtag_id][1]

