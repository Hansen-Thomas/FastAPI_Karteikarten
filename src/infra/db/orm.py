from sqlalchemy.orm import registry, relationship

from domain.card.card import Card
from domain.tag.tag import Tag
from infra.db.tables.card_table import card_table
from infra.db.tables.tag_table import tag_table
from infra.db.tables.card_has_tag_table import card_has_tag_table


def start_mappers():
    mapping_registry = registry()
    mapping_registry.map_imperatively(
        Card,
        card_table,
        properties={
            "tags": relationship(
                Tag,
                secondary=card_has_tag_table,
                lazy="immediate",
                collection_class=set,
            )
        },
    )
    mapping_registry.map_imperatively(
        Tag,
        tag_table,
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
