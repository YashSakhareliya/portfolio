import smtplib
import ssl
import os


def send_mail(message):
    Username = "sakhareliyayash03@gmail.com"
    password = os.getenv("PASSWORD")
    port = 465
    host ="smtp.gmail.com"
    receiver = "sakhareliyayash03@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(Username,password)
        server.sendmail(Username,receiver, message)