"""post table

Revision ID: d33a0800955f
Revises: d8bd80786f64
Create Date: 2024-03-28 09:11:52.082797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd33a0800955f'
down_revision = 'd8bd80786f64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', sa.String(length=140), nullable=True))
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=140), nullable=True))
        batch_op.drop_column('body')

    # ### end Alembic commands ###
