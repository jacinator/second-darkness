class Nation(object):
    objects = []

    def __init__(self, name, race, resources=1000, computer=True):
        self.objects.append(self)

        self.name = name
        self.race = race
        self.army = []

        self.resources = resources
        self.computer = computer

    def __str__(self):
        return self.name
