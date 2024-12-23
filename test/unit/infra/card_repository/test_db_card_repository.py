from sqlalchemy.orm import Session

from domain.card.card import Card
from domain.card.card_repository_db import DbCardRepository
import test.utils.test_cards as test_cards


def test_db_card_repo_can_save_and_return_cards(
    session_for_empty_unit_test_db: Session,
):
    # Arrange:
    card_repo = DbCardRepository(session_for_empty_unit_test_db)
    card = Card()
    card.id = 1
    card.german = "die Antwort"
    card.italian = "la risposta"

    # Act:
    card_repo.add(card)
    session_for_empty_unit_test_db.commit()
    
    # Assert:
    assert card_repo.all() == [card]
    assert card_repo.get(card.id) == card


def test_db_card_repo_can_delete_existing_cards(
    session_for_filled_unit_test_db: Session,
):
    # Arrange:
    card_repo = DbCardRepository(session_for_filled_unit_test_db)
    card1 = test_cards.get_card1()
    card2 = test_cards.get_card2()
    card3 = test_cards.get_card3()
    assert card1 in card_repo.all()
    assert card2 in card_repo.all()
    assert card3 in card_repo.all()
    
    