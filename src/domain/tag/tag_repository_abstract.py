from abc import ABC, abstractmethod

from domain.tag.tag import Tag


class AbstractTagRepository(ABC):
    @abstractmethod
    def get_by_value(self, value: str) -> Tag | None:
        raise NotImplementedError

    @abstractmethod
    def all(self) -> list[Tag]:
        raise NotImplementedError

    @abstractmethod
    def add(self, tag: Tag) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, tag: Tag) -> None:
        raise NotImplementedError
