class ErrorMixin(object):
    message = ""

    def __init__(self, *args, **kwargs):
        msg = self.message.format(*args, **kwargs)
        super().__init__(msg)


class EmptyChoicesError(ErrorMixin, ValueError):
    message = "{} is an empty array of choices"


class InvalidChoiceError(ErrorMixin, IndexError):
    message = "{} is not a valid choice"
