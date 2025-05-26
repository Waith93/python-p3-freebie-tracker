"""create db

Revision ID: 7a71dbf71c64
Revises: 
Create Date: 2023-03-15 15:05:55.516631
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a71dbf71c64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create 'devs' table
    op.create_table(
        'devs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False)
    )

    # Create 'companies' table
    op.create_table(
        'companies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('founding_year', sa.Integer(), nullable=False)
    )

    # Create 'freebies' table
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'))
    )


def downgrade() -> None:
    op.drop_table('freebies')
    op.drop_table('companies')
    op.drop_table('devs')

