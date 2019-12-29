#import Flask class from flask
from flask import Flask, render_template 
#app variable is created and setting it to instance of Flask class
# __name__ is a special variable name in Python used to name the module
#Thus, it helps to instantiate Flask in app variable.
#We import render_template function for routing.
app = Flask(__name__)


#Adding static content

posts=[
	{
		'author':'RD Sharma',
		'subject':'Maths',
		'class':'All'
	},
	{
		'author':'HC Verma',
		'subject':'Physics',
		'class':'12th'
	}
	
]




#routes are content we type in URL of browzer for going to different pages.
#@app.route decorator helps to navigate and show correct content on UI.
# '/' is the root page of the website.

#Below we have 2 decorators, handling multiple routes. Thus, the two routes are handled by the same function.
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',title='Home', postList=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='About')
	

	
#This condition is true only if script is run directly.
#To run the module directly, we use py flaskblog.py
if __name__ == '__main__':
	app.run(debug=True)