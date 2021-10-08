"""create emails table

Revision ID: 069689cf8b89
Revises: 
Create Date: 2021-10-09 02:06:42.987901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '069689cf8b89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'emails',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(191)),
        sa.Column('email', sa.String(191), unique=True)
    )


def downgrade():
    op.drop_table('emails')
