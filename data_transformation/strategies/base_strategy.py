from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import Union


class TransformationStrategy(ABC):
    """The TransformationStrategy class is an abstract class that defines a contract
    for all data transformation strategies. Any new strategy should subclass
    this and provide an implementation for the transform method.
    """  # noqa D205

    @abstractmethod
    def transform(self, var1: Union[str, float], var2: Optional[Union[str, float]]) -> Union[str, float, None]:
        """
        Abstract method to transform data that can handle one or two variables.

        Parameters:
        - var1: First variable to be transformed.
        - var2: Second variable, optional depending on the strategy.

        Returns:
        Transformed data.
        """
        pass
