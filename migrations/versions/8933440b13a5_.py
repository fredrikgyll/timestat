"""empty message

Revision ID: 8933440b13a5
Revises: 
Create Date: 2019-06-28 21:06:36.671071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8933440b13a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hour',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.Time(), nullable=False),
    sa.Column('end', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('short_name', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('short_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('shift',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.Enum('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', name='workdays'), nullable=True),
    sa.Column('hour', sa.Integer(), nullable=False),
    sa.Column('location', sa.Integer(), nullable=False),
    sa.Column('number_of_workers', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hour'], ['hour.id'], ),
    sa.ForeignKeyConstraint(['location'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shift_worker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shift', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('preference', sa.Enum('REFUSE', 'NEUTRAL', 'PREFER', name='shiftpreference'), nullable=True),
    sa.ForeignKeyConstraint(['shift'], ['shift.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shift_worker')
    op.drop_table('shift')
    op.drop_table('user')
    op.drop_table('location')
    op.drop_table('hour')
    # ### end Alembic commands ###
