import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

import infra.db as db
import infra.db.orm as orm


@pytest.fixture
def local_empty_unit_test_db():
    engine = create_engine(db.URL_OBJECT_UNIT_TESTS, echo=True)
    db.metadata.drop_all(engine)
    db.metadata.create_all(engine)
    return engine


@pytest.fixture
def unit_test_db_session(local_empty_unit_test_db):
    orm.start_mappers()
    try:
        session = sessionmaker(bind=local_empty_unit_test_db)()
        yield session
    finally:
        session.close()
    clear_mappers()


# @pytest.fixture
# def local_prepared_unit_test_db(local_empty_unit_test_db):
    