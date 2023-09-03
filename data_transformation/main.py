from typing import Any
from typing import Optional
from typing import Union

from data_transformation.utils.data_transformer import DataTransformer


def main(function_name: str, var1: Union[str, int], var2: Optional[Union[str, int]] = None) -> Any:  # noqa ANN401
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
