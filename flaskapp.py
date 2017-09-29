#!/usr/bin/env python
from flask import Flask, render_template
from utils import occupation
#import occupation, csv, random

app = Flask(__name__)

@app.route("/")
def root():
        return "root"

@app.route("/occupations")
def main():
    return render_template('occupations.html', listkeys = occupation.createDict().keys(), d = occupation.createDict(), randomJob = occupation.weightedRandom(occupation.createDict()))

if __name__ == "__main__":
        app.debug = True
        app.run()
