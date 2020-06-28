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
	def registerNode(self, address):
		parsedURL = urlparse(address)

		if parsedURL.netloc:
			self.nodes.add(parsedURL.netloc)
		elif parsedURL.path:
			self.nodes.add(parsedURL.path)
		else:
			raise ValueError("Invalid address")
	
	# verify if a chain is valid
	def validChain(self, chain):
		lastBlock = chain[0]
		i = 1

		while i < len(chain):
			block = chain[i]
			lastBlockHash = self.hash(lastBlock)

			if block["previousHash"] != lastBlockHash:
				return False
			
			lastBlock = block
			i += 1

		return True

	# resolve conflicts between neighbors' chains
	# for this app, we'll simply say the longest chain is the correct one
	def resolveConflicts(self):
		neighbors = self.nodes
		newChain = None

		maxLen = len(self.chain)

		for node in neighbors:
			response = requests.get(f"http://{node}/chain")

			if response.statusCode == 200:
				length = response.json()["length"]
				chain = response.json()["chain"]

				if length > maxLen and self.validChain(chain):
					maxLen = length
					newChain = chain
		
		if newChain:
			self.chain = newChain
			return True
		return False

	# create a new blok and add it to the chain
	def newBlock(self, proof, previousHash):
		block = {
			"index": len(self.chain) - 1,
			"timestamp": time(),
			"transactions": self.currentTransactions,
			"proof": proof,
			"previousHash": previousHash or self.has(self.chain[-1])
		}
		self.currentTransactions = []
		self.chain.append(block)
		return block

	# create new financial transaction and add it to our current list of transactions
	def newTransaction(self, sender, recipient, amount):
		self.currentTransactions.append({
			"sender": sender,
			"recipient": recipient,
			"amount": amount
		})

		return self.lastBlock["index"] + 1

	# get last blok in the chain
	@property
	def lastBlock(self):
		return self.chain[-1]

	# create cryphtograhpci hash in SHA256
	@staticmethod
	def hash(block):
		strBlock = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(strBlock).hexdigest()

	# create and validate the proof of work of a blok
	# note that iterating the value of proof isn't a particularly efficient way of doing this, and you shouldn't do
	# that in an actual application.
	def createProofOfWork(self, lastBlock):
		lastProof = lastBlock["proof"]
		lastHash = self.hash(lastBlock)

		proof = 0
		while self.validProof(lastProof, proof, lastHash) is False:
			proof += 1

		return proof

	# check if a proof of work is valid
	# note that this is a REALLY bad and inefficient way of going about this. Don't use this in an actual application,
	# remember this is for educational purposes, not a demonstration of a functional and secure application
	@staticmethod
	def validProof(lastProof, proof, lastHash):

		guess = f"{lastProof}{proof}{lastHash}".encode()
		guess_hash = hashlib.sha256(guess).hexdigest()

		return guess_hash[:4] == "0000" # if the first 4 bits are zero, our hash is considered valid
