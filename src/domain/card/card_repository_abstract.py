from abc import ABC, abstractmethod

from domain.card.card import Card


class AbstractCardRepository(ABC):

    @abstractmethod
    def get_by_german(self, german: str) -> Card:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_italian(self, italian: str) -> Card:
        raise NotImplementedError

    @abstractmethod
    def all(self) -> list[Card]:
        raise NotImplementedError
    
    @abstractmethod
    def add(self, card: Card) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, card: Card) -> None:
        raise NotImplementedError
