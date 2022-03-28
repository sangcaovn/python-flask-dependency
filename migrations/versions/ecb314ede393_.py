"""empty message

Revision ID: ecb314ede393
Revises: d13ca8ab0386
Create Date: 2022-03-28 11:11:40.758487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecb314ede393'
down_revision = 'd13ca8ab0386'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_description'), 'product', ['description'], unique=True)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_description'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###