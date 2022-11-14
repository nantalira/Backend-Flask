"""Tambah kolom level

Revision ID: 1ddccdaf469c
Revises: 9b8b28498c1d
Create Date: 2022-09-22 15:12:23.539113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ddccdaf469c'
down_revision = '9b8b28498c1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('level', sa.BigInteger(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'level')
    # ### end Alembic commands ###
