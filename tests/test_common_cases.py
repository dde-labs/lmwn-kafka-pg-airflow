import os

from sqlalchemy import make_url, URL


def test_make_url():
    url: URL = make_url(os.getenv("LOCAL_PG_URL"))
    assert url.drivername == "postgresql"
    assert url.database == "postgres"
    assert url.host == "localhost"
    assert url.port == 5432
    assert url.username == "postgres"
    assert url.password is None
