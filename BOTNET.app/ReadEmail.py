#!/usr/bin/python
import email, imaplib

user = 'th3ta403@gmail.com'
pwd = 'Theta403'

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user, pwd)

m.select("INBOX")

try:
	resp, data = m.fetch(1, "(RFC822)")
	
	email_body = data[0][1]
	
	mail = email.message_from_string(email_body)
	
	lines = mail.get_payload()[0].get_payload().split("\n")
	
	open ("/Users/171510/Desktop/BOTNET.app/InfoFile.txt", "w").close ()
	info_file = open ("/Users/171510/Desktop/BOTNET.app/InfoFile.txt", "a")
	with open ("/Users/171510/Desktop/BOTNET.app/InfoFile.txt") as f:
		if lines[0] not in f.read ():
			info_file.write (mail.get_payload()[ 0 ].get_payload() + "\n\n")
	info_file.close ()
	
	box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
	box.login(user, pwd)
	box.select('Inbox')
	typ, data = box.search(None, 'ALL')
	for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
	box.expunge()
	box.close()
	box.logout()
except:
	m.logout ()