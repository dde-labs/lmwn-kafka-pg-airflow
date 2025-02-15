from pathlib import Path

import pytest
from dotenv import load_dotenv


load_dotenv(Path(__file__).parent.parent / '.env')


@pytest.fixture(scope="session")
def test_path() -> Path:
    return Path(__file__).parent


@pytest.fixture(scope="session")
def root_path(test_path: Path) -> Path:
    return test_path.parent
