"""Create table for storing the datetime resource

Revision ID: d1ae58c215b9
Revises: 3c403aee5d08
Create Date: 2020-02-04 22:34:52.848617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1ae58c215b9'
down_revision = '3c403aee5d08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datetime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DATETIME(), nullable=False),
    sa.Column('comment', sa.VARCHAR(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('datetime')
    # ### end Alembic commands ###
