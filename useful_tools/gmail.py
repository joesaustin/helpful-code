from email.mime.text import MIMEText
import smtplib

#useful if you would like your script to send out an email.
class GoogleMail:
    
    def send_mail(self, address, subject, body):
        '''The SMTP server details'''
        smtp_server = "smtp.gmail.com:587"
        smtp_username = "email_address"
        smtp_password = "password"
        
        '''The email details'''
        from_address = "email_address"
        to_address = address
        #cc_addresses = ["copy1", "copy2"]
        msg_subject = subject
        msg_body = body
        msg = MIMEText(msg_body)
        
        '''Create Headers'''
        msg['Subject'] = msg_subject
        msg['From'] = from_address
        msg['To'] = to_address
        #msg['Cc'] = ','.join(cc_addresses) 
        
        ''' send the email'''
        s = smtplib.SMTP(smtp_server) 
        try:
            s.ehlo() 
            if s.has_extn('STARTTLS'):
                s.starttls()
                s.ehlo()
            s.login(smtp_username, smtp_password) 
            s.sendmail(from_address, to_address, msg.as_string())
        finally:
            s.quit()