from flask import Flask,redirect,url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask App!</h1>"

@app.route('/pass/<name>/<mark>')
def pass_page(name,mark):
    return f"<h1>Congratulations {name.title()}! You have passed the exam with {mark} marks!</h1>"

# Added <name> parameter to the route so it can accept the name argument
@app.route('/fail/<name>/<mark>')
def fail_page(name,mark):
    return f"<h1>Sorry {name.title()} as you have scored {mark}, you have failed the exam. Better luck next time!</h1>"

@app.route('/score/<name>/<int:marks>')
def score(name,marks):
    if marks<33:
        time.sleep(1)
        # we will redirect user to fail page
        return redirect(url_for('fail_page', name=name,mark=marks))
    else:
        time.sleep(1)
        # we will redirect user to pass page
        return redirect(url_for('pass_page', name=name,mark=marks))
# Run the application
if __name__ == '__main__':
    app.run(debug=True,port=5000)