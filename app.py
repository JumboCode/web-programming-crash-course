from flask import Flask
from flask import request

app = Flask(__name__)

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        req_data = request.get_json()
        message = req_data['message']
        if (message):
            posts.append(message)
            return ("Posted message: " + message)
        else:
            return "Error: Did not recieve 'message' in POST request"
    else:
        response = "Posts: \n"
        for post in posts:
            response = response + post + "\n"
        return response
