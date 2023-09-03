from data_transformation.strategies.base_strategy import TransformationStrategy


class DataTransformer:
    """The DataTransformer class acts as a context.

    It uses a strategy to execute data transformation operations.
    """

    def __init__(self, strategy: TransformationStrategy) -> None:
        """Initialize the DataTransformer with a given strategy.

        Args:
            strategy (TransformationStrategy): The strategy for data transformation.
        """
        self._strategy = strategy

    def execute_transformation(self, var1: object, var2: object = None) -> object:
        """Execute the data transformation using the strategy.

        Args:
            var1: First variable to transform.
            var2 (optional): Second variable. Depends on the strategy.

        Returns:
            Transformed data.
        """
        return self._strategy.transform(var1, var2)
