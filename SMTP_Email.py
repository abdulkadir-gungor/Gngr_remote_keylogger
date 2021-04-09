############################################################################
#
#   SMTP Email Class
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Add_PNG:
    ''' Add png file to e-mail '''

    #
    def __init__(self, name):
        self.name = name
        self.type = 'image'
        self.subtype = 'png'
        self.binary = b''

    #
    def set_byte(self,bytes):
        self.binary = bytes
        return self


#
class SMTP_Email:
    ''' Sending e-mail using the smtp protocol '''

    # __init__(self, smtp, smtp_port, sender, password):
    # 1) smtp = 'smtp.gmail.com'
    # 2) smtp_port = 587
    # 3) sender = 'sender.gungor@gmail.com'
    # 4) password = 'abc123DEF456'
    def __init__(self, smtp:str, smtp_port:int, sender:str, password:str):
        ''' SMTP_Email Class Start '''

        self.session = smtplib.SMTP(smtp, smtp_port)
        self.sender_address = sender
        self.sender_pass = password
        self.receiver_address = ''
        self.message =  MIMEMultipart()

    # message_body(self,mail_to,mail_subject,mail_message):
    # 1) mail_to = 'receiver.example@gmail.com'
    # 2) mail_subject = 'A test mail'
    # 3) mail_content = ' Hi, a test mail,  etc ...'
    def message_body(self,mail_to:str,mail_subject:str,mail_content:str):
        ''' Email Body '''

        self.receiver_address = mail_to
        #
        self.message['From'] = self.sender_address
        self.message['To'] = mail_to
        self.message['Subject'] = mail_subject
        self.message.attach( MIMEText(mail_content, 'plain') )
        return self

    # message_add_file(self, filename, filefullpath):
    # filename = "example.pdf"
    # filefullpath = "example.pdf" or "D:\python\examples\example.pdf"
    def message_add_file(self, file:Add_PNG):
        ''' Add Any Files to Email '''

        #
        payload = MIMEBase(file.type, _subtype=file.subtype, name=file.name)
        payload.set_payload( file.binary )
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=file.name)
        self.message.attach(payload)
        return self

    # message_send(self):
    def message_send(self):
        ''' Sends the email '''

        if self.receiver_address != '':
            self.session.starttls()
            self.session.login(self.sender_address, self.sender_pass)
            self.session.sendmail(self.sender_address,self.receiver_address,self.message.as_string())
            self.session.quit()
            self.message_clear()
            return self, True
        else:
            return self, False

    # message_clear(self):
    def message_clear(self):
        ''' Clears the content to send different e-mails '''

        self.receiver_address = ''
        self.message =  MIMEMultipart()
        return self
