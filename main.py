import mail_recv as recv
import img_raspberry as send
import threading

t = threading.Thread(target=recv.main)
t.daemon = True
t.start()

ot = threading.Thread(target=send_email)
to.daemon == True
to.start()


    

