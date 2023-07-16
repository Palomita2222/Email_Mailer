import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
from time import sleep

dia = 0
sender = "robertsaulamota@gmail.com"
password = "cyfcyiixcsdbtiez"
recipients = ["robertsaulamota@gmail.com"]
body = f"La planta en el dia d'avui:"  # Update the body as a string

def send_email(body, sender, recipients, password):
    subject = f"Dia {dia}"
    image_path = f"image{dia}.jpg"

    # Use the fswebcam command-line tool to capture an image    
    os.system(f'fswebcam --no-banner {image_path}')

    with open(image_path, 'rb') as f:
        image = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Attach the body as a plain text message
    msg.attach(MIMEText(body, "plain"))

    image = MIMEImage(image, name=f"Dia {dia}")
    msg.attach(image)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

while True:
    send_email(body, sender, recipients, password)
    dia += 1
    sleep(60*60*24)
