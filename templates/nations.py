from operator import attrgetter

from functions.tables import Table
from functions.menus import ObjectMenu, RegionActionMenu
from functions.menus.decorators import action

from .regions import Region


class Nation(object):
    objects = []

    def __init__(self, name, race, ordering, allies, enemies, computer=True):
        self.objects.append(self)

        self.name = name
        self.race = race
        self.army = []

        self.allies = allies
        self.enemies = enemies

        self.resources = 0
        self.computer = computer
        self.ordering = ordering

    def __str__(self):
        return self.name

    # ##### Information Retrieval ##### #
    # These methods are here to get and return information about this
    # Nation object.

    def get_income(self):
        return sum(r.resources for r in self.get_regions())

    def get_regions(self):
        return (r for r in Region.objects if r.occupants is self)

    # ##### Object Manipulation ##### #
    # These methods are for changing or modifying the data stored on
    # the class instance.

    def collect_income(self):
        self.resources += self.get_income()

    # ##### Menu Actions ##### #
    # These methods are put in place to allow the NationActionMenu to
    # properly manipulate and get information from Nation objects.

    @action("Regions")
    def action_regions(self):
        region_menu = ObjectMenu(self.get_regions())
        action_menu = RegionActionMenu(self, region_menu.choose())
        action_menu.choose()

    @action("Resources")
    def action_resources(self):
        print(Table((
            ("Resources", "$ {}".format(self.resources)),
            ("Income", "$ {}".format(self.get_income())),
        )).render())
        input("Press enter to continue")
