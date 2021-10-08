from flask_mail import Message

from databases import Models


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
            if self.sending_email(item.subject, item.content):
                print(data.edit)
            else:
                print('email not sent')

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
                body=content
            )
            self.mail.send(msg)
            return True

        except Exception as e:
            print(e)
            return False
