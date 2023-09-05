import pytest

from main import main


# Regular Test data
test_data = [
    ("add", 5, 3, 8),
    ("add", 5.4, 3, 8.4),
    ("add", -1, 3, 2),
    ("add", 0, 0, 0),
    ("subtract", 5, 3, 2),
    ("subtract", 3, 5, -2),
    ("subtract", 0, 0, 0),
    ("to_lowercase", "HELLO", None, "hello"),
    ("to_lowercase", "World", None, "world"),
    ("to_lowercase", "PYTHON", None, "python"),
]

# Error Test data
error_test_data = [
    ("to_lowercase", 34, None, "'int' object has no attribute 'lower'"),
    (
        "add",
        "b",
        3,
        'ERROR    data_transformation.utils.error_handler:error_handler.py:38 Error on ADDStrategy.transform execution. Original error: can only concatenate str (not "int") to str',  # noqa B950
    ),
    (
        "subtract",
        "a",
        3,
        "ERROR    data_transformation.utils.error_handler:error_handler.py:38 Error on SubtractStrategy.transform execution. Original error: unsupported operand type(s) for -: 'str' and 'int'",  # noqa B950
    ),
]


# Parametrized test function for regular scenarios
@pytest.mark.parametrize("operation,val1,val2,expected", test_data)
def test_transformations(operation, val1, val2, expected):
    result = main(operation, val1, val2)
    assert result == expected


# Parametrized test function for error scenarios
@pytest.mark.parametrize("operation,val1,val2,expected_error_message", error_test_data)
def test_transformations_errors(operation, val1, val2, expected_error_message, caplog):
    main(operation, val1, val2)
    assert expected_error_message in caplog.text
