# Use a database already created on mongolab 
server = 'ds149335.mlab.com'
port = 41875
db_name = 'cmbwsdb'
username = 'ishan'
password = 'ishan'

from flask import Flask
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

uri = "mongodb://"+username+":"+password+"@"+server
client = MongoClient(uri)

print ("!!!!!!!!!!!!!!!!!!!!!!!!!")
print (client)
print ("!!!!!!!!!!!!!!!!!!!!!!!!!")

@app.route('/')
def homepage():
    return "<h1>Hello this is the main page of our API</h1> "

@app.route('/login')
def loginpage():
	return """
	<h1>Login page</h1>
	"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

