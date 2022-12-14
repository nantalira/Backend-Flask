"""Ubah Foreign Key Type

Revision ID: 23a86bf1db5a
Revises: 604dc1476cf7
Create Date: 2022-09-19 10:49:24.296217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23a86bf1db5a'
down_revision = '604dc1476cf7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('mahasiswa_ibfk_2', 'mahasiswa', type_='foreignkey')
    op.drop_constraint('mahasiswa_ibfk_1', 'mahasiswa', type_='foreignkey')
    op.create_foreign_key(None, 'mahasiswa', 'dosen', ['dosen_satu'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'mahasiswa', 'dosen', ['dosen_dua'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mahasiswa', type_='foreignkey')
    op.drop_constraint(None, 'mahasiswa', type_='foreignkey')
    op.create_foreign_key('mahasiswa_ibfk_1', 'mahasiswa', 'dosen', ['dosen_dua'], ['id'])
    op.create_foreign_key('mahasiswa_ibfk_2', 'mahasiswa', 'dosen', ['dosen_satu'], ['id'])
    # ### end Alembic commands ###
