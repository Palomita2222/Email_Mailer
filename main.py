import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
from time import sleep
import cv2
sender = "sender@gmail.com"
password = "use a google app password after 2 step verification on the sender account"
recipients = ["recv@gmail.com"]
body = "message"  # Update the body as a string

def send_email(body, sender, recipients, password):
    subject = "whatever"

    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        _, frame = cap.read()
        cap.release()  # releasing camera immediately after capturing picture
        if _ and frame is not None:
            cv2.imwrite(f'image.jpg', frame)

    with open(f'image.jpg', 'rb') as f:
        image = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Attach the body as a plain text message
    msg.attach(MIMEText(body, "plain"))

    image = MIMEImage(image, name=f"Name")
    msg.attach(image)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(body, sender, recipients, password)
