import os
from pathlib import Path

from sqlalchemy import make_url

from scripts.pg import reload_data_to_pg
from scripts.kafka import publish_data_to_kafka



def test_reload_data_to_pg(root_path: Path):
    reload_data_to_pg(
        url=make_url(os.getenv("LOCAL_PG_URL")),
        base_path=root_path,
    )


def test_publish_data_to_kafka(root_path: Path):
    publish_data_to_kafka(
        host=os.getenv("LOCAL_KAFKA_HOST"),
        base_path=root_path,
    )
