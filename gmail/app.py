import smtplib


def send_email(subject, body):
    try:
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login('dan.nelson1@gmail.com', 'Sunshine-813')
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail('dan.nelson1@gmail.com', 'danelson@nwi.net', message)
        server.quit()
        print('email sent')
    except:
        print('email could not be sent')

subject = 'this is the subject of the email'
body = 'This is the message (body) of the message'
send_email(subject, body)