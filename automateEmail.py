from re import sub
import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'sender's email address'
email_password = 'yourpassword'
email_receiver = 'receiver's email address'


subject = 'automate email'
body = """
Hello,
This is Jinny Yun.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
