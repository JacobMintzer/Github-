import os
import json
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
import webbrowser
import threading
import logging
import time
app=Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route("/callback", methods=["GET"])
def callback():
	with open("Credentials.json") as file:
		credentials=json.load(file)
		
	try:
		githubSession=OAuth2Session(credentials["ClientID"])
		githubSession.fetch_token('https://github.com/login/oauth/access_token',client_secret=credentials["ClientSecret"],authorization_response=request.url)
		response=githubSession.post("https://api.github.com/repos/JacobMintzer/Github_Self-Replicating_Repo/forks")
		return "You have successfully authenticated the Github Self-Replicating Repo! You can find it <a href=\"{0}\">Here</a>".format(json.loads(response.content)["html_url"]),200
	except Exception as e:
		return str(e), 200
	finally:
		endServer()
	

def endServer():
	time.sleep(10)
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

def authenticate():
	print("authenticating")
	with open("Credentials.json") as file:
		credentials=json.load(file)
	githubSession=OAuth2Session(credentials["ClientID"],scope=["public_repo"])
	authorization_url, state = githubSession.authorization_url("https://github.com/login/oauth/authorize")
	#print (authorization_url)
	print("Opening browser to authenticate. If browser does not show up, please copy and paste <{0}> into your browser to continue.".format(authorization_url))
	webbrowser.open(authorization_url, new=2)

if __name__=="__main__":
	os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
	authThread=threading.Thread(target=authenticate)
	authThread.start()
	os.environ['WERKZEUG_RUN_MAIN']='true'
	app.run(debug=False,use_reloader=False, port=8080,)
