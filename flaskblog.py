#import Flask class from flask
from flask import Flask 
#app variable is created and setting it to instance of Flask class
# __name__ is a special variable name in Python used to name the module
#Thus, it helps to instantiate Flask in app variable.
app = Flask(__name__)

#routes are content we type in URL of browzer for going to different pages.
#@app.route decorator helps to navigate and show correct content on UI.
# '/' is the root page of the website.

#Below we have 2 decorators, handling multiple routes. Thus, the two routes are handled by the same function.
@app.route("/")
@app.route("/home")
def home():
	return "<h1> Home Page </h1>"


@app.route("/about")
def about():
	return "<h1> About Page </h1>"

	
#This condition is true only if script is run directly.
#To run the module directly, we use py flaskblog.py
if __name__ == '__main__':
	app.run(debug=True)