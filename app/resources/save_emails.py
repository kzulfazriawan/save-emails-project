from app.resources import Resource
from databases import Models
from databases.errors import NoneTypeValue


class Save_emails(Resource, Models):
    def __init__(self):
        super(Save_emails, self).__init__()

    def get(self):
        try:
            data = self.model.Email_send()
            data = data.select()

            return self.response.json(
                data.all()
            )
        except NoneTypeValue:
            return self.response.json(
                {"error": "not_found"},
                404
            )

    def post(self):
        validation = self.requests.validation(
            False,
            event_id='required',
            email_subject="required",
            email_content="required",
            timestamp="required"
        )

        if 'errors' in validation:
            return self.response.json(
                validation,
                422
            )

        request = self.requests.parser

        return self.response.json(
            self.model.Email_send().add(
                event_id=request.json['event_id'],
                subject=request.json['email_subject'],
                content=request.json['email_content'],
                timestamp=request.json['timestamp'],
                is_send=False
            )
        )
