from sqlalchemy.orm import Session

from domain.tag.tag import Tag
from domain.tag.tag_repository_db import DbTagRepository


def test_tag_repository_can_add_tag(session_for_empty_unit_test_db: Session):
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


def test_tag_repository_can_update_tag(session_for_filled_unit_test_db: Session):
    # Arrange:
    tag_repo = DbTagRepository(session_for_filled_unit_test_db)
    tags = tag_repo.all()
    first_tag = tags[0]

    # Act:
    old_value = first_tag.value
    new_value = old_value + " updated"
    first_tag.value = new_value
    session_for_filled_unit_test_db.commit()

    # Assert:
    assert tag_repo.get_by_value(new_value) == first_tag


def test_db_tag_repo_can_delete_existing_tag(
    session_for_filled_unit_test_db: Session,
):
    # Arrange:
    tag_repo = DbTagRepository(session_for_filled_unit_test_db)
    tags = tag_repo.all()
    first_tag = tags[0]
    second_tag = tags[1]
    third_tag = tags[2]

    # Act:
    tag_repo.delete(second_tag)
    session_for_filled_unit_test_db.commit()

    # Assert:
    assert first_tag in tag_repo.all()
    assert second_tag not in tag_repo.all()
    assert third_tag in tag_repo.all()


def test_db_tag_repo_cannot_delete_not_existing_tag(
    session_for_filled_unit_test_db: Session,
):
    # Arrange:
    tag_repo = DbTagRepository(session_for_filled_unit_test_db)
    tags = tag_repo.all()
    assert len(tags) == 3
    second_tag = tags[1]
    third_tag = tags[2]

    # Act (delete existing tag):
    tag_repo.delete(second_tag)
    session_for_filled_unit_test_db.commit()
    assert len(tag_repo.all()) == 2
    assert second_tag not in tag_repo.all()

    # Act (delete not existing tag):
    tag_repo.delete(second_tag)
    session_for_filled_unit_test_db.commit()
    assert len(tag_repo.all()) == 2
    assert second_tag not in tag_repo.all()

    # Act (delete existing tag):
    tag_repo.delete(third_tag)
    session_for_filled_unit_test_db.commit()
    assert len(tag_repo.all()) == 1
