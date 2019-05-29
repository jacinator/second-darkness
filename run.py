import operator

from functions.menus import NationActionMenu
from templates.nations import Nation
from templates.regions import Region

import resources.regions


def run(won=False):
    while won is False:
        for nation in sorted(Nation.objects, key=operator.attrgetter("ordering")):
            print(f"{nation.name}'s turn")

            if not nation.computer:
                menu = NationActionMenu(nation)
                menu.choose()

        won = True


if __name__ == "__main__":
    run()
