"""empty message

Revision ID: 2546decca142
Revises: 86f9c9883e55
Create Date: 2021-03-18 18:39:15.703935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2546decca142'
down_revision = '86f9c9883e55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###
