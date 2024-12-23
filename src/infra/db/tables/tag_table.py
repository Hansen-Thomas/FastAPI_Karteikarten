from sqlalchemy import Table, Column, String

from infra.db import metadata


tag_table = Table(
    "Tag",
    metadata,
    Column("value", String, primary_key=True),
)
