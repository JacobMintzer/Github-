# Self-replicating Github repo 
This repo contains code that will replicate this GitHub Repo. Authentication is done through OAuth2, so you will not have to give this application your password. The OAuth2 and http requests are handled through the python library Requests-OAuthlib. The program receives the OAuth2 token by hosting temporarily hosting a flask webapp, and using that to finish the process of forking the GitHub Repository. Once the repository is forked, the user is redirected to a page with a clickable link to the cloned repository, and the webserver is closed.

## Installation
The first thing you'll need to do is go to https://github.com/settings/applications/new and fill in the fields as shown below.
![OAuth2 settings](/github%20oauth.png)

and put your clientID and clientSecret in Credentials.json.

Next download the contents of this repo.

Next you have to make sure you have Python3. To install python3 please download it [here](https://www.python.org/downloads/).

In the environment, install the dependencies on unix-based systems by using this command in the terminal
`pip3 install -r /path/to/requirements.txt`
and in Windows environments by running this in powershell or command prompt
`python -m pip install -r /path/to/requirements.txt`

Once the dependencies are installed you can proceed to running the program by running in unix based environments
`python3 Replicate.py`
or in Windows environments with
`python Replicate.py`
and then authenticating using the browser that shows up. If the browser does not show up, a link will also appear in the terminal with instructions.
