from sqlalchemy import Table, Column, Integer, String, Enum

from domain.card.word_type import WordType
from infra.db import metadata


card_table = Table(
    "Card",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("word_type", Enum(WordType)),
    Column("german", String),
    Column("italian", String),
)
