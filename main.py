from app import Init
from app.jobs import *


class App(Init):
    def __init__(self):
        super(App, self).__init__()
        self.resources()

    def scheduler(self):
        daemon = self.daemon()
        mail = self.mail
        app_context = self.app.app_context()

        # cron examples
        @daemon.task('cron', id='do_job_2', minute='*')
        def job2():
            with app_context:
                check_mail = CheckEmail(mail)
                check_mail.check_email_not_send()

        return daemon

    def run(self):
        self.app.run(
            debug=True
        )


if __name__ == "__main__":
    app = App()
    app.scheduler().start()
    app.run()
