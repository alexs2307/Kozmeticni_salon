from flask import Flask, render_template,request
from flask_mail import Mail,Message



app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "spletnastran2022@gmail.com"
app.config['MAIL_PASSWORD'] = "wsoqyoaqhapgdxnm"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cenik")
def price():
    return render_template("cenik.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name=request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject='Lepotni studio Anais',body=f"Ime in Priimek: {name}\n\nE-mail: {email}\n\n\n{message}", sender='Spletna Stran' , recipients=['lepotnistudioanais@gmail.com'])
        mail.send(msg)
        return render_template("contact.html", success=True)

    return render_template("contact.html")

@app.route("/success.html")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)