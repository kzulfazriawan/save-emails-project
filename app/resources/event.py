from app.resources import Resource
from databases import Models
from databases.errors import NoneTypeValue


class Event(Resource, Models):
    def __init__(self):
        super(Event, self).__init__()

    def get(self):
        try:
            data = self.model.Event()
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
            description="required"
        )

        if 'errors' in validation:
            return self.response.json(
                validation,
                422
            )

        request = self.requests.parser

        return self.response.json(
            self.model.Event().add(
                name=request.json['name'],
                description=request.json['description']
            )
        )
