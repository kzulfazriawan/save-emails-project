"""alter send_emails_foreign_key table

Revision ID: e194d44f3d08
Revises: 10ad54f6a729
Create Date: 2021-10-08 21:42:47.511100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e194d44f3d08'
down_revision = '10ad54f6a729'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key('fk_email_send_event_id_event', 'email_send', 'event', ['event_id'], ['id'])


def downgrade():
    op.drop_constraint('fk_email_send_event_id_event', 'email_send', type_='foreignkey')
