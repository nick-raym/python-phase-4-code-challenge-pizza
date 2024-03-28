"""empty message

Revision ID: 0a8a6d30d6e2
Revises: f05a88048a1a
Create Date: 2024-03-27 21:15:44.331290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8a6d30d6e2'
down_revision = 'f05a88048a1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.drop_constraint('fk_pizzas_restaurant_id_restaurants', type_='foreignkey')
        batch_op.drop_column('restaurant_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('restaurant_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_pizzas_restaurant_id_restaurants', 'restaurants', ['restaurant_id'], ['id'])

    # ### end Alembic commands ###
