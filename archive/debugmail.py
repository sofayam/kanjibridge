import smtpd
import asyncore
from email.parser import Parser
import email

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        print 'Data >>>', data, '<<<' 
        headers = Parser().parsestr(data)
        print headers['Subject']
        print "-----------------------------------"
        print email.message_from_string(data).get_payload(decode=True)
        print unicode(email.message_from_string(data).get_payload(decode=True),'utf-8')
        return

server = CustomSMTPServer(('0.0.0.0', 25), None)

asyncore.loop()

