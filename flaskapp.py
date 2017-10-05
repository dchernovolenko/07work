#!/usr/bin/env python
from flask import Flask, render_template, request, session

app = Flask(__name__)
username = "hi"
password = "hello"
app.secret_key = "haha"
@app.route("/")
def root():
        if not session.get("logged"):
            return render_template('login.html')
        else:
            return render_template("welcome.html")

@app.route("/login", methods = ["GET", "POST"])
def response():
    if request.args["name"] == username and request.args["pass"] == password:
        session["logged"] = True
        return render_template("welcome.html")
    elif request.args["name"] == username and request.args["pass"] != password:
        return render_template("error.html", err = "wrong pass")
    elif request.args["name"] != username and request.args["pass"] == password:
        return render_template("error.html", err = "wrong user")
    else:
        return render_template("error.html", err = "both wrong")

@app.route("/welcome")
def logout():
    if request.args["lo"]:
        session.pop("logged")
        return render_template("login.html")


if __name__ == "__main__":
        app.debug = True
        app.run()
