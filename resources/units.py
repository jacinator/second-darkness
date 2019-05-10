from templates import units
from resources import nations, races

arda_guard = units.RegularUnit(
    name="Arda Guard",
    nations=[nations.mithlond, nations.rivendell, nations.greenwood],
)

axemen = units.MilitiaUnit(
    name="Axemen",
    nations=[nations.erebor, nations.ered_luin],
)

berserkers = units.RegularUnit(
    name="Berserkers",
    nations=[nations.anduin_valley],
)

elven_blades = units.MilitiaUnit(
    name="Elven Blades",
    nations=[nations.greenwood, nations.lorien, nations.mithlond, nations.rivendell],
)

corsairs = units.MilitiaUnit(
    name="Corsairs",
    nations=[nations.umbar],
)

dragon_hunters = units.MissileUnit(
    name="Dragon Hunters",
    nations=[nations.erebor],
)

dunedain = units.RegularUnit(
    name="Dunedain",
    nations=[nations.arnor],
)

engineers = units.MissileUnit(
    name="Engineers",
    nations=[nations.erebor, nations.ered_luin],
)

ents = units.MonsterUnit(
    name="Ents",
    nations=[nations.lorien],
)

galadhrim = units.RegularUnit(
    name="Galadhrim",
    nations=[nations.lorien],
)

gondorians = units.MilitiaUnit(
    name="Gondorians",
    nations=[nations.gondor, nations.dol_amroth],
)

guardsmen = units.CavalryUnit(
    name="Guardsmen",
    nations=[nations.rhun, nations.rohan],
)

haradrim = units.MilitiaUnit(
    name="Haradrim",
    nations=[nations.harad],
)

knights = units.CavalryUnit(
    name="Knights",
    nations=[nations.arnor, nations.dol_amroth, nations.gondor, nations.mithlond, nations.rivendell],
)

lancers = units.CavalryUnit(
    name="Lancers",
    nations=[nations.greenwood, nations.lorien],
)

marksmen = units.MissileUnit(
    name="Marksmen",
    nations=[nations.gondor, nations.dol_amroth, nations.harad, nations.rhun, nations.rohan],
)

mumakil = units.MonsterUnit(
    name="Mumakil",
    nations=[nations.harad],
)

orcs = units.MilitiaUnit(
    name="Orcs",
    nations=[nations.angmar, nations.isengard, nations.mirkwood, nations.mordor],
)

raiders = units.MissileUnit(
    name="Raiders",
    nations=[nations.angmar, nations.dunland, nations.isengard, nations.mirkwood, nations.mordor, nations.umbar],
)

rangers = units.MissileUnit(
    name="Rangers",
    nations=[nations.arnor, nations.gondor],
)

riders_rohan = units.CavalryUnit(
    name="Riders of Rohan",
    nations=[nations.rohan],
)

rohirrim = units.MilitiaUnit(
    name="Rohirrim",
    nations=[nations.rohan],
)

sentries = units.MissileUnit(
    name="Sentries",
    nations=[nations.anduin_valley, nations.greenwood, nations.lorien, nations.mithlond, nations.rivendell],
)

southrons = units.RegularUnit(
    name="Southrons",
    nations=[nations.harad],
)

spearmen = units.MilitiaUnit(
    name="Spearmen",
    nations=[nations.anduin_valley, nations.arnor, nations.dunland, nations.rhun],
)

tower_guard = units.RegularUnit(
    name="Tower Guard",
    nations=[nations.gondor],
)

trolls = units.MonsterUnit(
    name="Trolls",
    nations=[nations.mirkwood, nations.mordor],
)

uruk_hai = units.RegularUnit(
    name="Uruk-hai",
    nations=[nations.isengard],
)

uruk = units.RegularUnit(
    name="Uruk",
    nations=[nations.angmar, nations.mirkwood, nations.mordor],
)

variags = units.RegularUnit(
    name="Variags",
    nations=[nations.rhun],
)

veterans = units.RegularUnit(
    name="Veterans",
    nations=[nations.erebor, nations.ered_luin],
)

wargs = units.CavalryUnit(
    name="Wargs",
    nations=[nations.angmar, nations.isengard],
)

watchmen = units.RegularUnit(
    name="Watchmen",
    nations=[nations.erebor],
)
