import easyimap
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from gpiozero import LED
from time import sleep

login = 'robertsaulamota@gmail.com'
password = 'cyfcyiixcsdbtiez'

sender = "robertsaulamota@gmail.com"
password = "cyfcyiixcsdbtiez"
recipients = ["robertsaulamota@gmail.com"]



break_button = LED(7)
break_button.off()
def stop():
    break_button.on()
    body = f"Command Recieved"
    subject = "Command Recieved, The circuit has been stopped!"
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    

    msg.attach(MIMEText(body, "plain"))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        
    print("Circuit Stopped!")

def start():
    break_button.off()
    body = f"Command Recieved"
    subject = "Command Recieved, The circuit has been restarted!"
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    

    msg.attach(MIMEText(body, "plain"))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        
    print("Circuit Restarted")



def main():
    imapper = easyimap.connect('imap.gmail.com', login, password)
    for mail_id in imapper.listids(limit=1):
        mail = imapper.mail(mail_id)
        if "robertsaulamota@gmail.com" in mail.from_addr:
            if "stop" in mail.body or "Stop" in mail.body:
                if break_button.is_lit != True:
                    stop()
                else:
                    print("Pin is already on!")
            elif "start" in mail.body or "restart" in mail.body or "Start" in mail.body or "Restart" in mail.body:
                if break_button.is_lit != False:
                    start()
                else:
                    print("Pin is already off!")
    
while True:
    main()
    sleep(1)
