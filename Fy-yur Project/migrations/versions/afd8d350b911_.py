"""empty message

Revision ID: afd8d350b911
Revises: 
Create Date: 2020-06-07 15:02:19.841414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afd8d350b911'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venuetable',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('phn_num', sa.String(), nullable=False),
    sa.Column('genres', sa.String(), nullable=False),
    sa.Column('fblink', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venuetable')
    # ### end Alembic commands ###
