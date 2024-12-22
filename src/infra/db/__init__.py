import logging
import sys

from sqlalchemy import Connection, MetaData, URL, create_engine
from sqlalchemy.orm import sessionmaker

import config.definitions as definitions

"""
This module provides basic database-access for all other modules of the
application via SqlAlchemy.

First the metadata-object of our SqlAlchemy-setup is initialized to define all
used tables. Then depending on the configuration-file connection-URLs are
constructed and stored in module-level variables.

Finally we provide functions to get a SqlAlchemy-Session and a SqlAlchemy-
Connection as our basic entry-points for DB-access with SqlAlchemy.

-------------------------------------------------------------------------------

Basic usage:
- import the module (e.g. as db)
- request a session or connection with a context-manager:
    - for a session: "with db.get_session() as session:"
    - for a connection: "with db.get_connection() as conn:"
- use the session or connection to query the database
- the session or connection will be closed automatically after the block

-------------------------------------------------------------------------------

Below you find two examples using a not existing Users-object and table with:


Example usage for a connection (so no ORM): -----------------------------------

    from sqlalchemy import text

    import infra.database as db

    stmt = text("SELECT * FROM users WHERE id = :id")

    with db.get_connection() as conn:
        result = conn.execute(stmt, {"id": 1}).fetchone()
        print(result)


Example usage for a session (with ORM): ---------------------------------------

    from sqlalchemy import select

    import infra.database as db
    import infra.database.orm as orm

    from domain.users import User

    orm.start_mappers()

    with db.get_session() as session:
        user = session.execute(select(User).where(User.id == 1)).fetchone()
        print(user)

"""

# central SqlAlchemy setup: ===================================================


# 1) setup the database metadata: ---------------------------------------------


metadata = MetaData()
import infra.db.tables  # by that the metadata is initialized


# 2) setup the database-URL-objects (based on the config-file): ---------------


logger = logging.getLogger(__name__)
logger.debug("configure db-connection based on config-file")

# URL for the local SQLite-database (only used for testing):
URL_OBJECT_LOCAL = URL.create(drivername="sqlite", database="test.db")

# pick the URL-object used for this application-run based on the config-file:
if definitions.CFG_USE_DB == "Production":
    _url_object = None  # TODO: TBD
    _db_name = definitions.CFG_PRODUCTION_DB
elif definitions.CFG_USE_DB == "Test":
    _url_object = None  # TODO: TBD
    _db_name = definitions.CFG_TEST_DB
elif definitions.CFG_USE_DB == "Local":
    _url_object = URL_OBJECT_LOCAL
    _db_name = "Local"
else:
    logger.error(
        "USE_DB must be either 'Production' or 'Test', "
        f"but current value is '{definitions.CFG_USE_DB}'."
    )
    logger.error("--- CLOSE APP, BAD DB-CONFIGURATION------------------------")
    sys.exit(1)

logger.info(f"using database: {_db_name}")


# 3) setup engine and sessionmaker: -------------------------------------------


_engine = create_engine(_url_object, echo=False)
_SessionFactory = sessionmaker(bind=_engine)


# 4) provide functions to get a connection and a session: ---------------------


def get_connection() -> Connection:
    return _engine.connect()

def get_session():
    try:
        session = _SessionFactory()
        yield session
    finally:
        session.close()
        print(f"Status connection-pool: {_engine.pool.status()}")
