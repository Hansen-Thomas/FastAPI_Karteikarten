from sqlalchemy.orm import Session

from domain.card.card import Card
from domain.card.card_repository_db import DbCardRepository


def test_db_card_repo_can_save_and_return_cards(
    unit_test_db_session: Session,
):
    # Arrange:
    card_repo = DbCardRepository(unit_test_db_session)
    card = Card()
    card.id = 1
    card.german = "die Antwort"
    card.italian = "la risposta"

    # Act:
    card_repo.add(card)
    unit_test_db_session.commit()
    
    # Assert:
    # assert unit_test_db_session.committed
    assert card_repo.all() == [card]
    assert card_repo.get(card.id) == card