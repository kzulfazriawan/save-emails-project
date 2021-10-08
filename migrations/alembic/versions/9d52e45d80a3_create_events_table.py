"""create events table

Revision ID: 9d52e45d80a3
Revises: 5a1a4fd93e0f
Create Date: 2021-10-09 04:26:46.302554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d52e45d80a3'
down_revision = '5a1a4fd93e0f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'event',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(191)),
        sa.Column('description', sa.Text),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade():
    op.drop_table('event')
