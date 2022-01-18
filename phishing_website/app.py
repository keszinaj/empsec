from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        req = request.form
        login = req["login"]
        psw = req["password"]
        print(req)
    return render_template("login.html")

@app.route("/login")
def hello():
    return render_template('templates/login.html')
