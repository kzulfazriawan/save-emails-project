"""alter send_emails_status table

Revision ID: 10ad54f6a729
Revises: cf032297f017
Create Date: 2021-10-09 04:35:53.540347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10ad54f6a729'
down_revision = 'cf032297f017'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('email_send', sa.Column('is_send', sa.Boolean))


def downgrade():
    pass
