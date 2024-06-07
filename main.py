from flask import Flask, render_template

app = Flask(__name__)

menu = ["Новости", "О нас", "Галерея"]

@app.route("/")
def index():
    return render_template('index.html', menu=menu)

@app.route("/news")
def news():
    return render_template('news.html', menu=menu)
if __name__ == '__main__':
    app.run(debug=True)