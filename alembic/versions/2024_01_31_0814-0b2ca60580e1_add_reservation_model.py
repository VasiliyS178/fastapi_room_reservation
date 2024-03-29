"""Add Reservation model

Revision ID: 0b2ca60580e1
Revises: 5bd107b97d50
Create Date: 2024-01-31 08:14:12.751796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2ca60580e1'
down_revision = '5bd107b97d50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_reserve', sa.DateTime(), nullable=True),
    sa.Column('to_reserve', sa.DateTime(), nullable=True),
    sa.Column('meetingroom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meetingroom_id'], ['meetingroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###
