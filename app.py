#MONGOLAB SERVER DETAILS 
server = 'ds149335.mlab.com:49335/cmbwsapi'
port = 41875
db_name = 'cmbwsdb'
username = 'ishan'
password = 'ishan'

from flask import Flask, session, redirect, url_for, escape, request
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
@app.route('/register', methods=['POST'])
def register():
	psid = request.form['psid']
	pwd = request.form['password']
	managerName = request.form['managerName']
	managerContact = request.form['managerContact']
	user = {
		'psid' : [psid],
		'pwd' : [pwd],
		'managerName' : [managerName],
		'managerContact' : [managerContact]
	}
	result=usersCollection.insert_one(user)
	return 'true'

#LOGIN ENDPOINT
@app.route('/login', methods=['POST'])
def loginpage():
	psid = request.form['psid']
	pwd = request.form['password']
	data= usersCollection.find_one({'psid': psid})
	print(psid,pwd,data['pwd'][0].encode("utf-8"))
	if (data['pwd'][0].encode("utf-8") == pwd):
		return "true"
	return "false"

#MAIN
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
