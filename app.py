# Joyce Wu
# Softdev1 pd 7
# HW#04: Fill up yer Flask
# 2017-09-24

from flask import Flask
app = Flask(__name__)

@app.route("/") #route 0
def index(): #creates an index linking the three different routes using html
    return '<h1>Choose your destiny:<br><a href="/happiness">A</a> <a href="/love">B</a> <a href="/passion">C</a></h1>'

@app.route("/happiness") #route 1
def happy():
    return "Can you really find happiness in life?"

@app.route("/love") #route 2
def love():
    return "What is love?"

@app.route("/passion") #route 3
def passion():
    return "What do you do on your free time?"

if __name__ == "__main__":
    app.debug = True
    app.run()
