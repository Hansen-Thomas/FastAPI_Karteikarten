from typing import override

from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.tag.tag import Tag
from domain.tag.tag_repository_abstract import AbstractTagRepository


class DbTagRepository(AbstractTagRepository):
    def __init__(self, session: Session):
        self.session = session

    @override
    def get_by_value(self, value: str) -> Tag | None:
        stmt = select(Tag).where(Tag.value == value)
        return self.session.scalar(stmt)
    
    @override
    def all(self) -> list[Tag]:
        stmt = select(Tag)
        return self.session.scalars(stmt).all()
    
    @override
    def add(self, tag: Tag) -> None:
        self.session.add(tag)
    
    @override
    def delete(self, tag: Tag) -> None:
        self.session.delete(tag)
