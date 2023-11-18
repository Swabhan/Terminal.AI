import functools
from .insights import describe_error

def with_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(describe_error(e))
    return wrapper
