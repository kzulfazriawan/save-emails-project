from databases import MODEL
from databases.queries import Query
from databases.datatypes import *


class Event(MODEL, Query):
    __tablename__ = 'event'

    # ___column data form models___
    id = primary_key_id()
    name = character()
    description = text()
    created_at = created_at()
    updated_at = updated_at()

    @staticmethod
    def hidden():
        return []
