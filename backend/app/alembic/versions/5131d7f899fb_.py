"""empty message

Revision ID: 5131d7f899fb
Revises: 
Create Date: 2022-03-15 17:36:29.352457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5131d7f899fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bid_profile',
    sa.Column('bid_profile_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('note', sa.String(length=255), nullable=True),
    sa.Column('target_acos', sa.Float(), nullable=False),
    sa.Column('min_target_acos_boundary', sa.Float(), nullable=False),
    sa.Column('max_target_acos_boundary', sa.Float(), nullable=False),
    sa.Column('max_acos', sa.Float(), nullable=False),
    sa.Column('min_clicks', sa.Integer(), nullable=False),
    sa.Column('min_impressions', sa.Integer(), nullable=False),
    sa.Column('floor_bid', sa.Float(), nullable=False),
    sa.Column('ceiling_bid', sa.Float(), nullable=False),
    sa.Column('increment_up_rate', sa.Float(), nullable=False),
    sa.Column('increment_down_rate', sa.Float(), nullable=False),
    sa.Column('max_increment_up', sa.Float(), nullable=True),
    sa.Column('max_increment_down', sa.Float(), nullable=True),
    sa.Column('created_datetime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('bid_profile_id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_bid_profile_bid_profile_id'), 'bid_profile', ['bid_profile_id'], unique=False)
    op.create_table('bid_asin',
    sa.Column('asin_id', sa.Integer(), nullable=False),
    sa.Column('asin', sa.String(length=10), nullable=False),
    sa.Column('sku', sa.String(length=25), nullable=False),
    sa.Column('sales_channel_id', sa.Integer(), nullable=False),
    sa.Column('market', sa.String(length=10), nullable=False),
    sa.Column('list_price', sa.Float(), nullable=True),
    sa.Column('procurement_status', sa.String(length=50), nullable=True),
    sa.Column('bid_profile_id', sa.Integer(), nullable=True),
    sa.Column('created_datetime', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['bid_profile_id'], ['bid_profile.bid_profile_id'], ),
    sa.PrimaryKeyConstraint('asin_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bid_asin')
    op.drop_index(op.f('ix_bid_profile_bid_profile_id'), table_name='bid_profile')
    op.drop_table('bid_profile')
    # ### end Alembic commands ###
