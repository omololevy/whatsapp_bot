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

def timing(func):
    """
    Decorator for time the execution of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper