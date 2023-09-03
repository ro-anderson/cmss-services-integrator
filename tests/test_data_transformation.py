import pytest

from data_transformation.main import main


# Test data
test_data = [
    ("add", 5, 3, 8),
    ("add", -1, 3, 2),
    ("add", 0, 0, 0),
    ("subtract", 5, 3, 2),
    ("subtract", 3, 5, -2),
    ("subtract", 0, 0, 0),
    ("to_lowercase", "HELLO", None, "hello"),
    ("to_lowercase", "World", None, "world"),
    ("to_lowercase", "PYTHON", None, "python"),
]


# Parametrized test function
@pytest.mark.parametrize("operation,val1,val2,expected", test_data)
def test_transformations(operation, val1, val2, expected):
    result = main(operation, val1, val2)
    assert result == expected
