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

    from pygrabber.dshow_graph import FilterGraph

    # Create a FilterGraph instance
    graph = FilterGraph()

    # Set the video source to the USB camera
    graph.set_input_source(0)  # Use 0 for the default camera

    # Capture an image from the camera
    image_data = graph.get_image()

    # Convert the image data to a Pillow image
    pil_image = Image.frombytes('RGB', (image_data.width, image_data.height), image_data.data, 'raw', 'BGR')

    # Save the image to a file
    image_path = f"image{dia}.jpg"
    pil_image.save(image_path)

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
    sleep(60*60*24)
