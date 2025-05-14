import smtplib
from email.mime.text import MIMEText

def fun(to_email,name):
    sender_email = "vishnucn243@gmail.com"
    password = "qvee ikdz bjwy punt"
    message = f"Dear {name},\n\nHappy Birthday!\n\nBest wishes!"
    
    msg = MIMEText(message)
    msg['Subject'] = "Happy Birthday"
    msg['From'] = sender_email
    msg['To'] = to_email
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

fun("vishnucn34@gmail.com","vishnu")