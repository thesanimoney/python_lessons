from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template
from pathlib import Path

template = Template(Path('template.html').read_text())
body = template.substitute({'name': 'John'})

message = MIMEMultipart()
message['from'] = 'Oleksandr Stoliarchuk'
message['to'] = 'thesanimoneybiz@gmail.com'
message['subject'] = 'This is a test'
message.attach(MIMEText(body, 'html'))


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
       smtp.ehlo()
       smtp.starttls()
       smtp.login('thesanimoney@gmail.com', 'kcfq xtpg ylra kvfg')
       smtp.send_message(message)
       print("sent..")