from databases import MODEL
from databases.queries import Query
from databases.datatypes import *


class Emails(MODEL, Query):
    __tablename__ = 'emails'

    # ___column data form models___
    id = primary_key_id()
    name = character()
    email = character(unique=True)
    created_at = created_at()
    updated_at = updated_at()

    @staticmethod
    def hidden():
        return []
