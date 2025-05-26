from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask App!</h1>"

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Hey {name.title()}, Welcome to the Welcome Page!</h1>"

# @app.route('/welcome/Jahid')
# def welcome_Jahid():
#     return "<h1>Hey Jahid, Welcome to the Welcome Page!</h1>"


# Run the application
if __name__ == '__main__':
    app.run(debug=True,port=5000)