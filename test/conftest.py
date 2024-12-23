from pytest import fixture
from sqlalchemy.orm import Session

from domain.card.card_repository_abstract import AbstractCardRepository
from test.utils.fake_session import FakeSession
from test.utils.fake_card_repo import FakeCardRepository
from test.utils.test_cards import get_test_cards


@fixture
def fake_session() -> Session:
    return FakeSession()


@fixture
def filled_fake_card_repo(
    fake_session: Session,
) -> AbstractCardRepository:
    repo = FakeCardRepository(fake_session)
    test_cards = get_test_cards()
    for card in test_cards:
        repo.add(card)
    return repo
