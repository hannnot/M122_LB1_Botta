import configparser
from configparser import ConfigParser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = config['GMAILCONFIG']['email']
sender_pass = config['GMAILCONFIG']['pwd']
receiver_address = open(config['EMAILFILE']['path'], "r").read()
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line

message.attach(MIMEText(mail_content, 'plain'))

pdfname = config['ATTACHMENTFILE']['path']
 
# open the file in bynary
binary_pdf = open(pdfname, 'rb')
 
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())
 
# enconding the binary into base64
encoders.encode_base64(payload)
 
# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

timestamp = datetime.now()
fileName = timestamp.strftime("%d%m%Y%H%M%S.txt")
timestamp = timestamp.strftime("%d%m%Y%H%M%S")
file = open(config['OUTPUTFILE']['path']+fileName, "x")
file = open(config['OUTPUTFILE']['path']+fileName, "a")
file.write(timestamp + " Sent E-Mail to " + receiver_address)
file.close()
