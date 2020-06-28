# handle imports

from flask import Flask, jsonify, request

from blockchain import Blockchain

# create flask server
app = Flask(__name__)
import routes

# create our blockchain app
blockchain = Blockchain()

# add app arguments
def startServer():
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument("-p", "--port", default=6969, type=int, help="port to listen on")
	args = parser.parse_args()
	port = args.port

	app.run(host="127.0.0.1", port=port)

