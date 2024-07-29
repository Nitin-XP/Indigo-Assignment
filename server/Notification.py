import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
accountSid = os.getenv('ACCOUNT_SID')
authToken = os.getenv('AUTH_TOKEN')
client = Client(accountSid, authToken)

def pushNotification(to_number, to_email, body):
    # Sending SMS to Phone Number
    message = client.messages.create(
    to = to_number, # You can Try
    from_ = os.getenv('FROM_PHONE_NUMBER'),
    body = body
    )
    # Sending email
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = "Flight Status"
    msg['to'] = to_email

    user = "multipurposemail15@gmail.com"
    msg['from'] = user
    pwd = "pwww aile ckng ruji"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password=pwd)
    server.send_message(msg)
    server.quit()
