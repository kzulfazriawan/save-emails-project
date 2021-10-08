import os
import datetime
from dotenv import load_dotenv
from flask_mail import Message

from databases import Models


load_dotenv()


class CheckEmail(Models):
    def __init__(self, mail):
        super(CheckEmail, self).__init__()

        self.mail = mail
        self.email_send = self.model.Email_send()
        self.email = self.model.Emails()

    def check_email_not_send(self):
        data = self.email_send.select().filter(
            'is_send', False
        )
        for item in data.all(object()):
            if item.timestamp < datetime.datetime.now():
                if self.sending_email(item.subject, item.content):
                    self.update_email(item.id)
                    print('sent')
            else:
                print('wait')

    def update_email(self, id):
        data = self.email_send.select().filter(
            'id', id
        )
        return data.edit(is_send=True)

    def sending_email(self, subject, content):
        try:
            recipients = self.email.select()

            msg = Message(
                subject,
                recipients=[item.email for item in recipients.all(object())],
                sender=("Me", os.getenv('EMAIL_USERNAME')),
                body=content
            )
            self.mail.send(msg)
            return True

        except Exception as e:
            print(e)
            return False
