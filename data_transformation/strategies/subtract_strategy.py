from data_transformation.strategies.base_strategy import TransformationStrategy
from data_transformation.utils.error_handler import ErrorHandler


class SubtractStrategy(TransformationStrategy):
    """Strategy for subtract two numbers."""

    @ErrorHandler.handle_errors("Error on SubtractStrategy.transform execution.")
    def transform(self, var1: float, var2: float) -> float:
        """
        Subtract two numbers together.

        Parameters:
        - var1 (float): First number.
        - var2 (float): Second number to be subtracted from the first.

        Returns:
        float: The subtraction of the two numbers.
        """
        return var1 - var2
