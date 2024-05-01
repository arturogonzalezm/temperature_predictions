import pytest
from unittest.mock import patch
from io import StringIO

from src.temperature_predictor import ClimateData


@pytest.fixture
def climate_instance():
    with patch('sys.stdin', new_callable=StringIO):
        instance = ClimateData()
    return instance


def test_singleton_pattern(climate_instance):
    new_instance = ClimateData()
    assert climate_instance is new_instance, "ClimateData class is not following singleton pattern"
