from typing import override

from test.utils.fake_session import FakeSession
from domain.tag.tag import Tag
from domain.tag.tag_repository_abstract import AbstractTagRepository


class FakeTagRepository(AbstractTagRepository):
    def __init__(self, session: FakeSession) -> None:
        self.session = session
        self.tags: set[Tag] = set()

    @override
    def get_by_value(self, value: str) -> Tag | None:
        for tag in self.tags:
            if tag.value == value:
                return tag
        return None

    @override
    def all(self) -> list[Tag]:
        return list(self.tags)

    @override
    def add(self, tag: Tag) -> None:
        self.tags.add(tag)

    @override
    def delete(self, tag: Tag) -> None:
        if tag in self.tags:
            self.tags.remove(tag)
