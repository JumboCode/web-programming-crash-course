# JumboCode Web Programming Workshop

A Version of this source code lives on a Heroku instance at [https://jcwebworkshop.herokuapp.com/](https://jcwebworkshop.herokuapp.com/). 

If you go to that site, you'll see something like `posts: ...`
If you hit the server with a `POST` request: 

`curl jcwebworkshop.herokuapp.com/ -d '{"message":"YOUR MESSAGE HERE"}' -H 'Content-Type: application/json'`

and go back to the site, you'll see your message there!

### Get A Working Development Environment 

1. Clone this repo with `git clone https://github.com/JumboCode/web-programming-crash-course.git`
2. Install python on your machine, for the purposes of this tutorial there are instructions that should work with both python2 and python3.
3. Create a virtual environment for your dependencies.
    * If on python3, create the environment with `python -m venv venv`
    * If on python2, install the pip package virtualenv globaly with `pip install virtualenv`
        * Once virtualenv is installed, create a virtual environment with `virtualenv venv` 
4. Activate the virtual environment you just created with `source venv/bin/activate`. You can see if you were successful by whether a (venv) bubble pops up to the left in the terminal.  
5. Now that we have activated virtual environment, any dependencies we install we be isolated to our `venv` environment. Install the dependencies in the activated environment with `pip install --upgrade -r requirements.txt`
    * If you want to exit the virtual environment at any point, simply type `deactivate`. 

### How to Run the Web Server Locally: 

#### If on a Linux or Mac Machine:

1. `export FLASK_APP=app.py`
2. `export FLASK_ENV=development`
3. `flask run`

#### For Windows cmd, use set instead of export:

1. `set FLASK_APP=app.py`
2. `set FLASK_ENV=development`
3. `flask run`

#### For Windows PowerShell, use $env: instead of export:

1. `$env:FLASK_APP = app.py`
2. `$env:FLASK_ENV = "development"`
3. `flask run`

### Turn Your Server Public!

If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network with:
`flask run --host=0.0.0.0`

### Find Your IP Address
Find instructions on how to find your private IP address [here](https://lifehacker.com/5833108/how-to-find-your-local-and-external-ip-address).


### Make a Request to Your Friend's Server
*Warning: be sure you and your partner are both on Tufts_Secure!*
Once you have your IP address, give it to the person sitting next to you - while your server is running, as them to 'hit' your server by sending a curl request `curl [your IP address]:5000`. They should get the same 'Hello, world!' message you saw from Heroku!
Alternatively, if they type your IP address into their browser, they should see the same message.

### Extending for dynamic data! 
Right now, your server is only has 1 valid route, `GET` at the index, `/`
Let's extend that! 

### Dependencies
First, let's add another dependency to the file, that will be useful for handling data later. 

add:
`from flask import request`
to the top of your `app.py` file. 

### Adding another route method 
To make your index route accept both `GET` and `POST` requests, change your `@app.route` line to:

`@app.route('/', methods=['GET', 'POST'])` 

to enable your idex route to support both of these request types.

Next, let's distinguish between these routes: 
```
def index():
    if request.method == 'POST':
      # logic for handling post
    else:
      # logic for handling get
```

### Handling the POST route:
Let's assume that the data we're recieving on this route will be in JSON format (`'{"message":"YOUR MESSAGE HERE"}'`) 

To parse it, add this to your post-handling-logic: 

```
req_data = request.get_json()
        message = req_data['message']

```

Now, let's save that message somewhere! 
First, add an empty array at a global scope to store messages:

` posts = []`

Next, add some code to store the incoming message, and handle the common error in which we don't have a propper formated incoming json body: 

```
        if (message):
            posts.append(message)
            return ("Posted message: " + message)
        else:
            return "Error: Did not recieve 'message' in POST request"
```

Now, when you hit your server with a post-request, you'll get a response back with your message! Try it out: 

`curl http://127.0.0.1:5000/ -d '{"message":"YOUR MESSAGE HERE"}' -H 'Content-Type: application/json'`

### Handling the GET route:
When a get-request hits this endpoint, let's return all the messages: 

add this to the GET block: 
```
        response = "Posts: \n"
        for post in posts:
            response = response + post + "\n"
        return response
```

Now, you're code should mimic the heroku server! 
Try it out, hitting your, and a friend's, server with both of these routes. 


# Stuck? 
Check out the `finished-app.py` code in this repo!
