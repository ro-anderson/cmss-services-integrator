### 2. `data_transformation_functions.md`

#### Data Transformation Functions Challenge

In the context of web applications, there's a growing need for extensible and scalable functionalities that allow users to process and transform data. This challenge revolves around creating an extensible architecture for such data transformation operations.

- A scenario where the web application serves as a bridge between a CMMS system and an ERP.
- Current functionalities that range from simple string manipulations to complex operations.

#### The task:

- Construct Python functions capable of performing operations such as addition, subtraction, and the conversion of strings from uppercase to lowercase.
- Formulate a `main.py` function that, given a function name, `var1`, and `var2` as parameters, initiates the appropriate transformation function.
- Prioritize architectural extensibility, ensuring that the inclusion of new transformation operations in the future doesn't require alterations to the `main.py` function.

#### The Architecture:

To address the challenge in a robust and scalable manner, we formulated a library that leans heavily on the Strategy Design Pattern. This design pattern facilitates the definition of a family of algorithms, encapsulates each algorithm, and makes the algorithms interchangeable.

Directory Structure:
```
data_transformation
├── __init__.py
├── strategies
│   ├── __init__.py
│   ├── add_strategy.py
│   ├── base_strategy.py
│   ├── subtract_strategy.py
│   └── to_lowercase_strategy.py
└── utils
    ├── __init__.py
    └── data_transformer.py
```

- **TransformationStrategy:** This abstract class serves as a blueprint for all data transformation strategies. Every new strategy should derive from this class and provide a concrete implementation for the `transform` method.


- **DataTransformer:** This class functions as a context. It harnesses a strategy to execute data transformation operations. By leveraging the Strategy Design Pattern, we ensure the easy addition of new transformation strategies in the future, such as a potential `multiply_strategy.py`.

#### Key Decisions:

1. **Strategy Design Pattern:** By adopting the Strategy Design Pattern, we've decoupled the algorithm from the client that uses it. This paves the way for future extensions with minimal changes to existing code. New transformations can be added as new strategy classes without modifying the client or the context.
 - UML class diagram
![](../images/strategy_uml_class_diagram.jpeg)
    font: https://en.wikipedia.org/wiki/Strategy_pattern

2. **Modular and Extensible Design:** The strategies have been isolated in their dedicated directory. This clear segmentation simplifies the process of appending new transformation strategies in the future.

#### Sample Execution:

Incorporating the library into the system facilitates operations like this:

```bash
$ python main.py add 5 3

Output: 8

$ python main.py convert_to_lowercase 'HELLO'

Output: hello
```

#### Conclusion:

Using the Strategy Design Pattern, this solution not only meets the requirements set forth in the challenge but also prepares the groundwork for easy expansions in the future.

#### Testing the Transformation Operations:

In line with best practices, a suite of tests was formulated to ensure the correctness and reliability of the transformations. This helps in validating both simple and complex operations. By executing the command `make test`, the test suite is triggered.

The tests utilize the popular Python testing framework, `pytest`, and cover a wide range of scenarios, including:
- Basic arithmetic operations such as addition and subtraction with integers, floats, and edge cases.
- String transformation tests for converting uppercase strings to lowercase.

```python
import pytest
from main import main

# Test data
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

# Parametrized test function
@pytest.mark.parametrize("operation,val1,val2,expected", test_data)
def test_transformations(operation, val1, val2, expected):
    result = main(operation, val1, val2)
    assert result == expected
```
