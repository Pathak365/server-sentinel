
import time
from functools import wraps


def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start_time
            print(
                f"{func.__name__} took {elapsed:.4f} seconds"
            )

    return wrapper
