from pathlib import Path

import pytest


@pytest.fixture
def test_data():
    return Path(__file__).parent / "test_data.csv"
