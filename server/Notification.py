import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
accountSid = os.getenv('ACCOUNT_SID')
authToken = os.getenv('AUTH_TOKEN')
client = Client(accountSid, authToken)

# message = client.messages.create(
#     to = os.getenv('PHONE_NUMBER'),
#     from_ = "+16814994863",
#     body = "Your Flight is On Time."
# )
# print(message)

msg = EmailMessage()
msg.set_content("Your Flight is On Time.")
msg['subject'] = "Flight Status"
msg['to'] = "nitinkumar150103@gmail.com" 

user = "multipurposemail15@gmail.com"
msg['from'] = user
pwd = "pwww aile ckng ruji"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, password=pwd)
server.send_message(msg)
server.quit()