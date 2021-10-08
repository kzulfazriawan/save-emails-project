"""alter emails table

Revision ID: 4fd10a1c3131
Revises: 069689cf8b89
Create Date: 2021-10-09 02:24:04.659324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fd10a1c3131'
down_revision = '069689cf8b89'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('emails', sa.Column('created_at', sa.DateTime))
    op.add_column('emails', sa.Column('updated_at', sa.DateTime))


def downgrade():
    pass
