"""empty message

Revision ID: f375453ca1f6
Revises: 81ac738516a0
Create Date: 2018-07-29 18:36:39.972623

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f375453ca1f6'
down_revision = '81ac738516a0'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_chat_message',
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('timezone', sa.String(), nullable=False),
    sa.Column('sent_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_chat_message')
    # ### end Alembic commands ###