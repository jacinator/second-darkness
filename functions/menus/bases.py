from . import errors


class BaseMenu(object):
    """Basis for menus with rendering and handling.

    This base menu is the most basic methods necessary for a menu to
    be displayed properly and for a provided choice to be selected. The
    choice could be a string equal to one of the choices, or it could
    be an index fitting in the list.
    """

    choice_template = "{0:>3}. {1:.>20}"
    divide_template = " " * 3

    def __init__(self, choices, columns=3):
        if not len(choices):
            raise errors.EmptyChoicesError(choices)

        self.choices = choices
        self.columns = columns
        self.strings = tuple(map(str, choices))

    # These methods are for rendering the menu. They take the string
    # representations of all the choices and format them into indexed
    # rows and columns.

    def get_col(self, args):
        return self.choice_template.format(*args)

    def get_row(self, args):
        return self.divide_template.join(map(
            self.get_col,
            enumerate(*args),
        ))

    def render(self):
        return "\n".join(map(self.get_row, [
            (self.strings[index:index + self.columns], index + 1)
            for index in range(0, len(self.strings), self.columns)
        ]))

    # These methods handle the responses to the menu. They take a
    # string input, check if it's a valid index or convert it to one,
    # and return the value at that index.

    def get_index(self, choice):
        if choice.isdigit() and int(choice) <= len(self.choices):
            return int(choice) - 1
        else:
            cleaned = tuple(map(str.lower, self.strings))
            return cleaned.index(choice.lower())

    def get_value(self, choice):
        try:
            index = self.get_index(choice)
            return self.choices[index]
        except (ValueError, IndexError):
            raise errors.InvalidChoiceError(choice)


class MainMenu(BaseMenu):
    """Provide common setups to keep the code DRY.

    This class simply builds on the BaseMenu to provide some common utilities.
    """

    # This method compiles the most common senario into a single
    # function call, instead of writing them out each time.

    def choose(self):
        print(self.render())
        choice = input("> ")
        return self.get_value(choice)
