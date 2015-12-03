from flask import Flask

app = Flask(__name__)

@app.route('/test')
def hello_world():
    return "hey"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == '__main__':
    print("initializing")
    app.run()

