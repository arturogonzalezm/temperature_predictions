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


def singleton_behavior(climate_instance):
    new_instance = ClimateData()
    assert climate_instance is new_instance


def read_input_with_valid_data(mock_stdin, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\t25\t15\n2021\tFeb\t20\t10\n")
    climate_instance.read_input()
    assert not climate_instance.df.empty


def read_input_with_missing_values(mock_stdin, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\tMissing\t15\n2021\tFeb\t20\tMissing\n")
    climate_instance.read_input()
    assert climate_instance.df.isnull().values.any()


def process_data_with_no_missing_values(mock_stdin, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\t25\t15\n2021\tFeb\t20\t10\n")
    climate_instance.read_input()
    climate_instance.process_data()
    assert not climate_instance.df.isnull().values.any()


def process_data_with_missing_values(mock_stdin, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\tMissing\t15\n2021\tFeb\t20\tMissing\n")
    climate_instance.read_input()
    climate_instance.process_data()
    assert not climate_instance.df.isnull().values.any()


def print_interpolated_values_with_no_missing_values(mock_stdin, capsys, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\t25\t15\n2021\tFeb\t20\t10\n")
    climate_instance.read_input()
    climate_instance.process_data()
    climate_instance.print_interpolated_values()
    captured = capsys.readouterr()
    assert len(captured.out.splitlines()) == 0


def print_interpolated_values_with_missing_values(mock_stdin, capsys, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\tMissing\t15\n2021\tFeb\t20\tMissing\n")
    climate_instance.read_input()
    climate_instance.process_data()
    climate_instance.print_interpolated_values()
    captured = capsys.readouterr()
    assert len(captured.out.splitlines()) == 2


def print_interpolated_values_with_missing_tmax(mock_stdin, capsys, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\tMissing\t15\n2021\tFeb\t20\t10\n")
    climate_instance.read_input()
    climate_instance.process_data()
    climate_instance.print_interpolated_values()
    captured = capsys.readouterr()
    assert len(captured.out.splitlines()) == 1


def print_interpolated_values_with_missing_tmin(mock_stdin, capsys, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\t25\tMissing\n2021\tFeb\t20\t10\n")
    climate_instance.read_input()
    climate_instance.process_data()
    climate_instance.print_interpolated_values()
    captured = capsys.readouterr()
    assert len(captured.out.splitlines()) == 1


def print_interpolated_values_with_all_missing_values(mock_stdin, capsys, climate_instance):
    mock_stdin("2\nyear\tmonth\ttmax\ttmin\n2021\tJan\tMissing\tMissing\n2021\tFeb\t20\t10\n")
    climate_instance.read_input()
    climate_instance.process_data()
    climate_instance.print_interpolated_values()
    captured = capsys.readouterr()
    assert len(captured.out.splitlines()) == 2
