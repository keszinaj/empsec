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

if __name__=="__main__":
    app.run(debug=True)
