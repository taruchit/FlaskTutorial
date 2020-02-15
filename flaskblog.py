#import Flask class from flask
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm
#app variable is created and setting it to instance of Flask class
# __name__ is a special variable name in Python used to name the module
#Thus, it helps to instantiate Flask in app variable.
#We import render_template function for routing.

app = Flask(__name__)

#Adding secret key for protecting our application
app.config['SECRET_KEY'] = '28f2671dc4e709f5cc91904dfbcd7df6'

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


counter=1

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
	global counter
	counter +=1
	#return render_template('about.html', title='About')
	return render_template('about.html', contents=counter)
	
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
	
@app.route("/login", methods=['GET','POST'])
def login():
		#We create instance of our form.
		form = LoginForm()
		if form.validate_on_submit():
			if form.email.data=='admin@blog.com'  and form.password.data=='password':
				flash('You have been logged in successfully','success')
				return redirect(url_for('home'))
			else:
				flash('Login was not successfull','danger')
		return render_template('login.html', form=form)
	
#This condition is true only if script is run directly.
#To run the module directly, we use py flaskblog.py
if __name__ == '__main__':
	app.run(debug=True)