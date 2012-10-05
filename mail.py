import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
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

if __name__ == "__main__":
	mailer = Mailer('df.rodriguez143@gmail.com', 'Staticroof601020763800!')
	toaddr = 'df.rodriguez143@gmail.com'
	subject = 'Task!'
	msg = 'There was a terrible error that occured and I wanted you to know!'
	mailer.sendMail(toaddr, subject, msg)