"""add_pdf_processing_fields

Revision ID: abe37b575791
Revises: 
Create Date: 2025-12-12 21:32:24.184791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abe37b575791'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Assuming the table name is 'papers'. Change it if your table is named 'paper'.
    op.add_column('papers', sa.Column('parsed_content', sa.JSON(), nullable=True))
    op.add_column('papers', sa.Column('processing_status', sa.String(), nullable=True))
    op.add_column('papers', sa.Column('error_message', sa.Text(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('papers', 'error_message')
    op.drop_column('papers', 'processing_status')
    op.drop_column('papers', 'parsed_content')
