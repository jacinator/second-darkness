import operator

from functions import tables
from functions.menus import ObjectMenu, RegionActionMenu, decorators

from .regions import Region


class Nation(object):
    objects = []

    def __init__(self, name, race, ordering, resources=1000, computer=True):
        self.objects.append(self)

        self.name = name
        self.race = race
        self.army = []

        self.resources = resources
        self.computer = computer
        self.ordering = ordering

    def __str__(self):
        return self.name

    @decorators.action("Regions")
    def action_nations(self):
        region_menu = ObjectMenu(Region.objects, lambda r: r.occupants is self)
        action_menu = RegionActionMenu(self, region_menu.choose())
        action_menu.choose()

    @decorators.action("Resources")
    def action_resources(self):
        print(tables.Table((
            ("Resources", "$ {}".format(self.resources)),
            ("Income", "$ {}".format(sum(map(
                operator.attrgetter("resources"),
                filter(lambda r: r.occupants is self, Region.objects),
            )))),
        )).render())
