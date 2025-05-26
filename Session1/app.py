from flask import Flask

app = Flask(__name__) # in every module, python gives a special variable __name__ which is the name of the module. whcih is basically the main module in that file.

#Create endpoints for the Flask application
@app.route('/')
@app.route('/home')
def Home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route('/about')
def About():
    return "<h1>About Us</h1><p>This is the about page of our Flask application.</p><h3>we are learning Flask</h3>"



#path parameters
@app.route('/user/<name>') #after the /user path, we are expecting a name from the user
def user(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to your user page.</p>"

@app.route('/user/<name>/<int:age>') #we can also specify the type of the parameter
def user_with_age(name, age):
    return f"<h1>Hello, {name}!</h1><p>You are {age} years old.</p>"



#state the application
# to run the app, use the command: flask run
if __name__ == '__main__': # This application will run only if we are in app.py module
    app.run(debug=True,port=5000)