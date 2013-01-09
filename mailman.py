import email
import wordutils
import smtpd
import asyncore


class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        msg = email.message_from_string(data)
        subject = msg.get('Subject')
        #payload = unicode(msg.get_payload(decode=True),'utf-8')
        payload = msg.get_payload(decode=True)
        #print payload
        wordutils.processWords(subject,payload)
        return

server = CustomSMTPServer(('0.0.0.0', 25), None)

print "starting mailman"

asyncore.loop()


