"""added breed column

Revision ID: f2f0a93be1d6
Revises: 
Create Date: 2019-01-11 14:15:31.206141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f0a93be1d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cats', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cats', 'breed')
    # ### end Alembic commands ###
