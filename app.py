from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Hello this is the main page of our API</h1>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

