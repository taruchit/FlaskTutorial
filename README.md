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

Now, we will learn if else: -
We write if else condition in title. If the condition is met then parameter sent along with function is displayed.
If the condition is not met, then else gets executed and default string gets displayed.

Now, we will remove duplicate content from templates: - Template Inheritance
1. We create layout.html, and pick all the repeated sections between the two templates (home and about)
2. We create a block in body tag of layout.html.
3. Now, we will inherit the layout template in home and about template.
4. In home.html, we need to overwrite content with the for loop.

Learning about use of Bootstrap: -

1. In layout.html, we added the required bootstrap css. Thus, it will help to use bootstrap across multiple pages easily.
2. In layout.html, we added the JS code in body tag required for bootstrap.
3. Now we added the content inside Bootstrap class "container".
4. url_for in Flask is used for creating a URL to prevent the overhead of having to change URLs throughout an application (including in templates). Without url_for , if there is a change in the root URL of our app then we have to change it in every page where the link is present.

Adding Navigation menu: -

1. In layout.html, we add html code for our navigation.
2. In href, url_for is used to give the path.

