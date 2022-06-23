"""empty message

Revision ID: 6dd268deba90
Revises: 
Create Date: 2022-06-09 20:15:38.023950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dd268deba90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
