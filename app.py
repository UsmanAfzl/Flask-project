from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def greetings():
    headLine = "Usman is freaking awesome!"
    return render_template("index.html", headLine = headLine)