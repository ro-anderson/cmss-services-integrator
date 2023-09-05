from data_transformation.strategies.base_strategy import TransformationStrategy
from data_transformation.utils.error_handler import ErrorHandler


class ToLowercaseStrategy(TransformationStrategy):
    """Strategy to transform the given string to lowercase."""

    @ErrorHandler.handle_errors("Error on ToLowercaseStrategy.transform execution.")
    def transform(self, var1: str, var2: None = None) -> str:
        """
        Transform the given string to lowercase.

        Args:
            var1 (str): The string to transform.
            var2 (None, optional): Not used in this strategy. Defaults to None.

        Returns:
            str: The transformed lowercase string.
        """
        return var1.lower()
