from sqlalchemy.orm import Session

from domain.card.card import Card
from domain.card.card_repository_db import DbCardRepository
from domain.card.word_type import WordType
from domain.tag.tag import Tag
from domain.tag.tag_repository_db import DbTagRepository


def test_db_card_repo_can_add_card(
    session_for_empty_unit_test_db: Session,
):
    # Arrange:
    card_repo = DbCardRepository(session_for_empty_unit_test_db)
    card = Card()
    card.id = 1
    card.word_type = WordType.NOUN
    card.german = "die Antwort"
    card.italian = "la risposta"

    # Act:
    card_repo.add(card)
    session_for_empty_unit_test_db.commit()

    # Assert:
    assert card_repo.all() == [card]
    assert card_repo.get_by_german(card.german) == card


def test_db_card_repo_can_add_card_with_tags(
    session_for_empty_unit_test_db: Session,
):
    # Arrange:
    card_repo = DbCardRepository(session_for_empty_unit_test_db)
    card = Card()
    card.id = 1
    card.word_type = WordType.NOUN
    card.german = "die Katze"
    card.italian = "il gatto"

    card.add_tag("Tiere")
    card.add_tag("Natur")

    # Act:
    card_repo.add(card)
    session_for_empty_unit_test_db.commit()

    # Assert:
    tag_repo = DbTagRepository(session_for_empty_unit_test_db)
    tags = tag_repo.all()
    assert len(tags) == 2
    cards = card_repo.all()
    assert len(cards) == 1
    assert cards[0] == card
    assert tags[0] in cards[0].tags



def test_db_card_repo_can_get_all_cards(session_for_filled_unit_test_db: Session):
    # Arrange:
    card_repo = DbCardRepository(session_for_filled_unit_test_db)

    # Act:
    cards = card_repo.all()

    # Assert:
    assert len(cards) == 5


def test_db_card_repo_can_update_card(
    session_for_filled_unit_test_db: Session,
):
    # Arrange:
    card_repo = DbCardRepository(session_for_filled_unit_test_db)
    cards = card_repo.all()
    first_card = cards[0]
    old_german_value = first_card.german
    old_italian_value = first_card.italian
    new_german_value = old_german_value + " (updated)"
    new_italian_value = old_italian_value + " (updated)"

    # Act:
    first_card.german = new_german_value
    first_card.italian = new_italian_value
    session_for_filled_unit_test_db.commit()

    # Assert:
    first_card_after_commit = card_repo.get_by_german(new_german_value)
    assert first_card_after_commit.german == new_german_value
    assert first_card_after_commit.italian == new_italian_value


def test_db_card_repo_can_delete_existing_card(
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


def test_db_card_repo_cannot_delete_not_existing_card(
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
    session_for_filled_unit_test_db.commit()
    assert len(card_repo.all()) == 4
    assert second_card not in card_repo.all()

    # Act (delete not existing card):
    card_repo.delete(second_card)
    session_for_filled_unit_test_db.commit()
    assert len(card_repo.all()) == 4
    assert second_card not in card_repo.all()

    # Act (delete existing card):
    card_repo.delete(third_card)
    session_for_filled_unit_test_db.commit()
    assert len(card_repo.all()) == 3
