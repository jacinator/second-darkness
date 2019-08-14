import operator

from functions import tables
from functions.menus import ObjectMenu, RegionActionMenu, decorators

from .regions import Region


class Nation(object):
    objects = []

    def __init__(self, name, race, ordering, allies, enemies, resources=1000, computer=True):
        self.objects.append(self)

        self.name = name
        self.race = race
        self.army = []

        self.allies = allies
        self.enemies = enemies

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

    def get_friendly_regions(self):
        return filter(
            lambda r: r.occupants is self or r.occupants.name in self.allies,
            Region.objects,
        )

    def get_hostile_regions(self):
        return filter(
            lambda r: r.occupants.name in self.enemies,
            Region.objects,
        )

    def get_allies(self):
        return filter(
            lambda n: n.name in self.allies,
            self.objects,
        )

    def get_enemies(self):
        return filter(
            lambda n: n.name in self.enemies,
            self.objects,
        )
