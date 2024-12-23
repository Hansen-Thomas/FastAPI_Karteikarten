from typing import override

from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.card.card_repository_abstract import AbstractCardRepository
from domain.card.card import Card


class DbCardRepository(AbstractCardRepository):
    def __init__(self, session: Session):
        self.session = session

    @override
    def all(self) -> list[Card]:
        stmt = select(Card)
        return self.session.scalars(stmt).all()

    @override
    def get(self, id: int) -> Card | None:
        stmt = select(Card).where(Card.id == id)
        return self.session.scalar(stmt)

    @override
    def add(self, card: Card) -> None:
        self.session.add(card)

    @override
    def delete(self, card: Card) -> None:
        stmt = select(Card).where(Card.id == card.id)
        card = self.session.scalar(stmt)
        if card:
            self.session.delete(card)
