from sqlalchemy import Table, Column, Integer, String, ForeignKey

from infra.db import metadata


card_has_tag_table = Table(
    "Card_has_Tag",
    metadata,
    Column("id_card", Integer, ForeignKey("Card.id"), primary_key=True),
    Column("tag", String, ForeignKey("Tag.value"), primary_key=True),
)
