"""added weekly digests column to alert table

Revision ID: 50b793ad398a
Revises: 0382ff889e8d
Create Date: 2022-01-21 11:40:42.721718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50b793ad398a'
down_revision = '0382ff889e8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alert', sa.Column('weekly_digest', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alert', 'weekly_digest')
    # ### end Alembic commands ###
