#!/usr/bin/env python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
        return render_template('root.html')

@app.route("/response", methods = ["GET", "POST"])
def response():
    return render_template("responsetemp.html", usr = request.args["name"], mtd = request.method)

if __name__ == "__main__":
        app.debug = True
        app.run()
