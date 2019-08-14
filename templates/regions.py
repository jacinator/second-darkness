import functools

from functions import battles, strings, tables
from functions.menus import ObjectMenu, decorators, errors


def get_unit_row(args):
    return (args[0].name, args[1], args[0].offense, args[0].defense,)


def clean_units(method):
    @functools.wraps(method)
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

    def _clean_army(self):
        for unit in [u for u, c in self.army.items() if c <= 0]:
            del self.army[unit]

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

    def get_neighbors(self):
        return filter(
            lambda r: r.name in self.neighbors,
            self.objects,
        )

    def get_friendly_neighbors(self, nation):
        return filter(
            lambda r: r.occupants is nation or r.occupants.name in nation.allies,
            self.get_neighbors(),
        )

    def get_hostile_neighbors(self, nation):
        return filter(
            lambda r: r.occupants.name in nation.enemies,
            self.get_neighbors(),
        )

    def get_report(self):
        return tables.Table((
            ("Name", strings.capitalize(self.name)),
            ("Occupants", strings.capitalize(self.occupants.name)),
            ("Inhabitants", strings.capitalize(self.occupants.race.plural)),
            ("Resources", "+ {}".format(self.resources)),
            ("Strength", "! {}".format(self.get_strength())),
        )).render()

    def get_neighbor_reports(self):
        return tables.TableList(
            "{} and {} neighboring regions".format(
                strings.capitalize(self.name),
                len(self.neighbors),
            ),
            self.get_report(),
            *map(Region.get_report, self.get_neighbors()),
        ).render()

    def get_strength(self):
        return sum(self.army.values())

    def get_units_report(self, nation=None):
        if nation is None:
            nation = self.occupants

        heading = [("Name", "Number", "Offense", "Defense")]
        content = list(map(get_unit_row, [x for x in self.army.items() if nation in x[0].nations]))
        return tables.Table(heading + content).render()

    def has_army(self):
        return len(self.army.keys())

    def move_units(self, nation, to):
        units = {}

        for unit, count in self.army.items():
            if nation in unit.nations:
                units[unit] = count

        to.add_units(units)
        self.sub_units(units)

    @decorators.action("Attack")
    def action_attack(self, nation):
        try:
            against = ObjectMenu(
                self.objects,
                lambda r: r.occupants != nation and r.name in self.neighbors,
            ).choose()
        except errors.EmptyChoicesError:
            print("{} cannot attack from {} - there aren't any enemies nearby!".format(
                strings.capitalize(nation.name),
                self.name,
            ))
        else:
            battles.battle(nation, self, against)

            if not against.has_army():
                against.occupants = self.occupants
                self.move_units(nation, against)

            print(tables.TableList(
                "Unit statuses",
                self.get_units_report(),
                against.get_units_report(),
            ).render())

    @decorators.action("Details")
    def action_details(self, nation):
        print(self.get_neighbor_reports())

    @decorators.action("Move")
    def action_move(self, nation):
        try:
            to = ObjectMenu(
                self.objects,
                lambda r: r.occupants == nation and r.name in self.neighbors,
            ).choose()
        except errors.EmptyChoicesError:
            print("{} cannot move from {} - there aren't any friendly regions nearby!".format(
                strings.capitalize(nation.name),
                self.name,
            ))
        else:
            self.move_units(nation, to)

    @decorators.action("Review")
    def action_review(self, nation):
        print(self.get_units_report(nation))

    @decorators.action("Recruit")
    def action_recruit(self, nation):
        unit_menu = ObjectMenu(
            nation.army,
            lambda u: u.developed <= self.developed,
        )
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

        print(tables.TableList("Recruited these units", tables.Table((
            ("Name", "Count", "Offense", "Defense",),
            *map(get_unit_row, units.items()),
        )).render()).render())
