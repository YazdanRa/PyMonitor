import functools


def monitor(*args, **kwargs):

    def real_decorator(func):

        @functools.wraps(func)
        def wrapper():
            pass

        return wrapper

    return real_decorator
