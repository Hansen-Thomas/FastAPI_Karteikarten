import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from domain.card.card import Card
from domain.card.card_repository_db import DbCardRepository
import infra.db as db
import infra.db.orm as orm
from test.utils.test_cards import get_test_cards


@pytest.fixture
def engine_for_resetted_unit_test_db():
    """
    Creates a new empty sqlite database for each test and returns the engine for
    that.
    """
    engine = create_engine(db.URL_OBJECT_UNIT_TESTS, echo=True)
    db.metadata.drop_all(engine)
    db.metadata.create_all(engine)
    return engine


@pytest.fixture
def session_for_empty_unit_test_db(engine_for_resetted_unit_test_db):
    """
    Returns a session for a new empty sqlite database for each test.
    """
    orm.start_mappers()
    try:
        session = sessionmaker(bind=engine_for_resetted_unit_test_db)()
        yield session
    finally:
        session.close()
    clear_mappers()


@pytest.fixture
def session_for_filled_unit_test_db(
    engine_for_resetted_unit_test_db,
):
    """
    Returns a session for a new sqlite database with some cards for each test.
    """
    orm.start_mappers()
    try:
        # prepare the database:
        session_to_fill = sessionmaker(bind=engine_for_resetted_unit_test_db)()

        repo = DbCardRepository(session_to_fill)
        test_cards = get_test_cards()
        for card in test_cards:
            repo.add(card)

        session_to_fill.commit()
        session_to_fill.close()

        # return a session for the filled database:
        session = sessionmaker(bind=engine_for_resetted_unit_test_db)()
        yield session
    finally:
        session.close()
    clear_mappers()
