from typing import override

from test.utils.fake_session import FakeSession
from domain.card.card import Card
from domain.card.card_repository_abstract import AbstractCardRepository


class FakeCardRepository(AbstractCardRepository):
    def __init__(self, session: FakeSession) -> None:
        self.session = session
        self.cards: set[Card] = set()

    @override
    def get_by_german(self, german: str) -> Card | None:
        for card in self.cards:
            if card.german == german:
                return card
        return None

    @override
    def get_by_italian(self, italian: str) -> Card | None:
        for card in self.cards:
            if card.italian == italian:
                return card
        return None

    @override
    def all(self) -> list[Card]:
        return list(self.cards)

    @override
    def add(self, card) -> None:
        self.cards.add(card)

    @override
    def delete(self, card: Card) -> None:
        if card in self.cards:
            self.cards.remove(card)
