from flask import Flask, render_template


app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cenik")
def price():
    return render_template("cenik.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/success.html")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)