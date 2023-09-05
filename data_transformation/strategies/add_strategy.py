from data_transformation.strategies.base_strategy import TransformationStrategy
from data_transformation.utils.error_handler import ErrorHandler


class AddStrategy(TransformationStrategy):
    """Strategy for adding two numbers."""

    @ErrorHandler.handle_errors("Error on ADDStrategy.transform execution.")
    def transform(self, var1: float, var2: float) -> float:
        """
        Add two numbers together.

        Parameters:
        - var1 (float): First number to be added.
        - var2 (float): Second number to be added.

        Returns:
        float: The sum of the two numbers.
        """
        return var1 + var2
