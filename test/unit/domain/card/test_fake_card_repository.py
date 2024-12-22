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

    card_repo.delete(card.id)
    assert card_repo.all() == []
    assert card_repo.get(card.id) is None

    fake_session.commit()
    assert fake_session.committed
