import logging
import time

logging.basicConfig(level=logging.INFO)

def log_activity(func):
    """
    Decorator to log the activity of a function.
    """
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__} with result {result}")
        return result
    return wrapper

