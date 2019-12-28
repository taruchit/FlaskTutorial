Session 1: -
1. Install Flask: pip install flask
2. To verify if Flask is installed correctly: import flask
3. Create a file: flaskblog.py
4. Set environment variable for our file that we want to be the Flask application.
set FLASK_APP=flaskblog.py
5. flask run
The above command helps to start our webserver.
6. If we add <h1> tag in return content, the modified content will be loaded only after retstarting the web server.
7. To overcome the issue in point 6: -
set FLASK_DEBUG=1
flask run
'''Now if we change the content in return and refresh the browzer, the updated data is visible.'''
8. Now, we will add 'About' route.

Session 2 Templates in Flask: -
We created a folder: templates.
Inside the folder we created two files: home.html and about.html
Then, we imported render_template function in flaskblog.py.
Finally, in /home route, we called render_template() and passed the file home.html as the argument.

