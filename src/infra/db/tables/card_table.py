from sqlalchemy import Table, Column, Boolean, Integer, String, Enum, DateTime

from domain.card.word_type import WordType
from infra.db import metadata


card_table = Table(
    "Card",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("word_type", Enum(WordType)),
    Column("german", String),
    Column("italian", String),
    Column("times_played", Integer),
    Column("correct_answers", Integer),
    Column("last_answer_correct", Boolean),
    Column("last_played", DateTime),
)
