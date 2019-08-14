from templates import nations
from resources import races

from . import names

anduin_valley = nations.Nation(
   name=names.anduin_valley,
   race=races.men,
   ordering=7,
   allies=[
      names.greenwood,
      names.rohan,
   ],
   enemies=[
      names.angmar,
      names.mirkwood,
   ],
)

angmar = nations.Nation(
   name=names.angmar,
   race=races.goblins,
   ordering=6,
   allies=[
      names.mirkwood,
      names.mordor,
      names.moria,
   ],
   enemies=[
      names.anduin_valley,
      names.arnor,
      names.rivendell,
   ],
)

arnor = nations.Nation(
   name=names.arnor,
   race=races.men,
   ordering=8,
   allies=[
      names.ered_luin,
      names.gondor,
      names.mithlond,
      names.rivendell,
   ],
   enemies=[
      names.angmar,
      names.mordor,
      names.moria,
   ],
)

dol_amroth = nations.Nation(
   name=names.dol_amroth,
   race=races.men,
   ordering=5,
   allies=[
      names.gondor,
      names.rohan,
   ],
   enemies=[
      names.mordor,
      names.umbar,
   ],
)

dunland = nations.Nation(
   name=names.dunland,
   race=races.men,
   ordering=18,
   allies=[
      names.isengard,
   ],
   enemies=[
      names.rohan,
   ],
)

erebor = nations.Nation(
   name=names.erebor,
   race=races.dwarves,
   ordering=15,
   allies=[
      names.ered_luin,
      names.greenwood,
      names.rivendell,
   ],
   enemies=[
      names.mirkwood,
   ],
)

ered_luin = nations.Nation(
   name=names.ered_luin,
   race=races.dwarves,
   ordering=19,
   allies=[
      names.arnor,
      names.erebor,
      names.mithlond,
      names.rivendell,
   ],
   enemies=[],
)

gondor = nations.Nation(
   name=names.gondor,
   race=races.men,
   ordering=3,
   allies=[
      names.arnor,
      names.dol_amroth,
      names.rivendell,
      names.rohan,
   ],
   enemies=[
      names.harad,
      names.mirkwood,
      names.mordor,
      names.umbar,
   ],
)

greenwood = nations.Nation(
   name=names.greenwood,
   race=races.elves,
   ordering=11,
   allies=[
      names.anduin_valley,
      names.erebor,
      names.lorien,
      names.mithlond,
      names.rivendell,
   ],
   enemies=[
      names.mirkwood,
   ],
)

harad = nations.Nation(
   name=names.harad,
   race=races.men,
   ordering=2,
   allies=[
      names.mordor,
      names.rhun,
      names.umbar,
   ],
   enemies=[
      names.gondor,
   ],
)

isengard = nations.Nation(
   name=names.isengard,
   race=races.orcs,
   ordering=16,
   allies=[
      names.dunland,
      names.mirkwood,
      names.mordor,
   ],
   enemies=[
      names.rohan,
   ],
)

lorien = nations.Nation(
   name=names.lorien,
   race=races.elves,
   ordering=13,
   allies=[
      names.greenwood,
      names.mithlond,
      names.rivendell,
   ],
   enemies=[
      names.mirkwood,
      names.mordor,
      names.moria,
   ],
)

mirkwood = nations.Nation(
   name=names.mirkwood,
   race=races.orcs,
   ordering=10,
   allies=[
      names.angmar,
      names.isengard,
      names.mordor,
      names.moria,
   ],
   enemies=[
      names.anduin_valley,
      names.erebor,
      names.gondor,
      names.greenwood,
      names.lorien,
   ],
)

mithlond = nations.Nation(
   name=names.mithlond,
   race=races.elves,
   ordering=20,
   allies=[
      names.arnor,
      names.ered_luin,
      names.greenwood,
      names.lorien,
      names.rivendell,
   ],
   enemies=[
      names.mordor,
      names.umbar,
   ],
)

mordor = nations.Nation(
   name=names.mordor,
   race=races.orcs,
   ordering=1,
   allies=[
      names.angmar,
      names.harad,
      names.isengard,
      names.mirkwood,
      names.moria,
      names.rhun,
      names.umbar,
   ],
   enemies=[
      names.arnor,
      names.dol_amroth,
      names.gondor,
      names.lorien,
      names.mithlond,
      names.rivendell,
      names.rohan,
   ],
)

moria = nations.Nation(
   name=names.moria,
   race=races.goblins,
   ordering=12,
   allies=[
      names.angmar,
      names.mirkwood,
      names.mordor,
   ],
   enemies=[
      names.arnor,
      names.lorien,
      names.rivendell,
   ],
)

rhun = nations.Nation(
   name=names.rhun,
   race=races.men,
   ordering=14,
   allies=[
      names.harad,
      names.mordor,
   ],
   enemies=[],
)

rivendell = nations.Nation(
   name=names.rivendell,
   race=races.elves,
   ordering=9,
   allies=[
      names.arnor,
      names.erebor,
      names.ered_luin,
      names.gondor,
      names.greenwood,
      names.lorien,
      names.mithlond,
   ],
   enemies=[
      names.angmar,
      names.mordor,
      names.moria,
   ],
)

rohan = nations.Nation(
   name=names.rohan,
   race=races.men,
   ordering=17,
   allies=[
      names.anduin_valley,
      names.dol_amroth,
      names.gondor,
   ],
   enemies=[
      names.dunland,
      names.isengard,
      names.mordor,
   ],
)

umbar = nations.Nation(
   name=names.umbar,
   race=races.men,
   ordering=4,
   allies=[
      names.harad,
      names.mordor,
   ],
   enemies=[
      names.dol_amroth,
      names.gondor,
      names.mithlond,
   ],
)
