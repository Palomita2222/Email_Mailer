import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
from time import sleep
import cv2
dia = 0
sender = "robertsaulamota@gmail.com"
password = "cyfcyiixcsdbtiez"
recipients = ["robertsaulamota@gmail.com"]
body = f"La planta en el dia d'avui:"  # Update the body as a string

def send_email(body, sender, recipients, password):
    subject = f"Dia {dia}"

    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        _, frame = cap.read()
        cap.release()  # releasing camera immediately after capturing picture
        if _ and frame is not None:
            cv2.imwrite(f'image{dia}.jpg', frame)

    with open(f'image{dia}.jpg', 'rb') as f:
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
    sleep(1)
