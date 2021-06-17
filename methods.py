from configparser import ConfigParser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime


# This function sends an E-Mail to the E-Mail adress which was created in the .txt file before
def sendEmail(config: ConfigParser, receiver_address: str):
    
    # The sending mail address and password from the config file
    sender_address = config['GMAILCONFIG']['email']
    sender_pass = config['GMAILCONFIG']['pwd']

    mail_content = '''Hallo,
    Dieses Mail wurde im Rahmen des Moduls 122 gesendet
    '''
    
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line

    message.attach(MIMEText(mail_content, 'plain'))

    #pdf file from the config file
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

#This function reads and returns the E-Mail which is written in the .txt file
def openEmail(config: ConfigParser):
    email = open(config['EMAILFILE']['path'], "r").read()
    return email

#This function creates a new .txt file in the folder which is set in the config file.
def createOutput(config: ConfigParser, receiver_address: str):
    timestamp = datetime.now()
    fileName = timestamp.strftime("%d%m%Y%H%M%S.txt")
    timestamp = timestamp.strftime("%d%m%Y%H%M%S")
    file = open(config['OUTPUTFILE']['path']+fileName, "x")
    file = open(config['OUTPUTFILE']['path']+fileName, "a")
    file.write(timestamp + " Sent E-Mail to " + receiver_address)
    file.close()