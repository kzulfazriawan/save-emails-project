import os
from abc import ABC
from inspect import isclass

from dotenv import load_dotenv
from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from metric.src.filesystem import auto

ROOTPATH = os.path.dirname(os.path.abspath(__name__))
APPPATH = os.path.join(ROOTPATH, 'app')

FLASK = Flask(__name__)
JWT = JWTManager(FLASK)

load_dotenv()


class App:
    app = FLASK

    def __init__(self):
        self.app.config['SECRET_KEY'] = 'HELLOWORLD123'
        self.app.config['SCHEDULER_API_ENABLED'] = True
        self.app.config['MAIL_SERVER'] = os.getenv('EMAIL_SMTP')
        self.app.config['MAIL_PORT'] = os.getenv('EMAIL_PORT')
        self.app.config['MAIL_USE_TLS'] = True if os.getenv('EMAIL_TLS') == 'True' else False
        self.app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
        self.app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
        self.app.config['MAIL_USE_SSL'] = True if os.getenv('EMAIL_SSL') == 'True' else False

        self.mail = Mail(self.app)
        CORS(self.app)

    def daemon(self):
        scheduler = APScheduler()
        scheduler.init_app(self.app)

        return scheduler


class Route(App):
    def __init__(self):
        super(Route, self).__init__()

    def route(self, resource, **kwargs):
        if all(k in kwargs for k in ['url', 'method', 'endpoint']):
            url, method, endpoint = kwargs['url'], kwargs['method'], kwargs['endpoint']

            if not isinstance(method, list):
                method = [method]

            return self.app.route(url, methods=method, endpoint=endpoint)(resource)

    def resource(self, _class, prefix='/'):
        if isclass(_class):
            lists = ['get', 'post', 'put', 'delete']
            resources = [i for i in dir(_class) if i in lists]

            for i in resources:
                endpoint = ''.join([prefix, _class.__name__.lower()])
                _epname = '.'.join([_class.__name__.lower(), i])

                url = f"{endpoint}/<int:id>" if i in ['put', 'delete'] else endpoint
                self.route(getattr(_class(), i), method=i.upper(), url=url, endpoint=_epname)


class Init(ABC, Route):
    def __init__(self):
        super(Init, self).__init__()

    def resources(self):
        for k, v in auto('app', 'resources', 'app/resources').items():
            url = k.replace('app.resources', '').split('.')[:-1]
            url = os.path.join(*url) if len(url) > 1 else ''

            self.resource(v, f'/{url}')
