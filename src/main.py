from domain.card.card import Card
from domain.card.card_repository_db import DbCardRepository
from domain.card.word_type import WordType
from domain.tag.tag import Tag
from domain.tag.tag_repository_db import DbTagRepository

import infra.db as db
import infra.db.orm as orm

orm.start_mappers()

session = next(db.get_session())
card = Card()
card.word_type = WordType.NOUN
card.german = "Haus"
card.italian = "casa"

card.add_tag("test2")
card.add_tag("test3")

card_repo = DbCardRepository(session)
card_repo.add(card)

session.commit()

print("hello world")
