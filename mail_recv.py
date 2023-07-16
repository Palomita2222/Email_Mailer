import easyimap
from gpiozero import LED

break_button = LED(7)
def stop():
    led.toggle()


login = 'robertsaulamota@gmail.com'
password = 'cyfcyiixcsdbtiez'

imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=1):
    mail = imapper.mail(mail_id)
    if "robertsaulamota@gmail.com" in mail.from_addr:
        if "stop" in mail.body:
            print("Stop/Start Executed succesfully")
            stop()

    print(mail.from_addr)
    print(mail.body)
