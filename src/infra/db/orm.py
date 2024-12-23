from sqlalchemy.orm import registry, relationship

from domain.card.card import Card
from infra.db.tables.card_table import card_table


def start_mappers():
    mapping_registry = registry()
    mapping_registry.map_imperatively(
        Card,
        card_table,
        properties={},
    )
    # mapping_registry.map_imperatively(
    #     User,
    #     user_table,
    #     properties={
    #         "roles": relationship(
    #             Role, secondary=user_has_role_table, lazy="immediate"
    #         )
    #     },
    # )
