from flask import Flask

app = Flask(__name__)

@app.route("/")
def greetings():
    return "Hello world"


@app.route("/<string:name>")
def greet(name):
    name = name.capitalize()
    return f"<h1>Hello {name}!</h1>"