from beornings.army import *
from corsairs.army import *
from dunedain.army import *
from dunland.army import *
from dwarves.army import *
from easterlings.army import *
from ents.army import *
from gondor.army import *
from gundabad.army import *
from halflings.army import *
from harad.army import *
from high_elves.army import *
from isengard.army import *
from mordor.army import *
from rohan.army import *
from silvan_elves.army import *
from sindar_elves.army import *
from eagles.army import *
from monsters.army import *

from dunedain.heroes import *
from rohan.heroes import *
from halflings.heroes import *
from gondor.heroes import *
from dwarves.heroes import *

from functions.end_game import DefeatAssess

HeroDictionary = {
    smaug.name.lower(): smaug,
    thorondor.name.lower(): thorondor,
    aragorn.name.lower(): aragorn,
    beorn.name.lower(): beorn,
    elrohir.name.lower(): elrohir,
    elledan.name.lower(): elledan,
    dain.name.lower(): dain,
    gimli.name.lower(): gimli,
    gothmog.name.lower(): gothmog,
    treebeard.name.lower(): treebeard,
    faramir.name.lower(): faramir,
    boromir.name.lower(): boromir,
    denethor.name.lower(): denethor,
    pippin.name.lower(): pippin,
    bolg.name.lower(): bolg,
    azog.name.lower(): azog,
    bombadil.name.lower(): bombadil,
    frodo.name.lower(): frodo,
    sam.name.lower(): sam,
    cotton.name.lower(): cotton,
    elrond.name.lower(): elrond,
    cirdan.name.lower(): cirdan,
    saruman.name.lower(): saruman,
    lurtz.name.lower(): lurtz,
    nazgul.name.lower(): nazgul,
    angmar.name.lower(): angmar,
    theoden.name.lower(): theoden,
    eomer.name.lower(): eomer,
    eowyn.name.lower(): eowyn,
    merry.name.lower(): merry,
    thranduil.name.lower(): thranduil,
    legolas.name.lower(): legolas,
    galadriel.name.lower(): galadriel,
    celeborn.name.lower(): celeborn,

    bilbo.name.lower(): bilbo,
    bard.name.lower(): bard,
    thorin.name.lower(): thorin,
    dwalin.name.lower(): dwalin,
    balin.name.lower(): balin,
    fili.name.lower(): fili,
    kili.name.lower(): kili,
    dori.name.lower(): dori,
    ori.name.lower(): ori,
    nori.name.lower(): nori,
    oin.name.lower(): oin,
    gloin.name.lower(): gloin,
    bifur.name.lower(): bifur,
    bofur.name.lower(): bofur,
    bombur.name.lower(): bombur,
}

UnitDictionary = {
    eagle.name.lower(): eagle,
    dunland_archers.name.lower(): dunland_archers,
    dunlendings.name.lower(): dunlendings,
    beorning_archers.name.lower(): beorning_archers,
    beorning_infantry.name.lower(): beorning_infantry,
    skin_changers.name.lower(): skin_changers,
    corsair_archers.name.lower(): corsair_archers,
    pirates.name.lower(): pirates,
    'corsairs of umbar': pirates,
    'corsairs': pirates,
    arnor_rangers.name.lower(): arnor_rangers,
    dunedain_spearmen.name.lower(): dunedain_spearmen,
    mounted_dunedain.name.lower(): mounted_dunedain,
    rangers.name.lower(): rangers,
    dwarven_archers.name.lower(): dwarven_archers,
    dwarven_spearmen.name.lower(): dwarven_spearmen,
    dwarven_veterans.name.lower(): dwarven_veterans,
    dragon_veterans.name.lower(): dragon_veterans,
    watchmen.name.lower(): watchmen,
    easterling_archers.name.lower(): easterling_archers,
    easterling_infantry.name.lower(): easterling_infantry,
    lancers.name.lower(): lancers,
    variags.name.lower(): variags,
    'variags': variags,
    onodrim.name.lower(): onodrim,
    huorns.name.lower(): huorns,
    gondorians.name.lower(): gondorians,
    gondorian_archers.name.lower(): gondorian_archers,
    ithilien_rangers.name.lower(): ithilien_rangers,
    knights.name.lower(): knights,
    'knights': knights,
    tower_guard.name.lower(): tower_guard,
    defilers.name.lower(): defilers,
    gundabad_archers.name.lower(): gundabad_archers,
    snaga.name.lower(): snaga,
    wargs.name.lower(): wargs,
    hobbits.name.lower(): hobbits,
    hobbit_archers.name.lower(): hobbit_archers,
    tooks.name.lower(): tooks,
    haradrim.name.lower(): haradrim,
    harad_archers.name.lower(): harad_archers,
    mumak.name.lower(): mumak,
    southrons.name.lower(): southrons,
    troll_men.name.lower(): troll_men,
    'troll men': troll_men,
    gondolin_knights.name.lower(): gondolin_knights,
    mithlond_sentries.name.lower(): mithlond_sentries,
    noldorim.name.lower(): noldorim,
    noldor_archers.name.lower(): noldor_archers,
    orcs.name.lower(): orcs,
    uruk_archers.name.lower(): uruk_archers,
    uruk_hai.name.lower(): uruk_hai,
    warg_riders.name.lower(): warg_riders,
    olog_hai.name.lower(): olog_hai,
    troll.name.lower(): troll,
    uruk.name.lower(): uruk,
    orc_archers.name.lower(): orc_archers,
    riders.name.lower(): riders,
    'riders': riders,
    rohirric_archers.name.lower(): rohirric_archers,
    rohirrim.name.lower(): rohirrim,
    royal_guard.name.lower(): royal_guard,
    'royal guard': royal_guard,
    mirkwood_guards.name.lower(): mirkwood_guards,
    mirkwood_infantry.name.lower(): mirkwood_infantry,
    silvan_archers.name.lower(): silvan_archers,
    silvan_lancers.name.lower(): silvan_lancers,
    sindar_lancers.name.lower(): sindar_lancers,
    lorien_archers.name.lower(): lorien_archers,
    lorien_infantry.name.lower(): lorien_infantry,
    lorien_spearmen.name.lower(): lorien_spearmen,
}
