import imaplib
import email

class EmailReader():

    def login(self, username, password):
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        return mail
    
    def read_mail_body(self, username, password, subject_text, search_text, start_str, end_str):
        mail = self.login(username, password)
        mail.list()
        mail.select("inbox")
        typ, data = mail.search(None, '(SUBJECT "%s")' %subject_text)
        ids = data[0]
        id_list = ids.split()
        email_str = ""
        
        for i in range(0,len(id_list)):
        
            result, data = mail.fetch(id_list[i], "(UID BODY[TEXT])")
            raw_email = data[0][1]
            
            msg = email.message_from_string(raw_email)
            body = msg.get_payload()
            
            if search_text in body:
                start = body.index(start_str)
                end = body.index(end_str)
                email_str = body[(start):(end)]
                break
            
        mail.close()
        mail.logout()
        return email_str