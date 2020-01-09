# Self-replicating Github repo 
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
