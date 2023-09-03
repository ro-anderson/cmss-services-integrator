from data_transformation.strategies.base_strategy import TransformationStrategy


class ToLowercaseStrategy(TransformationStrategy):
    """Strategy to transform the given string to lowercase."""

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
