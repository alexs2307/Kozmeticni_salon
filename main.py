from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cenik")
def price():
    return render_template("cenik.html")

if __name__ == '__main__':
    app.run(debug=True)