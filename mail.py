import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


class Mailer():
    def __init__(self, username, password):
        # Credentials (if needed)
        self.username = username
        self.password = password

    def sendMail(self, toaddr, subject, text):
        msg = MIMEMultipart()
        msg['Date'] = datetime.strftime(datetime.now(), '%Y-%m-%d')
        msg['From'] = self.username
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, toaddr, msg.as_string())
        server.quit()
