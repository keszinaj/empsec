import smtplib
import json
from random import seed
from random import randint

class HandleMail:
    def __init__(self):
        self.fake_mail_text = []
        self.link = ''
        self.readMail()
        self.readLink()
        seed(1)
    def readMail(self):
        with open('./fake_mail.json') as f:
            data = json.load(f)
            for tex in data['fake_mail']:
                self.fake_mail_text.append(tex['text'])
    def getText(self):
        v = randint(0, len(self.fake_mail_text) - 1)
        return self.fake_mail_text[v].replace('{phishing_link}', self.link)
    def readLink(self):
        with open('./link.txt') as f:
            self.link = f.read()


class Mail:
    def __init__(self, mail, fake_from, fake_name, subject, text):
        self.fake_from = fake_from
        self.fake_name = fake_name
        self.subject = subject
        self.content = text
        self.to_name = ''
        self.to_email = mail
    def sendMail(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('sonrfid@gmail.com', '')
            message = f"From: {self.fake_name} <{self.fake_from}>\nTo: {self.to_name} <{self.to_email}>\nSubject: {self.subject}\n\n{self.content}"
            smtp.sendmail('sonrfid@gmail.com', self.to_email, message.encode())

if __name__ == "__main__":
    set_server = HandleMail()
    text = set_server.getText()
    fake_from = "donaldtrump@gmail.com"
    fake_name = "Donald Trump"
    subject = "ASAPv"
    with open('./send_to.txt') as my_file:
        for mail in my_file:
            mail_test = Mail(mail, fake_from, fake_name, subject, text)
            mail_test.sendMail()
    print('sent')

