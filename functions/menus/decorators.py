import functools


class ActionInner:

    def __init__(self, method, string):
        self.method = method
        self.string = string

    def __call__(self, *args, **kwargs):
        return self.method(*args, **kwargs)

    def __str__(self):
        return self.string


def action(string):
    def decorator(method):
        return functools.wraps(method)(ActionInner(method, string))
    return decorator
