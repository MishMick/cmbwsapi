#MONGOLAB SERVER DETAILS 
server = 'ds149335.mlab.com:49335/cmbwsapi'
port = 41875
db_name = 'cmbwsdb'
username = 'ishan'
password = 'ishan'

from flask import Flask
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

#DEFINE URL FOR MONGODB SERVER
uri = "mongodb://"+username+":"+password+"@"+server
client = MongoClient(uri)

#GET DATABASE AND TABLE NAME
db=client.cmbwsapi
usersCollection = db.users

#INDEX PAGE
@app.route('/')
def index():
	return "Women Safety APP"

#REGISTER ENDPOINT
@app.route('/register/<int:psid>/<string:pwd>/<string:role>', methods=['POST'])
def register(psid,pwd,role):
	user = {
        'psid' : [psid],
        'pwd' : [pwd],
        'role' : [role] 
	}
	result=usersCollection.insert_one(user)
	return 'Debug : Created ' + str(result.inserted_id)

#LOGIN ENDPOINT
@app.route('/login', methods=['POST'])
def loginpage():
	psid = request.form['psid']
	password = request.form['password']
	print ('User logging in' + psid + password)
	return "true"

#MAIN
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

