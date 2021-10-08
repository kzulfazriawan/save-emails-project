"""alter send_emails table

Revision ID: cf032297f017
Revises: 9d52e45d80a3
Create Date: 2021-10-09 04:29:16.764878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf032297f017'
down_revision = '9d52e45d80a3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('email_send', sa.Column('timestamp', sa.DateTime))


def downgrade():
    pass
