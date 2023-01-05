from flask import Flask,request,make_response
from functools import wraps
import unittest


# creating object for the flask
app = Flask(__name__)


# Giving authentication for the user
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        return make_response('could not verify your login!', 401, {'www-authenticate': 'Basic realm="Login Required"'})
    return decorated


# Taking the data from the user
@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return '<h1>You are succesfully logged in</h1>'

    return make_response('could not verify!', 401, {'www-authenticate': 'Basic realm="Login Required"'})


# Check auth and login the user with route
@app.route('/homepage')
@auth_required
def homepage():
    return '<h1>Already you are in the page</h1>'

# This is another sample page
@app.route('/contactpage')
@auth_required
def contactpage():
    return '<h1>You entered into the contact page</h1>'


# This will used to test the funtionalities
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


# Runing the program
if __name__ == "__main__":
    app.run(debug=True)
