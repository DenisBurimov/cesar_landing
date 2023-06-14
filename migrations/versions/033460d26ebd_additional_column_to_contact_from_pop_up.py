"""additional column to Contact from pop up

Revision ID: 033460d26ebd
Revises: 383e623f150d
Create Date: 2023-06-13 16:11:53.794904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '033460d26ebd'
down_revision = '383e623f150d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('first_name', sa.String(length=64), nullable=True))
    op.add_column('contacts', sa.Column('last_name', sa.String(length=64), nullable=True))
    op.add_column('contacts', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('contacts', sa.Column('message', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contacts', 'message')
    op.drop_column('contacts', 'email')
    op.drop_column('contacts', 'last_name')
    op.drop_column('contacts', 'first_name')
    # ### end Alembic commands ###
