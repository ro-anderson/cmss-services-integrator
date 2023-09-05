import sys

from typing import Any
from typing import Optional
from typing import Union

from data_transformation.utils.data_transformer import DataTransformer


def main(function_name: str, var1: Union[str, float], var2: Optional[Union[str, float]] = None) -> Any:  # noqa ANN401
    """
    Execute the data transformation using the provided function name.

    This function dynamically determines the strategy to use based on the provided
    `function_name`.

    Parameters:
    - function_name (str): Name of the function (strategy) to execute.
    - var1 (Union[str, int]): First variable to be transformed. It can be a string or an integer.
    - var2 (Optional[Union[str, int]]): Second variable, optional depending on the strategy. It can be a string or an integer.

    Returns:
    Transformed data, which could either be a string or an integer.
    """

    # Dynamically construct the module and class names
    module_name = f"data_transformation.strategies.{function_name}_strategy"
    class_name = "".join(word.capitalize() for word in function_name.split("_")) + "Strategy"

    # Dynamically import the strategy
    module = __import__(module_name, fromlist=[class_name])
    strategy_class = getattr(module, class_name)

    transformer = DataTransformer(strategy_class())
    return transformer.execute_transformation(var1, var2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide at least a function_name and var1 as arguments.")  # noqa T201
        sys.exit(1)

    function_name = sys.argv[1]

    # Try to convert var1 to a float. If it's not a number, it will raise a ValueError,
    # in which case we just treat var1 as a string.
    try:
        var1 = float(sys.argv[2])
    except ValueError:
        var1 = sys.argv[2]

    # If a third argument (var2) is provided, try to convert it to a float as well.
    # If it's not a number, treat it as a string.
    if len(sys.argv) == 4:
        try:
            var2 = float(sys.argv[3])
        except ValueError:
            var2 = sys.argv[3]
        result = main(function_name, var1, var2)
    else:
        result = main(function_name, var1)

    print(result)  # noqa T201
