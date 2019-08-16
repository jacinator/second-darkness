import operator

from functions.computers import run_computer
from functions.menus import NationActionMenu
from templates.nations import Nation
from templates.regions import Region

import resources.regions


def run(won=False):
    while won is False:
        for nation in sorted(Nation.objects, key=operator.attrgetter("ordering")):
            nation.collect_income()

            if not nation.computer:
                print(f"\n{nation.name}'s turn\n+ $ {nation.get_income()}\n")
                menu = NationActionMenu(nation)
                menu.choose()
                print()
            else:
                run_computer(nation)


if __name__ == "__main__":
    run()
