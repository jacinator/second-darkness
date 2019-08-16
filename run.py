import operator

from functions.computers import run_computer
from functions.menus import NationActionMenu
from templates.nations import Nation
from templates.regions import Region

import resources.regions


def run(won=False):
    # This needs to be run after the regions areall defined, which is
    # why it's located here. Otherwise this could have been placed in
    # the nation template.
    for nation in Nation.objects:
        nation.resources += (nation.get_income() * 3)

    while won is False:
        for nation in sorted(Nation.objects, key=operator.attrgetter("ordering")):
            nation.collect_income()

            if not nation.computer:
                print(f"\n{nation.name}'s turn\n+ $ {nation.get_income():>6} Income\n  $ {nation.resources:>6} Total resources\n")
                for _ in range(4):
                    menu = NationActionMenu(nation)
                    menu.choose()
                print()
            else:
                run_computer(nation)


if __name__ == "__main__":
    run()
