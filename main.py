# handle imports
from uuid import uuid4
from flask import Flask, jsonify, request
import routes

# create flask server
app = Flask(__name__)

# save ip to a var for later use
node_identifier = str(uuid4()).replace("-", "")

# create our blockchain app
blockchain = Blockchain()

# add app arguments
if __name__ == "__main__":
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument("-p", "--port", default=6969, type=int, help="port to listen on")
	args = parser.parse_args()
	port = args.port

	app.run(host="0.0.0.0", port=port)

