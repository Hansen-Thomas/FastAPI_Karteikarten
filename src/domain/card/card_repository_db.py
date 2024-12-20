from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.card.card_repository_abstract import AbstractCardRepository
from domain.card.card import Card


class DbCardRepository(AbstractCardRepository):
    def __init__(self, session: Session):
        self.session = session
        
    def all(self) -> list[Card]:
        return self.session.query(Card).all()
    
    def get(self, id: int) -> Card | None:
        stmt = select(Card).where(Card.id == id)
        return self.session.execute(stmt).scalar()
    
    def add(self, card: Card) -> None:
        self.session.add(card)
        self.session.commit()
        
    def delete(self, id: int) -> None:
        stmt = select(Card).where(Card.id == id)
        card = self.session.execute(stmt).scalar()
        self.session.delete(card)
        self.session.commit()
