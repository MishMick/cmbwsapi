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


db=client.cmbwsapi
usersCollection = db.users

@app.route('/')
def index():
    return "Women Safety APP"

@app.route('/userExists/<int:psid>', methods=['GET'])
def userExists(psid):
    if psid == 1:
    	return "test"
    else:
    	return "ps != 1"

@app.route('/validate/<int:psid>/<string:pwd>', methods=['GET'])
def validate(psid,pwd):

    data= usersCollection.find_one({'psid': psid})
    
    if (data['pwd'][0].encode("utf-8") == pwd):
        return "True"

    return "False"


 
@app.route('/register/<int:psid>/<string:pwd>/<string:role>', methods=['POST'])
def register(psid,pwd,role):
    user = {
        'psid' : [psid],
        'pwd' : [pwd],
        'role' : [role] 
    }

    result=usersCollection.insert_one(user)
    return 'Debug : Created ' + str(result.inserted_id)


@app.route('/login')
def loginpage():
	return """
	<h1>Login page</h1>
	"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

