from middle_earth.map_brownlands import *
from middle_earth.map_eriador import *
from middle_earth.map_gondor_rohan import *
from middle_earth.map_misty_mountains import *
from middle_earth.map_mordor import *
from middle_earth.map_wilderland import *

from lists_dictionaries.territory_list import TerritoryList

from interface.faction import FactionInterface
from interface.alliance import AllianceInterface

Mordor = FactionInterface(mordor)
Mordor.Run()
