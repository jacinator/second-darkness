class Render(object):

    def __init__(self, value, width=79):
        self.value = value
        self.width = width

    def get_frame(self):
        return '-' * self.width

    def get_value(self):
        return self.value

    def render(self):
        return '{0}\n{1}'.format(
            self.get_frame(),
            self.get_value(),
        )


class Table(Render):

    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
        self.column_width = int(self.width / len(value[0])) - 1

    def get_value(self):
        return '\n'.join(map(self.get_row, self.value))

    def get_col(self, col):
        return '{0:<{width}}'.format(col, width=self.column_width)

    def get_row(self, row):
        return ' '.join(map(self.get_col, row))


class TableList(Render):

    def __init__(self, title, *value, **kwargs):
        self.title = title
        super().__init__(value, **kwargs)

    def get_value(self):
        return '{0:^{width}}\n{1}'.format(
            self.title,
            '\n'.join(self.value),
            width=self.width,
        )
