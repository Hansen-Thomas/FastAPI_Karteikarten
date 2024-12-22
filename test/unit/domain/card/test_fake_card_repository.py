from sqlalchemy.orm import Session

from domain.card.card import Card
from test.utils.fake_card_repo import FakeCardRepository


def test_fake_card_repo_can_save_and_return_cards(fake_session: Session):
    card_repo = FakeCardRepository(fake_session)

    card = Card()
    card.german = "die Antwort"
    card.italian = "la risposta"

    card_repo.add(card)
    assert card_repo.all() == [card]
    assert card_repo.get(card.id) == card

    fake_session.commit()
    assert fake_session.committed


def test_fake_card_repo_can_delete_existing_cards(fake_session: Session):
    card_repo = FakeCardRepository(fake_session)

    card = Card()
    card.german = "die Antwort"
    card.italian = "la risposta"

    card_repo.add(card)
    card_repo.delete(card)
    assert card_repo.all() == []
    assert card_repo.get(card.id) is None

    fake_session.commit()
    assert fake_session.committed


def test_fake_card_repo_can_not_delete_not_existing_card(fake_session: Session):
    card_repo = FakeCardRepository(fake_session)

    card = Card()
    card.german = "die Antwort"
    card.italian = "la risposta"

    card_repo.delete(card)  # repo is empty, so nothing should happen
    assert card_repo.all() == []
    assert card_repo.get(card.id) is None

    fake_session.commit()
    assert fake_session.committed
