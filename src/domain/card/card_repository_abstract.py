from abc import ABC, abstractmethod

from domain.card.card import Card


class AbstractCardRepository(ABC):
    @abstractmethod
    def all(self) -> list[Card]:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int) -> Card:
        raise NotImplementedError

    @abstractmethod
    def add(self, card: Card) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, card: Card) -> None:
        raise NotImplementedError
