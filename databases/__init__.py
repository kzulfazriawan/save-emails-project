import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from metric.src.filesystem import auto

load_dotenv()
MODEL = declarative_base()


def session(connection=False):
    """
    ## session
    """
    url = f"{os.environ['DB_SERVER']}://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@" \
          f"{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"

    if not connection:
        session_ng = sessionmaker(bind=create_engine(url), expire_on_commit=False)
        return session_ng()
    else:
        return create_engine(url).begin()


class Models:
    def __init__(self):
        """
        ____ORM class is the ORM class wizard to gather and summon all the models registered and
        send it to the attribute class____
        """
        self.model = lambda: None
        for k, v in auto('databases', 'models', 'databases/models').items():
            setattr(self.model, v.__name__, v)
