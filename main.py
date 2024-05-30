from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/news")
def news():
    return "<h1> Новости </h1>"
if __name__ == '__main__':
    app.run(debug=True)