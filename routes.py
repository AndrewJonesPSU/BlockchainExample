from main import app
import os

# route to mine/POST a blok
	
# route to create/POST a new financial transaction

# route to register/POST a new neighbor

# route to resolve neighboring chains (get the longest one from friends)

# route to shut down the server (for development purposes, don't use in actual apps unless you want anyone at all to be able to turn off your server at any time)
@app.route("/terminate", methods=["GET"])
def shutdownServer():
	try:
		CTRL_C_EVENT = 0
		GenerateConsoleCtrlEvent(CTRL_C_EVENT, 0)
		return "Worked"
	except Exception as e:
		os._exit(0)
		return e