import sys
from io import StringIO
import pytest

from src.temperature_predictor import ClimateData


# Fixture to replace sys.stdin for test input
@pytest.fixture
def mock_stdin(monkeypatch):
    def _mock_stdin(input_data):
        monkeypatch.setattr(sys, 'stdin', StringIO(input_data))

    return _mock_stdin


# Fixture to capture sys.stdout outputs
@pytest.fixture
def capture_stdout(monkeypatch):
    output = StringIO()
    monkeypatch.setattr(sys, 'stdout', output)
    return output


# Tests for read_input
def test_read_input(mock_stdin):
    test_input = "3\nyear\tmonth\ttmax\ttmin\n2021\tJan\t25\t15\n2021\tFeb\tMissing\t10\n2021\tMar\t20\tMissing\n"
    mock_stdin(test_input)
    cd = ClimateData()
    cd.read_input()
    assert cd.df.shape == (3, 4)  # Expect 3 rows and 4 columns
    assert list(cd.df.columns) == ['year', 'month', 'tmax', 'tmin']


# Tests for process_data
def test_process_data(mock_stdin):
    test_input = "3\nyear\tmonth\ttmax\ttmin\n2021\tJan\t25\t15\n2021\tFeb\tMissing\t10\n2021\tMar\t20\tMissing\n"
    mock_stdin(test_input)
    cd = ClimateData()
    cd.read_input()
    cd.process_data()
    assert not cd.df['tmax'].isnull().any()  # Check no NaN values after interpolation
    assert not cd.df['tmin'].isnull().any()


# Tests for print_interpolated_values
def test_print_interpolated_values(mock_stdin, capture_stdout):
    test_input = "3\nyear\tmonth\ttmax\ttmin\n2021\tJan\t25\t15\n2021\tFeb\tMissing\t10\n2021\tMar\t20\tMissing\n"
    mock_stdin(test_input)
    cd = ClimateData()
    cd.read_input()
    cd.process_data()
    cd.print_interpolated_values()
    output = capture_stdout.getvalue().splitlines()
    assert len(output) == 2  # Expect 2 lines of output
    assert output[0] == '25.0'  # Expected interpolated value for tmax in Feb
    assert output[1] == '15.0'  # Expected interpolated value for tmin in Mar
