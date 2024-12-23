from sqlalchemy.orm import Session

from domain.card.card import Card
from test.utils.fake_card_repo import FakeCardRepository


def test_fake_card_repo_can_save_and_return_cards(fake_session: Session):
    # Arrange:
    card_repo = FakeCardRepository(fake_session)
    card = Card()
    card.german = "die Antwort"
    card.italian = "la risposta"

    # Act:
    card_repo.add(card)
    fake_session.commit()

    # Assert:
    assert fake_session.committed
    assert card_repo.all() == [card]
    assert card_repo.get(card.id) == card


def test_fake_card_repo_can_delete_existing_cards(fake_session: Session):
    # Arrange:
    card_repo = FakeCardRepository(fake_session)
    card = Card()
    card.german = "die Antwort"
    card.italian = "la risposta"

    # Act:
    card_repo.add(card)
    card_repo.delete(card)
    fake_session.commit()

    # Assert:
    assert card_repo.all() == []
    assert card_repo.get(card.id) is None
    assert fake_session.committed


def test_fake_card_repo_can_not_delete_not_existing_card(fake_session: Session):
    # Arrange:
    card_repo = FakeCardRepository(fake_session)
    card = Card()
    card.german = "die Antwort"
    card.italian = "la risposta"

    # Act:
    card_repo.delete(card)  # repo is empty, so nothing should happen
    fake_session.commit()

    # Assert:
    assert card_repo.all() == []
    assert card_repo.get(card.id) is None
    assert fake_session.committed
