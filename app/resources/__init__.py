from abc import ABC

from flask import jsonify as _json
from flask import redirect as _rdr
from flask import request as _req
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email


class Resource(ABC):
    def __init__(self):
        super(Resource, self).__init__()

        self.requests = Requests(self.__class__.__name__)
        self.response = Response()


class Requests:
    def __init__(self, class_name):
        """
        ## Requests

        [ID]
            Class ini berguna untuk melakukan parsing dan validasi terhadap requests yang masuk.
        [EN]
            This class is used to parsed and validation for incoming requests.
        """
        self.class_name = class_name.lower()
        self.parse = lambda: None

    @property
    def parser(self):
        """

        @return:
        """
        req = lambda: None
        try:
            if _req.json is not None:
                req.json = _req.json

            if bool(_req.form):
                req.form = _req.form.to_dict(flat=False)

                if bool(_req.files):
                    req.file = _req.files.to_dict(flat=False)

            if bool(_req.args):
                req.args = _req.args
        except AttributeError:
            pass
        else:
            return req

    def validation(self, csrf_enable=True, **kwargs):
        """
        ## validation

        :param csrf_enable:
        :param kwargs:
        :return:
        """
        try:
            dict_validation = {}

            for k, v in kwargs.items():
                validate = v.split(',')
                tmp_validators = []

                if 'required' in validate:
                    tmp_validators.append(DataRequired(f'field {k} is required'))
                if 'email' in validate:
                    tmp_validators.append(Email(f'field {k} is required and valid email type'))

                # defining field-type
                if 'numeric' in validate:
                    dict_validation[k] = IntegerField(k, validators=tmp_validators)
                else:
                    dict_validation[k] = StringField(k, validators=tmp_validators)

        except KeyError as err:
            raise RequestValidationException.with_traceback(err.__traceback__)

        else:
            forms = type(f'{self.class_name}_forms_validation', (FlaskForm,), dict_validation)
            forms = forms(meta={"csrf": False}) if not csrf_enable else forms()

            if not forms.validate():
                return {'errors': forms.errors, 'code': 422}
            else:
                return {'code': 200}


class Response:
    def __init__(self):
        """
        ## Response

        [ID]
            Class ini bertujuan untuk memberikan response kepada client, baik itu redirect, json atau HTML.
        [EN]
            This class is purposed to give response to the client which is redirect, json or HTML.
        """
        pass

    def json(self, data, status_code=200):
        return _json(data), status_code

    def redirect(self, target):
        return _rdr(target, 301)


class RequestValidationException(Exception):
    def __init__(self, exception, message="Invalid requests parse!"):
        self.message = message
        self.exception = exception
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.exception}'
