import logging
from typing import Callable, Dict, List


def logging_decorator(logger: logging.Logger = logging.getLogger(__name__)) -> Callable:
    def func_wrapper(func: Callable) -> Callable:
        def wrapped(*args: List, **kwargs: Dict) -> Callable:
            logger.debug(
                f"Start function: {func.__name__}, args={str(args)[:50]}, kwargs={str(kwargs)[:80]}"
            )
            result = func(*args, **kwargs)
            # logger.debug(f"Finish success function {func.__name__}, with result {result}")
            return result

        return wrapped

    return func_wrapper
