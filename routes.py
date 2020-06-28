from main import app, blockchain, startServer
import os
from uuid import uuid4

# save ip to a var for later use
node_identifier = str(uuid4()).replace("-", "")

@app.route("/", methods=["GET"])
def helloWorld():
	return "Hello, World!\nNode is online."

# route to mine/POST a blok
	
# route to create/POST a new financial transaction

# route to register/POST a new neighbor

# route to resolve neighboring chains (get the longest one from friends)

# route to shut down the server (for development purposes, don't use in actual apps unless you want anyone at all to be able to turn off your server at any time)
@app.route("/terminate", methods=["POST"])
def shutdownServer():
	try:
		CTRL_C_EVENT = 0
		GenerateConsoleCtrlEvent(CTRL_C_EVENT, 0)
		return "Worked"
	except Exception as e:
		os._exit(0)
		return e



startServer()