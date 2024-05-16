import smtplib,ssl

from main import context

Username = "sakhareliyayash03@gmail.com"
password = "krcd jksj zmtb efmu"
port = 465
host ="smtp.gmail.com"
receiver = "sakhareliyayash03@gmail.com"

context = ssl.create_default_context()
massage = """\
Subject: Hi,
hello,How are you?
Good Morning 
"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(Username,password)
    server.sendmail(Username,receiver, massage)