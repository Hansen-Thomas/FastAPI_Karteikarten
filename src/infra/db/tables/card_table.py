from sqlalchemy import Table, Column, Integer, String

from infra.db import metadata


table_card = Table(
    "Card",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("german", String),
    Column("italian", String),
)