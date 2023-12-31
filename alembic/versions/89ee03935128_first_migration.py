"""First migration

Revision ID: 89ee03935128
Revises: 
Create Date: 2023-06-12 18:45:17.401143

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '89ee03935128'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('timestamp', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_currency'))
    )
    with op.batch_alter_table('currency', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_currency_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('currency', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_currency_id'))

    op.drop_table('currency')
    # ### end Alembic commands ###
