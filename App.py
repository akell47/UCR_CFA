import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from DiscoverPolicingScraper import DiscoverPolicingScraper


def get_url():
    return "postgresql://{0}:{1}@{2}/{3}".format(
        os.getenv("UCR_CFA_DB_USER"),
        os.getenv("UCR_CFA_DB_PASSWORD"),
        os.getenv("UCR_CFA_DB_HOST"),
        os.getenv("UCR_CFA_DB_NAME"))

engine = create_engine(get_url())


def get_db_info():
    connection = engine.connect()
    result = connection.execute("select version() as v")

    version = str(result.first())

    if version is None:
        version = "Failed"

    return version


def scrape_all():
    scrape_discover_policing()


def scrape_discover_policing():
    scraper = DiscoverPolicingScraper.createForDBOutput(engine)
    scraper.scrape()
