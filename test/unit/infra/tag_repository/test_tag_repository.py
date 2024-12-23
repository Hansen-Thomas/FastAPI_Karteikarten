from sqlalchemy.orm import Session

from domain.tag.tag import Tag
from domain.tag.tag_repository_db import DbTagRepository


def test_tag_repository_can_add_tags(session_for_empty_unit_test_db: Session):
    # Arrange:
    tag_repo = DbTagRepository(session_for_empty_unit_test_db)
    tag = Tag()
    tag.value = "test tag"

    # Act:
    tag_repo.add(tag)
    session_for_empty_unit_test_db.commit()

    # Assert:
    assert tag_repo.all() == [tag]
    assert tag_repo.get_by_value(tag.value) == tag


def test_tag_repository_can_get_all_tags(session_for_filled_unit_test_db: Session):
    # Arrange:
    tag_repo = DbTagRepository(session_for_filled_unit_test_db)

    # Act:
    tags = tag_repo.all()

    # Assert:
    assert len(tags) == 3
