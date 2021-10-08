from databases import MODEL
from databases.queries import Query
from databases.datatypes import *


class Email_send(MODEL, Query):
    __tablename__ = 'email_send'

    # ___column data form models___
    id = primary_key_id()
    event_id = foreign_key_id(None, 'event.id')
    subject = character()
    content = character(unique=True)
    timestamp = date_time()
    is_send = boolean()
    created_at = created_at()
    updated_at = updated_at()

    @staticmethod
    def hidden():
        return []
