from pytest import fixture
from sqlalchemy.orm import Session

from domain.card.card import Card
from domain.card.card_repository_abstract import AbstractCardRepository
from domain.card.word_type import WordType
from test.utils.fake_session import FakeSession
from test.utils.fake_card_repo import FakeCardRepository


@fixture
def fake_session() -> Session:
    return FakeSession()


@fixture
def fake_card_repo(fake_session: Session) -> AbstractCardRepository:
    return FakeCardRepository(fake_session)


@fixture
def card1() -> Card:
    card = Card()
    card.word_type = WordType.NOUN
    card.german = "die Antwort"
    card.italian = "la risposta"
    return card


@fixture
def card2() -> Card:
    card = Card()
    card.word_type = WordType.NOUN
    card.german = "die Frage"
    card.italian = "la domanda"
    return card


@fixture
def card3() -> Card:
    card = Card()
    card.word_type = WordType.NOUN
    card.german = "die Katze"
    card.italian = "il gatto"
    return card


@fixture
def card4() -> Card:
    card = Card()
    card.word_type = WordType.VERB
    card.german = "gehen"
    card.italian = "andare"
    return card


@fixture
def card5() -> Card:
    card = Card()
    card.word_type = WordType.VERB
    card.german = "haben"
    card.italian = "avere"
    return card


@fixture
def filled_fake_card_repo(
    fake_card_repo: AbstractCardRepository,
    card1: Card,
    card2: Card,
    card3: Card,
    card4: Card,
    card5: Card,
) -> AbstractCardRepository:
    fake_card_repo.add(card1)
    fake_card_repo.add(card2)
    fake_card_repo.add(card3)
    fake_card_repo.add(card4)
    fake_card_repo.add(card5)
    return fake_card_repo
