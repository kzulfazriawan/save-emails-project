from app.resources import Resource
from databases import Models
from databases.errors import NoneTypeValue


class Emails(Resource, Models):
    def __init__(self):
        super(Emails, self).__init__()

    def get(self):
        try:
            data = self.model.Emails()
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
            name='required',
            email="required"
        )

        if 'errors' in validation:
            return validation

        request = self.requests.parser

        return self.response.json(
            self.model.Emails().add(
                name=request.json['name'],
                email=request.json['email']
            )
        )
