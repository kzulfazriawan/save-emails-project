"""create send_emails table

Revision ID: 5a1a4fd93e0f
Revises: 4fd10a1c3131
Create Date: 2021-10-09 04:19:05.298487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a1a4fd93e0f'
down_revision = '4fd10a1c3131'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'email_send',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('event_id', sa.Integer),
        sa.Column('subject', sa.String(191)),
        sa.Column('content', sa.Text),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade():
    op.drop_table('email_send')
