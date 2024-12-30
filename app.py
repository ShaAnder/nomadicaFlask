#import os to getting our app running
import os

#first we import flask
from flask import Flask

#now we create our flask class instance and storing it in our app variable
#the first argument of the flask class is the name of the module we ill use
app = Flask(__name__)

#now we create our route decorator. 
#routing decorators allow us to tell functions to route to our main pages based on the url
@app.route("/")
def index():
    #instead of running a code snippet we can serve an HTML file using render templates
    return "Hello World"

#now we get our app running with the following argument
#this arguments states if our app script is top level and only allows our code to run
#when the script is executed not on import
if __name__ == "__main__":
    #we get the app to run with the following args, debug = true for debugging and ip/port vars
    #to set default ip and port number incase our OS cannot find them
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )

#having this will allow us to then use "python3 run.py" (or app.py) to run our app
#we should always have debug off if we are running production / submission, make sure to
#turn this off if we're not in dev