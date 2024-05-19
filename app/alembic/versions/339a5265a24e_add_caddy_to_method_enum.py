"""Add caddy to method enum

Revision ID: 339a5265a24e
Revises: df425bed2bc5
Create Date: 2020-12-20 07:15:49.986345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '339a5265a24e'
down_revision = 'df425bed2bc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TYPE methodenum ADD VALUE IF NOT EXISTS 'CADDY'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
