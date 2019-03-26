"""added fifa

Revision ID: 91aa76502da2
Revises: fe5bc24225e2
Create Date: 2019-03-13 12:41:04.842000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91aa76502da2'
down_revision = 'fe5bc24225e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fifa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('photo', sa.String(length=140), nullable=True),
    sa.Column('nationality', sa.String(length=140), nullable=True),
    sa.Column('flag', sa.String(length=140), nullable=True),
    sa.Column('overall', sa.Integer(), nullable=True),
    sa.Column('potential', sa.Integer(), nullable=True),
    sa.Column('club', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fifa')
    # ### end Alembic commands ###