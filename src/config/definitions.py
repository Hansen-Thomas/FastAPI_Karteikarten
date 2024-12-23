import configparser
import os

# dynamically build and provide directory-structure for other modules:
_MY_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(_MY_DIR, "..")
ROOT_DIR = os.path.join(SRC_DIR, "..")
LOG_DIR = os.path.join(ROOT_DIR, "logs")

PATH_CONFIG_FILE = os.path.join(SRC_DIR, "config.ini")
PATH_LOGGIG_CONFIG_FILE = os.path.join(SRC_DIR, "logging.json")

# Read main-config-file and provide definitions for other modules:
try:
    CONFIG = configparser.ConfigParser()
    CONFIG.read(PATH_CONFIG_FILE)

    # read database-configuration:
    CFG_DB_USE = CONFIG.get("DB", "USE")
    CFG_DB_HOST_PRODUCTION = CONFIG.get("DB", "HOST_PRODUCTION")
    CFG_DB_NAME_PRODUCTION = CONFIG.get("DB", "NAME_PRODUCTION")
    CFG_DB_HOST_STAGE = CONFIG.get("DB", "HOST_STAGE")
    CFG_DB_NAME_STAGE = CONFIG.get("DB", "NAME_STAGE")

except Exception as e:
    print(f"Error reading config-file: {e}")
    # as a workaround, we need to provide a couple of values for the DB-setup
    # if no config-file is given:
    CFG_DB_USE = "UnitTests"  # Always use local DB if no config file given
    CFG_DB_HOST_PRODUCTION = ""
    CFG_DB_NAME_PRODUCTION = ""
    CFG_DB_HOST_STAGE = ""
    CFG_DB_NAME_STAGE = ""
