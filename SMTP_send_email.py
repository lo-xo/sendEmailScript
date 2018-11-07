#!/usr/bin/env python
 
import sys, smtplib, socket
from email.MIMEText import MIMEText

 
SMTP_SERVER = '23.235.24.36' # Dia chi smtp server
SMTP_PORT = 465  # Port smtp server
 
username='abc@gmail.com' # User login smtp server
password='hczghxjEFXAx' # Nhap password login smtp server 

fromaddr = username
toaddrs = 'darkvn@gmail.com'

 
def sendAnEmail(subject, content):
    	msg = MIMEText(content)
    	msg['Subject'] = subject
    	msg['From'] = fromaddr
    	msg['To'] =toaddrs
	
	try:
		s=smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
		s.set_debuglevel(1)
		s.ehlo()
		try:
			s.login(username,password)
		except smtplib.SMTPException, e:
			print "Authentication failed:", e
			sys.exit(1)
		s.sendmail(fromaddr, toaddrs, msg.as_string())
	except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
		print    " *** your message may not have been sent! "
		print e
		sys.exit(2)
	else:
		print "Message successfully sent to %d recipient(s) " %len(toaddrs)
		s.close()
if __name__ == '__main__':
	if len(sys.argv) != 4:	
		print "Parameter invalid"
	else:
    toaddrs=sys.argv[1]
		subject=sys.argv[2]
		content=sys.argv[3]
		sendAnEmail(subject, content)
