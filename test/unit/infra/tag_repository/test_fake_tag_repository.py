from sqlalchemy.orm import Session

from domain.tag.tag import Tag
from test.utils.fake_tag_repo import FakeTagRepository


def test_fake_tag_repo_can_add_tag(fake_session: Session):
    # Arrange:
    tag_repo = FakeTagRepository(fake_session)
    tag = Tag(value="Freizeit")

    # Act:
    tag_repo.add(tag)
    fake_session.commit()

    # Assert:
    assert fake_session.committed
    assert tag_repo.all() == [tag]
    assert tag_repo.get_by_value(value=tag.value) == tag


def test_fake_tag_repo_can_delete_existing_tag(fake_session: Session):
    # Arrange:
    tag_repo = FakeTagRepository(fake_session)
    tag = Tag(value="Freizeit")

    # Act:
    tag_repo.add(tag)
    tag_repo.delete(tag)
    fake_session.commit()

    # Assert:
    assert tag_repo.all() == []
    assert tag_repo.get_by_value(tag.value) is None
    assert fake_session.committed


def test_fake_tag_repo_can_not_delete_not_existing_tag(fake_session: Session):
    # Arrange:
    tag_repo = FakeTagRepository(fake_session)
    tag = Tag(value="Freizeit")

    # Act:
    tag_repo.delete(tag)  # repo is empty, so nothing should happen
    fake_session.commit()

    # Assert:
    assert tag_repo.all() == []
    assert tag_repo.get_by_value(tag.value) is None
    assert fake_session.committed
