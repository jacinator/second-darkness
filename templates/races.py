class Race(object):

    def __init__(self, singular, plural, adjective):
        self.singular = singular
        self.plural = plural
        self.adjective = adjective

    def __str__(self):
        return self.plural
