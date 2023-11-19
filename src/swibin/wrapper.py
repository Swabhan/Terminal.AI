import functools
from .describe_error import describe_error

def with_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            describe_error(e, args, kwargs)
    return wrapper
