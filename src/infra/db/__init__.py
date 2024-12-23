import logging
import sys

from sqlalchemy import Connection, Engine, MetaData, URL, create_engine
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
        stmt = select(User).where(User.id == 1)
        user = session.execute(stmt).fetchone()
        print(user)

"""

# central SqlAlchemy setup: ===================================================


# 1) setup the database metadata: ---------------------------------------------


metadata = MetaData()
import infra.db.tables  # by that the metadata is initialized


# 2) setup the database-URL-objects (based on the config-file): ---------------


logger = logging.getLogger(__name__)
logger.debug("configure db-connection based on config-file")

# Create connection-URLs:

# example for a MS-SQL-Server-URL:
_driver_name = "mssql+pyodbc"  # change that depending on your DBMS
_query = {"driver": "ODBC Driver 17 for SQL Server"}

# URL for the production-database:
URL_OBJECT_PROD = URL.create(
    drivername=_driver_name,
    host=definitions.CFG_DB_HOST_PRODUCTION,
    database=definitions.CFG_DB_NAME_PRODUCTION,
    query=_query,
)

# URL for the stage-database (only used for testing):
URL_OBJECT_STAGE = URL.create(drivername="sqlite", database="stage.db")

# URL for the local SQLite-database (only used for unit testing):
URL_OBJECT_UNIT_TESTS = URL.create(drivername="sqlite", database="pytest.db")
# URL_OBJECT_UNIT_TESTS = URL.create(drivername="sqlite", database=":memory:")

# pick the URL-object used for this application-run based on the config-file:
if definitions.CFG_DB_USE == "Production":
    raise NotImplementedError("Production-DB not implemented yet.")
    _url_object = URL_OBJECT_PROD
elif definitions.CFG_DB_USE == "Stage":
    _url_object = URL_OBJECT_STAGE
elif definitions.CFG_DB_USE == "UnitTests":
    _url_object = URL_OBJECT_UNIT_TESTS
else:
    logger.error(
        "USE_DB must be either 'Production' or 'Stage', "
        f"but current value is '{definitions.CFG_DB_USE}'."
    )
    logger.error("--- CLOSE APP, BAD DB-CONFIGURATION------------------------")
    sys.exit(1)

logger.info(f"using database: {definitions.CFG_DB_USE}")


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


# 5) Provide other utility functions: -----------------------------------------
#
#    These functions should not be used by the application, but only by
#    scripts or tests. They offer a way to retrieve an engine and to setup
#    the schema.


def _get_engine(db: str, echo: bool = False) -> Engine:
    if db == "Production":
        _url = URL_OBJECT_PROD
    else:
        _url = URL_OBJECT_STAGE

    engine = create_engine(_url, echo=echo)
    return engine


def _setup_schema(engine: Engine) -> None:
    metadata.create_all(engine)
