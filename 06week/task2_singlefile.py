# Single file flask application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/secret/")
def secret_page():
    return "<h1>You found the secret page!</h1>"

# this makes the interpreter run app
if __name__ == '__main__':
    app.run(debug=True)