# JumboCode Web Programming Workshop

A Version of this source code lives on a Heroku instance at [https://jcwebworkshop.herokuapp.com/](https://jcwebworkshop.herokuapp.com/). 

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
