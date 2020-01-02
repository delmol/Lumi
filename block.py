import hashlib

class Block:
	
	def __init__(self, data):
		self.blockHeight = 0
		self.blockTimestamp = 0
		self.blockReward = 1
		self.blockDifficulty = 1
		self.blockTransactions = data
		self.blockHash = ""
		self.blockParentHash = ""
		self.blockNonce = 0
	
	def initBlock():
		
