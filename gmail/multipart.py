import smtplib 

from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email import encoders

fromaddr = 'SENDER EMAIL ADDRESS'
toaddr = 'RECIPIENT EMAIL ADDRESS'

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = 'This is the subject of my email'

body = 'This is the body of my email'

msg.attach(MIMEText(body))

#  paths of the files we want to use
files = ['PATH TO FILE 1', 'PATH TO FILE 2', 'OTHER FILES']

for filename in files:
    attachment = open(filename, 'rb')
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    msg.attach(part)
    attachment.quit()

msg = msg.as_string()

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromaddr, 'gpjeukeadncvznul')
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print('Email sent successfully')
except:
    print("Email couldn't be sent")
