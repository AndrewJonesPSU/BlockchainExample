from time import time
from urllib.parse import urlparse

import hashlib
import json
import requests


class Blockchain:
	def __init__(self):
		self.chain = [] # normally a linked list, but this isn't ment to be a complex blockchain app, just an educational example
		self.nodes = set() # set of all other nodes (aka servers) on the network
		self.currentTransactions = [] # current transactions that haven't been passed to a blok

		# create first blok of chain
		self.newBlock(previousHash = '1', proof = 100)

	# register another user's node in PAB
	def registerNode(self):
		pass
	
	# verify if a chain is valid

	# resolve conflicts between neighbors' chains

	# create a new blok

	# create new financial transaction



	# get last blok in the chain
	@property
	def lastBlock(self):
		return self.chain[-1]

	# create cryphtograhpci hash in SHA256
	@staticmethod
	def hash(block):
		strBlock = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(strBlock).hexdigest()

	# check the proof of work of a blok

	# check if a proof of work is valid

