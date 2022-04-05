import logging
from typing import Callable, Dict, List


def logging_decorator(func: Callable) -> Callable:
    def return_wrapped(*args: List, **kwargs: Dict) -> Callable:
        logger = logging.getLogger(__name__)
        logger.debug(f"Start function: {func.__name__}, args={str(args)[:50]}, kwargs={str(kwargs)[:80]}")
        result = func(*args, **kwargs)
        # logger.debug(f"Finish success function {func.__name__}, with result {result}")
        return result

    return return_wrapped
