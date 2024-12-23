from sqlalchemy.orm import Session

from domain.card.card import Card
from domain.card.card_repository_db import DbCardRepository


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
    assert card_repo.get_by_german(card.german) == card


def test_db_card_repo_can_delete_existing_cards(
    session_for_filled_unit_test_db: Session,
):
    # Arrange:
    card_repo = DbCardRepository(session_for_filled_unit_test_db)
    cards = card_repo.all()
    first_card = cards[0]
    second_card = cards[1]
    third_card = cards[2]

    # Act:
    card_repo.delete(second_card)
    session_for_filled_unit_test_db.commit()

    # Assert:
    assert first_card in card_repo.all()
    assert second_card not in card_repo.all()
    assert third_card in card_repo.all()


def test_db_card_repo_cannot_delete_not_existing_cards(
    session_for_filled_unit_test_db: Session,
):
    # Arrange:
    card_repo = DbCardRepository(session_for_filled_unit_test_db)
    cards = card_repo.all()
    assert len(cards) == 5
    second_card = cards[1]
    third_card = cards[2]

    # Act (delete existing card):
    card_repo.delete(second_card)
    assert len(card_repo.all()) == 4
    assert second_card not in card_repo.all()

    # Act (delete not existing card):
    card_repo.delete(second_card)
    assert len(card_repo.all()) == 4
    assert second_card not in card_repo.all()

    # Act (delete existing card):
    card_repo.delete(third_card)
    assert len(card_repo.all()) == 3

    # Act:
    session_for_filled_unit_test_db.commit()
    cards_after_commit = card_repo.all()
    assert len(cards_after_commit) == 3
