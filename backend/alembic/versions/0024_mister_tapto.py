"""add columns for mister tapto integration

Revision ID: 0024_mister_tapto
Revises: 0023_make_columns_non_nullable
Create Date: 2024-07-18 20:19:00.000000

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "0024_mister_tapto"
down_revision = "0023_make_columns_non_nullable"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("roms", schema=None) as batch_op:
        batch_op.add_column(sa.Column("mister_path", sa.String(1000), default=""))

    with op.batch_alter_table("roms", schema=None) as batch_op:
        batch_op.execute("update roms set mister_path = ''")


def downgrade() -> None:
    with op.batch_alter_table("roms", schema=None) as batch_op:
        batch_op.drop_column("mister_path")
