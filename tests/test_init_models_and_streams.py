import os
from pathlib import Path

from sqlalchemy import make_url

from scripts.pg import create_models_and_streams_to_pg


def test_create_models_and_streams(root_path: Path):
    create_models_and_streams_to_pg(
        url=make_url(os.getenv("LOCAL_PG_URL")),
        base_path=root_path,
    )
