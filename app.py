from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def greetings():
    names = ["Alice", "Jacob","Billie"]
    return render_template("index.html", names = names)