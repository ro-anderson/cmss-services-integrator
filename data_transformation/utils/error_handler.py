import functools
import logging

from typing import Any
from typing import Callable
from typing import TypeVar


# Logger configuration
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger(__name__)

T = TypeVar("T", bound=Callable[..., Any])


class ErrorHandler:
    """A utility class for handling errors in a consistent manner."""

    @staticmethod
    def handle_errors(error_message: str) -> Callable[[T], T]:
        """Catch and handle exceptions for the decorated function.

        Parameters:
        - error_message (str): Message to be displayed when an error occurs.

        Returns:
        Decorated function that handles exceptions.
        """

        def decorator(func: T) -> T:
            @functools.wraps(func)
            def wrapper(*args, **kwargs) -> Any:  # noqa ANN401
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Here we're logging the error instead of printing.
                    # You can integrate with any logging framework of your choice.
                    log.error(f"{error_message} Original error: {str(e)}")

            return wrapper

        return decorator
