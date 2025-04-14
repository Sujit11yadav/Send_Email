from flask import Flask,render_template, request, redirect, url_for
from flask_mail import Mail,Message
import os  
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.config['Mail_Server'] = 'smtp.gmail.com'
app.config["Mail_USERNAME"] = os.getenv('DEL_EMAIL')
app.config['Mail_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods= ["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        message = request.form["message"]
        msg  =Message(subject, sender = os.getenv('DEL_EMAIL'), recipients= [os.getenv('REC_EMAIL')])
        msg.body = "Hello From"+ name +",\n\n"+message
        mail.send(msg)
        return redirect(url_for("index"))
    
if __name__ == '__main__':
    app.run(debug=True)

