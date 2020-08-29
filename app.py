from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def greetings():
    today = datetime.datetime.now()
    new_year = today.month == 1 and today.day==1
    return render_template("index.html", new_year = new_year)