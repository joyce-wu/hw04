from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Choose your destiny:<br><a href="/happiness">A</a> <a href="/love">B</a> <a href="/passion">C</a></h1>'

@app.route("/happiness")
def happy():
    return "Can you really find happiness in life?"

@app.route("/love")
def love():
    return "What is love?"

@app.route("/passion")
def passion():
    return "What do you do on your free time?"

if __name__ == "__main__":
    app.debug = True
    app.run()
