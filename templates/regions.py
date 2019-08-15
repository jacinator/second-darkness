from functools import wraps

from functions.battles import battle
from functions.menus import ObjectMenu
from functions.menus.decorators import action
from functions.menus.errors import EmptyChoicesError
from functions.strings import capitalize
from functions.tables import Table, TableList


def get_unit_table_render(region, units):
    return Table([("Name", "Number", "Offense", "Defense", "Region")] + [
        (u.name, c, u.offense, u.defense, region.name)
        for u, c in units.items()
    ]).render()


def clean_units(method):
    @wraps(method)
    def inner(self, units):
        for unit, count in units.items():
            method(self, unit, count)
        for unit in [u for u, c in self.army.items() if c <= 0]:
            del self.army[unit]
    return inner


class Region(object):
    objects = []

    def __init__(self, name, occupants, neighbors, resources=1, developed=0, army=None):
        self.objects.append(self)

        self.name = name
        self.occupants = occupants
        self.neighbors = neighbors
        self.resources = resources
        self.developed = developed
        self.army = army or {}

    def __str__(self):
        return self.name

    def get_report(self):
        return Table((
            ("Name", capitalize(self.name)),
            ("Occupants", capitalize(self.occupants.name)),
            ("Inhabitants", capitalize(self.occupants.race.plural)),
            ("Resources", "+ {}".format(self.resources)),
            ("Strength", "! {}".format(sum(self.army.values()))),
        )).render()

    def get_neighbor_reports(self):
        return TableList(
            "{} and {} neighboring regions".format(
                capitalize(self.name),
                len(self.neighbors),
            ),
            self.get_report(),
            *map(Region.get_report, self.get_neighbors()),
        ).render()

    def get_units_report(self, nation=None):
        if nation is None:
            nation = self.occupants

        return get_unit_table_render(self, {u: c for u, c in self.army.items() if nation in u.nations})

    # ##### Information Retrieval ##### #
    # These methods are here to get and return information about this
    # Nation object.

    def get_neighbors(self):
        return (r for r in self.objects if r.name in self.neighbors)

    def get_friendly_neighbors(self, nation):
        return (r for r in self.get_neighbors() if r.occupants.name in nation.allies or r.occupants is nation)

    def get_hostile_neighbors(self, nation):
        return (r for r in self.get_neighbors() if r.occupants.name in nation.enemies)

    # ##### Object Manipulation ##### #
    # These methods are for changing or modifying the data sotred on
    # the class instance.

    @clean_units
    def add_units(self, unit, count):
        try:
            self.army[unit] += count
        except KeyError:
            self.army[unit] = count

    @clean_units
    def sub_units(self, unit, count):
        try:
            self.army[unit] -= count
        except KeyError:
            pass

    def move_units(self, nation, to):
        units = {}

        for unit, count in self.army.items():
            if nation in unit.nations:
                units[unit] = count

        to.add_units(units)
        self.sub_units(units)

    def attack_enemy(self, nation, against):
        battle(nation, self, against)

        if not len(against.army.keys()):
            against.occupants = self.occupants
            self.move_units(nation, against)

    # ##### Menu Actions ##### #
    # These methods are put in place to allow the RegionActionMenu to
    # properly manipulate and get information from Region objects.

    @action("Attack")
    def action_attack(self, nation):
        try:
            menu = ObjectMenu(self.get_hostile_neighbors(nation))
            against = menu.choose()

            self.attack_enemy(nation, against)
            print(TableList(
                "Unit statuses",
                self.get_units_report(),
                against.get_units_report(),
            ).render())
            input("Press enter to continue")
        except EmptyChoicesError:
            print("{} cannot attack from {} - there aren't any enemies nearby!".format(
                capitalize(nation.name),
                self.name,
            ))

    @action("Details")
    def action_details(self, nation):
        print(self.get_neighbor_reports())
        input("Press enter to continue")

    @action("Move")
    def action_move(self, nation):
        try:
            menu = ObjectMenu(self.get_friendly_neighbors(nation))
            to = menu.choose()

            self.move_units(nation, to)
            print(TableList(
                "Unit statuses",
                to.get_units_report(),
                self.get_units_report(),
            ).render())
            input("Press enter to continue")
        except EmptyChoicesError:
            print("{} cannot move from {} - there aren't any friendly regions nearby!".format(
                capitalize(nation.name),
                self.name,
            ))

    @action("Review")
    def action_review(self, nation):
        print(self.get_units_report(nation))
        input("Press enter to continue")

    @action("Recruit")
    def action_recruit(self, nation):
        unit_menu = ObjectMenu((u for u in nation.army if u.developed <= self.developed))
        units = {}
        _continue = "Y"

        while _continue == "Y":
            unit_type = unit_menu.choose()
            unit_numb = None
            while unit_numb is None:
                try:
                    unit_numb = int(input("How many units of {} would you like to recruit? ".format(unit_type)))
                except ValueError:
                    print("Invalid number")
            units[unit_type] = unit_numb

            try:
                _continue = input("Continue [y/N] > ")[0].upper()
            except IndexError:
                _continue = ""

        for unit, count in units.items():
            count = min(int(nation.resources / unit.cost), count)
            units[unit] = count

            if nation not in unit.nations or count < 1:
                del units[unit]
            else:
                nation.resources -= unit.cost * count
        self.add_units(units)

        print(TableList(
            "Recruited these units",
            get_unit_table_render(units),
        ).render())
        input("Press enter to continue")
