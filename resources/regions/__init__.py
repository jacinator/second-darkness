from templates import regions
from resources import nations, units

from . import names


anfalas = regions.Region(
    name=names.anfalas,
    occupants=nations.gondor,
    resources=2,
    neighbors=[
        names.ras_morthil_andrast,
        names.pinnath_gelin,
    ],
    army={
        units.gondorians: 2,
    },
)

anorien = regions.Region(
    name=names.anorien,
    occupants=nations.gondor,
    resources=4,
    neighbors=[
        names.eastfold,
        names.east_emnet,
        names.nindalf,
        names.north_ithilien,
        names.pelennor,
    ],
    army={
        units.gondorians: 4,
        units.marksmen: 2,
        units.rangers: 3,
    },
)

barad_dur = regions.Region(
    name=names.barad_dur,
    occupants=nations.mordor,
    resources=10,
    developed=5,
    neighbors=[
        names.plateau_gorgoroth,
    ],
    army={
        units.orcs: 5,
    },
)

barrow_downs = regions.Region(
    name=names.barrow_downs,
    occupants=nations.arnor,
    neighbors=[
        names.shire,
        names.bree,
        names.south_downs,
    ],
    army={
    },
)

belfalas = regions.Region(
    name=names.belfalas,
    occupants=nations.gondor,
    neighbors=[
        names.dol_amroth,
        names.dor_en_ernil,
    ],
    resources=2,
    army={
        units.knights: 4,
        units.marksmen: 2,
    },
)

bree = regions.Region(
    name=names.bree,
    occupants=nations.arnor,
    neighbors=[
        names.shire,
        names.north_downs,
        names.south_downs,
        names.barrow_downs,
        names.weather_hills,
    ],
    resources=5,
    army={
        units.spearmen: 3,
    },
    developed=1,
)

brown_lands = regions.Region(
    name=names.brown_lands,
    occupants=nations.rohan,
    neighbors=[
        names.wold,
        names.emyn_muil,
        names.dol_guldur,
    ],
)

calembel = regions.Region(
    name=names.calembel,
    occupants=nations.gondor,
    neighbors=[
        names.lamedon,
    ],
    resources=2,
    army={
        units.gondorians: 4,
    },
    developed=2,
)

caras_galadhon = regions.Region(
    name=names.caras_galadhon,
    occupants=nations.lorien,
    resources=6,
    developed=4,
    neighbors=[
        names.lorien,
    ],
    army={
        units.galadhrim: 4,
        units.sentries: 5,
    },
)

carn_dum = regions.Region(
    name=names.carn_dum,
    occupants=nations.angmar,
    neighbors=[
        names.ettenmoors,
        names.north_downs,
        names.mount_gundabad,
        names.misty_mountains,
        names.northern_waste,
    ],
    resources=3,
    army={
        units.uruk: 3,
        units.orcs: 2,
    },
    developed=3,
)

carrock = regions.Region(
    name=names.carrock,
    resources=8,
    occupants=nations.anduin_valley,
    army={
        units.berserkers: 3,
        units.sentries: 2,
    },
    developed=1,
    neighbors=[
        names.mount_gundabad,
        names.misty_mountains,
        names.loeg_ningloron,
        names.woodland_realm,
        names.mirkwood,
    ],
)

dale = regions.Region(
    name=names.dale,
    occupants=nations.erebor,
    neighbors=[
        names.erebor,
        names.lake_town,
    ],
    resources=5,
    army={
        units.watchmen: 2,
        units.dragon_hunters: 3,
    },
)

dead_marshes = regions.Region(
    name=names.dead_marshes,
    occupants=nations.mordor,
    neighbors=[
        names.nindalf,
        names.noman_lands,
        names.emyn_muil,
        names.east_bight,
    ],
)

dol_amroth = regions.Region(
    name=names.dol_amroth,
    occupants=nations.gondor,
    neighbors=[
        names.lamedon,
        names.belfalas,
    ],
    army={
        units.gondorians: 4,
        units.knights: 3,
        units.marksmen: 2,
    },
    developed=4,
)

dol_guldur = regions.Region(
    name=names.dol_guldur,
    occupants=nations.mordor,
    resources=7,
    neighbors=[
        names.mirkwood,
        names.east_bight,
        names.loeg_ningloron,
        names.lorien,
        names.parth_celebrant,
        names.brown_lands,
    ],
    army={
        units.orcs: 6,
        units.trolls: 1,
        units.raiders: 3,
    },
    developed=5,
)

dor_en_ernil = regions.Region(
    name=names.dor_en_ernil,
    occupants=nations.gondor,
    neighbors=[
        names.lebennin,
        names.belfalas,
    ],
    resources=3,
    army={
        units.gondorians: 1,
        units.knights: 3,
        units.marksmen: 2,
    },
)

dorwinion = regions.Region(
    name=names.dorwinion,
    occupants=nations.rhun,
    resources=5,
    neighbors=[
        names.east_bight,
        names.iron_hills,
        names.lake_town,
        names.rhun,
        names.erebor,
    ],
    army={
        units.spearmen: 3,
        units.marksmen: 2,
    },
)

druwaith_iaur = regions.Region(
    name=names.druwaith_iaur,
    occupants=nations.dunland,
    neighbors=[
        names.dunland,
        names.pinnath_gelin,
        names.ras_morthil_andrast,
        names.gap_rohan,
        names.dunland,
    ],
    resources=3,
    army={
        units.spearmen: 6,
    },
)

dunharrow = regions.Region(
    name=names.dunharrow,
    occupants=nations.rohan,
    neighbors=[
        names.eastfold,
    ],
    resources=2,
    army={
        units.rohirrim: 3,
        units.riders_rohan: 7,
    },
    developed=2,
)

dunland = regions.Region(
    name=names.dunland,
    resources=2,
    occupants=nations.dunland,
    neighbors=[
        names.eregion,
        names.isengard,
        names.methedras,
        names.south_downs,
        names.druwaith_iaur,
        names.sarn_ford,
        names.tharbad,
        names.gap_rohan,
    ],
)

east_bight = regions.Region(
    name=names.east_bight,
    occupants=nations.rhun,
    resources=3,
    neighbors=[
        names.dol_guldur,
        names.dorwinion,
        names.lake_town,
        names.mirkwood,
        names.dead_marshes,
        names.emyn_muil,
    ],
)

east_emnet = regions.Region(
    name=names.east_emnet,
    occupants=nations.rohan,
    neighbors=[
        names.west_emnet,
        names.eastfold,
        names.emyn_muil,
        names.anorien,
        names.wold,
    ],
    resources=3,
    army={
        units.rohirrim: 4,
        units.riders_rohan: 2,
    },
)

eastfold = regions.Region(
    name=names.eastfold,
    occupants=nations.rohan,
    neighbors=[
        names.west_emnet,
        names.east_emnet,
        names.anorien,
        names.dunharrow,
    ],
    resources=1,
)

edoras = regions.Region(
    name=names.edoras,
    occupants=nations.rohan,
    neighbors=[
        names.westfold,
    ],
    resources=2,
    army={
        units.riders_rohan: 5,
        units.rohirrim: 4,
        units.guardsmen: 4,
    },
    developed=3,
)

emyn_beraid = regions.Region(
    name=names.emyn_beraid,
    occupants=nations.mithlond,
    neighbors=[
        names.grey_havens,
        names.ered_luin,
        names.shire,
    ],
    resources=2,
    army={
        units.arda_guard: 3,
    },
)

emyn_muil = regions.Region(
    name=names.emyn_muil,
    occupants=nations.rohan,
    neighbors=[
        names.nindalf,
        names.dead_marshes,
        names.brown_lands,
        names.east_bight,
        names.east_emnet,
    ],
)

emyn_nu_fuin = regions.Region(
    name=names.emyn_nu_fuin,
    occupants=nations.greenwood,
    neighbors=[
        names.woodland_realm,
        names.mirkwood,
    ],
    resources=3,
    army={
        units.arda_guard: 3,
        units.sentries: 2,
    },
)

emyn_uial = regions.Region(
    name=names.emyn_uial,
    occupants=nations.arnor,
    neighbors=[
        names.grey_havens,
        names.shire,
        names.north_downs,
    ],
    army={
        units.rangers: 3,
        units.dunedain: 1,
    },
)

entwade = regions.Region(
    name=names.entwade,
    occupants=nations.rohan,
    neighbors=[
        names.west_emnet,
    ],
    resources=2,
    army={
        units.rohirrim: 4,
        units.riders_rohan: 1,
    },
    developed=1,
)

erebor = regions.Region(
    name=names.erebor,
    resources=12,
    occupants=nations.erebor,
    neighbors=[
        names.withered_heath,
        names.woodland_realm,
        names.iron_hills,
        names.lake_town,
        names.dale,
        names.dorwinion,
    ],
    army={
        units.veterans: 8,
        units.axemen: 3,
    },
    developed=4,
)

ered_luin = regions.Region(
    name=names.ered_luin,
    occupants=nations.ered_luin,
    neighbors=[
        names.harlindon,
        names.forlindon,
        names.grey_havens,
        names.emyn_beraid,
        names.sarn_ford,
    ],
    resources=5,
    army={
        units.axemen: 5,
        units.engineers: 4,
    },
)

ered_mithrin = regions.Region(
    name=names.ered_mithrin,
    occupants=nations.angmar,
    neighbors=[
        names.northern_waste,
        names.misty_mountains,
        names.mount_gundabad,
        names.woodland_realm,
        names.withered_heath,
    ],
    resources=2,
    army={
        units.orcs: 5,
        units.wargs: 3,
    },
)

eregion = regions.Region(
    name=names.eregion,
    resources=2,
    occupants=nations.dunland,
    neighbors=[
        names.rivendell,
        names.dunland,
        names.mines_moria,
        names.south_downs,
    ],
)

ettenmoors = regions.Region(
    name=names.ettenmoors,
    occupants=nations.angmar,
    neighbors=[
        names.weather_hills,
        names.north_downs,
        names.carn_dum,
        names.misty_mountains,
        names.rhudaur,
    ],
    army={
        units.orcs: 2,
        units.wargs: 2,
    },
)

fangorn = regions.Region(
    name=names.fangorn,
    resources=6,
    occupants=nations.lorien,
    neighbors=[
        names.parth_celebrant,
        names.methedras,
        names.isengard,
        names.wold,
        names.west_emnet,
        names.wellinghall,
    ],
)

far_harad = regions.Region(
    name=names.far_harad,
    occupants=nations.harad,
    neighbors=[
        names.khand,
        names.near_harad,
        names.haradwaith,
    ],
    resources=3,
    army={
        units.haradrim: 3,
        units.mumakil: 1,
        units.southrons: 4,
    },
)

forlindon = regions.Region(
    name=names.forlindon,
    occupants=nations.mithlond,
    neighbors=[
        names.ered_luin,
    ],
    army={
        units.arda_guard: 2,
    },
)

fornost = regions.Region(
    name=names.fornost,
    occupants=nations.arnor,
    neighbors=[
        names.north_downs,
    ],
    army={
        units.rangers: 3,
        units.dunedain: 1,
        units.knights: 2,
    },
    developed=3,
)

gabilgathod = regions.Region(
    name=names.gabilgathod,
    occupants=nations.erebor,
    resources=5,
    developed=3,
    neighbors=[
        names.iron_hills,
    ],
    army={
        units.axemen: 4,
        units.engineers: 3,
    },
)

gap_rohan = regions.Region(
    name=names.gap_rohan,
    occupants=nations.isengard,
    neighbors=[
        names.dunland,
        names.druwaith_iaur,
        names.west_emnet,
        names.isengard,
    ],
    resources=2,
    army={
        units.wargs: 1,
        units.uruk_hai: 10,
    },
)

gladden_fields = regions.Region(
    name=names.loeg_ningloron,
    resources=3,
    occupants=nations.anduin_valley,
    neighbors=[
        names.carrock,
        names.mines_moria,
        names.lorien,
        names.dol_guldur,
        names.mirkwood,
    ],
    army={
        units.berserkers: 2,
        units.spearmen: 2,
    },
)

goblin_town = regions.Region(
    name=names.goblin_town,
    occupants=nations.angmar,
    neighbors=[
        names.misty_mountains,
    ],
    resources=3,
    army={
        units.wargs: 3,
        units.uruk: 2,
        units.raiders: 2,
    },
    developed=2,
)

grey_havens = regions.Region(
    name=names.grey_havens,
    occupants=nations.mithlond,
    neighbors=[
        names.ered_luin,
        names.emyn_beraid,
        names.emyn_uial,
    ],
    resources=8,
    army={
        units.arda_guard: 7,
        units.knights: 3,
    },
    developed=4,
)

haradwaith = regions.Region(
    name=names.haradwaith,
    occupants=nations.harad,
    neighbors=[
        names.near_harad,
        names.far_harad,
        names.umbar,
        names.hyarmendacil,
    ],
    resources=4,
    army={
        units.southrons: 3,
        units.haradrim: 7,
        units.marksmen: 5,
        units.mumakil: 3,
    },
)

harlindon = regions.Region(
    name=names.harlindon,
    occupants=nations.mithlond,
    neighbors=[
        names.ered_luin,
    ],
    army={
        units.arda_guard: 2,
    },
)

harondor = regions.Region(
    name=names.harondor,
    occupants=nations.harad,
    neighbors=[
        names.lebennin,
        names.south_ithilien,
        names.near_harad,
    ],
    resources=3,
    army={
        units.haradrim: 4,
        units.mumakil: 1,
        units.southrons: 2,
    },
)

hobbiton = regions.Region(
    name=names.hobbiton,
    occupants=nations.arnor,
    neighbors=[
        names.shire,
    ],
    resources=6,
    army={
        units.spearmen: 6,
        units.dunedain: 3,
        units.rangers: 3,
    },
    developed=2,
)

hyarmendacil = regions.Region(
    name=names.hyarmendacil,
    occupants=nations.harad,
    resources=4,
    developed=4,
    neighbors=[
        names.haradwaith,
    ],
    army={
        units.haradrim: 5,
    },
)

iron_hills = regions.Region(
    name=names.iron_hills,
    resources=6,
    occupants=nations.erebor,
    neighbors=[
        names.withered_heath,
        names.erebor,
        names.lake_town,
        names.rhun,
        names.dorwinion,
        names.gabilgathod,
    ],
)

isengard = regions.Region(
    name=names.isengard,
    resources=8,
    occupants=nations.isengard,
    neighbors=[
        names.dunland,
        names.fangorn,
        names.methedras,
        names.gap_rohan,
    ],
    army={
        units.uruk_hai: 10,
        units.raiders: 5,
        units.wargs: 3,
        units.orcs: 3,
    },
    developed=5,
)

khand = regions.Region(
    name=names.khand,
    occupants=nations.rhun,
    neighbors=[
        names.near_harad,
        names.far_harad,
        names.rhun,
        names.lithlad,
    ],
    resources=4,
    army={
        units.variags: 6,
        units.spearmen: 2,
    },
)

khazad_dum = regions.Region(
    name=names.khazad_dum,
    occupants=nations.angmar,
    neighbors=[
        names.mines_moria,
    ],
    developed=4,
    army={
        units.raiders: 4,
        units.uruk: 4,
        units.orcs: 3,
    },
    resources=4,
)

lake_town = regions.Region(
    name=names.lake_town,
    occupants=nations.erebor,
    neighbors=[
        names.erebor,
        names.dale,
        names.woodland_realm,
        names.iron_hills,
        names.east_bight,
        names.dorwinion,
    ],
    army={
        units.watchmen: 2,
        units.dragon_hunters: 3,
    },
    developed=2,
)

lamedon = regions.Region(
    name=names.lamedon,
    occupants=nations.gondor,
    resources=1,
    neighbors=[
        names.pinnath_gelin,
        names.dol_amroth,
        names.lebennin,
        names.calembel,
    ],
)

lebennin = regions.Region(
    name=names.lebennin,
    occupants=nations.gondor,
    neighbors=[
        names.lamedon,
        names.dor_en_ernil,
        names.harondor,
        names.south_ithilien,
        names.pelargir,
    ],
    resources=2,
)

lithlad = regions.Region(
    name=names.lithlad,
    occupants=nations.mordor,
    neighbors=[
        names.khand,
        names.nurn,
        names.plateau_gorgoroth,
    ],
    resources=3,
    army={
        units.orcs: 5,
    },
)

lorien = regions.Region(
    name=names.lorien,
    resources=4,
    occupants=nations.lorien,
    neighbors=[
        names.parth_celebrant,
        names.loeg_ningloron,
        names.mines_moria,
        names.dol_guldur,
        names.caras_galadhon,
    ],
)

methedras = regions.Region(
    name=names.methedras,
    resources=2,
    occupants=nations.isengard,
    neighbors=[
        names.fangorn,
        names.isengard,
        names.dunland,
        names.parth_celebrant,
        names.mines_moria,
    ],
    army={
        units.wargs: 4,
        units.orcs: 4,
    },
)

minas_tirith = regions.Region(
    name=names.minas_tirith,
    occupants=nations.gondor,
    neighbors=[
        names.pelennor,
    ],
    resources=2,
    army={
        units.knights: 1,
        units.gondorians: 5,
        units.tower_guard: 3,
        units.rangers: 2,
    },
    developed=5,
)

minas_morgul = regions.Region(
    name=names.minas_morgul,
    occupants=nations.mordor,
    resources=3,
    developed=4,
    neighbors=[
        names.morgul_vale,
    ],
    army={
        units.orcs: 4,
    },
)

mines_moria = regions.Region(
    name=names.mines_moria,
    occupants=nations.angmar,
    resources=8,
    neighbors=[
        names.eregion,
        names.misty_mountains,
        names.loeg_ningloron,
        names.lorien,
        names.methedras,
        names.khazad_dum,
        names.rivendell,
    ],
)

mirkwood = regions.Region(
    name=names.mirkwood,
    occupants=nations.mordor,
    resources=4,
    neighbors=[
        names.carrock,
        names.emyn_nu_fuin,
        names.loeg_ningloron,
        names.dol_guldur,
        names.east_bight,
        names.woodland_realm,
    ],
)

misty_mountains = regions.Region(
    name=names.misty_mountains,
    occupants=nations.angmar,
    neighbors=[
        names.ered_mithrin,
        names.carn_dum,
        names.ettenmoors,
        names.rhudaur,
        names.carrock,
        names.mines_moria,
        names.rivendell,
        names.mount_gundabad,
        names.goblin_town,
    ],
    resources=4,
)

morgul_vale = regions.Region(
    name=names.morgul_vale,
    occupants=nations.mordor,
    neighbors=[
        names.north_ithilien,
        names.plateau_gorgoroth,
        names.minas_morgul,
    ],
    resources=2,
    army={
        units.orcs: 8,
        units.raiders: 4,
    },
)

mount_gundabad = regions.Region(
    name=names.mount_gundabad,
    occupants=nations.angmar,
    neighbors=[
        names.carn_dum,
        names.ered_mithrin,
        names.misty_mountains,
        names.carrock,
        names.northern_waste,
    ],
    resources=4,
    army={
        units.orcs: 5,
        units.raiders: 3,
        units.wargs: 4,
    },
    developed=4,
)

near_harad = regions.Region(
    name=names.near_harad,
    occupants=nations.harad,
    neighbors=[
        names.khand,
        names.far_harad,
        names.haradwaith,
        names.umbar,
        names.harondor,
    ],
    resources=3,
    army={
        units.haradrim: 8,
        units.mumakil: 1,
    },
)

nindalf = regions.Region(
    name=names.nindalf,
    occupants=nations.mordor,
    neighbors=[
        names.anorien,
        names.emyn_muil,
        names.noman_lands,
        names.dead_marshes,
    ],
)

noman_lands = regions.Region(
    name=names.noman_lands,
    occupants=nations.mordor,
    neighbors=[
        names.nindalf,
        names.dead_marshes,
        names.north_ithilien,
        names.udun,
    ],
    army={
        units.orcs: 5,
    },
)

north_downs = regions.Region(
    name=names.north_downs,
    occupants=nations.arnor,
    neighbors=[
        names.shire,
        names.weather_hills,
        names.ettenmoors,
        names.emyn_uial,
        names.carn_dum,
        names.fornost,
        names.bree,
    ],
)

north_ithilien = regions.Region(
    name=names.north_ithilien,
    occupants=nations.mordor,
    neighbors=[
        names.noman_lands,
        names.anorien,
        names.pelennor,
        names.morgul_vale,
    ],
    resources=3,
    army={
        units.orcs: 6,
        units.trolls: 3,
    },
)

northern_waste = regions.Region(
    name=names.northern_waste,
    occupants=nations.angmar,
    neighbors=[
        names.carn_dum,
        names.mount_gundabad,
        names.ered_mithrin,
    ],
    resources=2,
    army={
        units.orcs: 8,
    },
)

nurn = regions.Region(
    name=names.nurn,
    occupants=nations.mordor,
    neighbors=[
        names.lithlad,
        names.plateau_gorgoroth,
    ],
    resources=3,
    army={
        units.orcs: 5,
        units.raiders: 1,
    },
)

parth_celebrant = regions.Region(
    name=names.parth_celebrant,
    resources=5,
    occupants=nations.lorien,
    neighbors=[
        names.lorien,
        names.fangorn,
        names.methedras,
        names.dol_guldur,
        names.wold,
    ],
    army={
        units.lancers: 3,
    },
)

pelargir = regions.Region(
    name=names.pelargir,
    occupants=nations.gondor,
    neighbors=[
        names.lebennin,
    ],
    resources=2,
    army={
        units.gondorians: 2,
        units.knights: 2,
        units.marksmen: 4,
        units.rangers: 2,
    },
    developed=3,
)

pelennor = regions.Region(
    name=names.pelennor,
    occupants=nations.gondor,
    neighbors=[
        names.north_ithilien,
        names.south_ithilien,
        names.anorien,
        names.minas_tirith,
    ],
    resources=3,
)

pinnath_gelin = regions.Region(
    name=names.pinnath_gelin,
    occupants=nations.gondor,
    resources=2,
    neighbors=[
        names.anfalas,
        names.druwaith_iaur,
        names.lamedon,
    ],
    army={
        units.gondorians: 3,
    },
)

plateau_gorgoroth = regions.Region(
    name=names.plateau_gorgoroth,
    occupants=nations.mordor,
    neighbors=[
        names.udun,
        names.morgul_vale,
        names.nurn,
        names.lithlad,
        names.barad_dur,
    ],
    resources=1,
    army={
        units.orcs: 4,
        units.raiders: 2,
    },
)

ras_morthil_andrast = regions.Region(
    name=names.ras_morthil_andrast,
    occupants=nations.gondor,
    neighbors=[
        names.anfalas,
        names.druwaith_iaur,
    ],
    army={
        units.gondorians: 2,
    },
)

rhudaur = regions.Region(
    name=names.rhudaur,
    occupants=nations.angmar,
    resources=2,
    neighbors=[
        names.ettenmoors,
        names.misty_mountains,
        names.rivendell,
        names.weather_hills,
    ],
    army={
        units.wargs: 2,
        units.orcs: 3,
    },
)

rhun = regions.Region(
    name=names.rhun,
    occupants=nations.rhun,
    resources=4,
    neighbors=[
        names.dorwinion,
        names.iron_hills,
        names.khand,
        names.talath_rhunen,
    ],
)

rivendell = regions.Region(
    name=names.rivendell,
    resources=9,
    occupants=nations.rivendell,
    neighbors=[
        names.rhudaur,
        names.mines_moria,
        names.eregion,
        names.misty_mountains,
        names.south_downs,
    ],
    army={
        units.arda_guard: 4,
        units.knights: 5,
    },
    developed=4,
)

sarn_ford = regions.Region(
    name=names.sarn_ford,
    occupants=nations.arnor,
    neighbors=[
        names.shire,
        names.ered_luin,
        names.south_downs,
        names.dunland,
    ],
    army={
        units.rangers: 3,
        units.dunedain: 1,
    },
)

shire = regions.Region(
    name=names.shire,
    occupants=nations.arnor,
    neighbors=[
        names.emyn_beraid,
        names.emyn_uial,
        names.north_downs,
        names.bree,
        names.sarn_ford,
        names.barrow_downs,
        names.hobbiton,
    ],
    resources=4,
)

south_downs = regions.Region(
    name=names.south_downs,
    occupants=nations.arnor,
    neighbors=[
        names.sarn_ford,
        names.barrow_downs,
        names.weather_hills,
        names.bree,
        names.rivendell,
        names.dunland,
        names.eregion,
    ],
    army={
        units.rangers: 3,
        units.dunedain: 1,
    },
)

south_ithilien = regions.Region(
    name=names.south_ithilien,
    occupants=nations.gondor,
    neighbors=[
        names.lebennin,
        names.harondor,
        names.pelennor,
    ],
    resources=3,
    army={
        units.rangers: 6,
        units.gondorians: 5,
    },
)

talath_rhunen = regions.Region(
    name=names.talath_rhunen,
    occupants=nations.rhun,
    resources=2,
    developed=3,
    neighbors=[
        names.rhun,
    ],
    army={
        units.spearmen: 2,
        units.marksmen: 1,
    },
)

tharbad = regions.Region(
    name=names.tharbad,
    occupants=nations.dunland,
    resources=4,
    developed=2,
    neighbors=[
        names.dunland,
    ],
    army={
        units.spearmen: 5,
        units.raiders: 3,
    },
)

thranduils_caverns = regions.Region(
    name=names.thranduils_caverns,
    occupants=nations.greenwood,
    resources=4,
    developed=4,
    neighbors=[
        names.woodland_realm,
    ],
    army={
        units.arda_guard: 5,
        units.sentries: 5,
    },
)

udun = regions.Region(
    name=names.udun,
    occupants=nations.mordor,
    neighbors=[
        names.noman_lands,
        names.plateau_gorgoroth,
    ],
    army={
        units.trolls: 2,
        units.raiders: 5,
        units.orcs: 7,
    },
)

umbar = regions.Region(
    name=names.umbar,
    occupants=nations.umbar,
    neighbors=[
        names.haradwaith,
        names.near_harad,
    ],
    resources=6,
    army={
        units.corsairs: 7,
        units.raiders: 4,
    },
    developed=3,
)

weather_hills = regions.Region(
    name=names.weather_hills,
    occupants=nations.arnor,
    neighbors=[
        names.bree,
        names.south_downs,
        names.north_downs,
        names.ettenmoors,
        names.rhudaur,
    ],
    resources=3,
    army={
        units.rangers: 3,
        units.dunedain: 1,
    },
)

wellinghall = regions.Region(
    name=names.wellinghall,
    occupants=nations.lorien,
    resources=4,
    developed=2,
    neighbors=[
        names.fangorn,
    ],
    army={
        units.ents: 4,
    },
)

west_emnet = regions.Region(
    name=names.west_emnet,
    occupants=nations.rohan,
    neighbors=[
        names.east_emnet,
        names.entwade,
        names.fangorn,
        names.westfold,
        names.eastfold,
        names.gap_rohan,
    ],
    resources=1,
)

westfold = regions.Region(
    name=names.westfold,
    occupants=nations.rohan,
    neighbors=[
        names.edoras,
        names.west_emnet,
    ],
    resources=1,
)

withered_heath = regions.Region(
    name=names.withered_heath,
    resources=2,
    occupants=nations.angmar,
    neighbors=[
        names.ered_mithrin,
        names.woodland_realm,
        names.iron_hills,
        names.erebor,
    ],
    army={
        units.orcs: 7,
    },
)

wold = regions.Region(
    name=names.wold,
    occupants=nations.rohan,
    neighbors=[
        names.fangorn,
        names.east_emnet,
        names.parth_celebrant,
        names.brown_lands,
    ],
    army={
        units.riders_rohan: 4,
    },
)

woodland_realm = regions.Region(
    name=names.woodland_realm,
    occupants=nations.greenwood,
    neighbors=[
        names.emyn_nu_fuin,
        names.lake_town,
        names.erebor,
        names.withered_heath,
        names.carrock,
        names.ered_mithrin,
        names.mirkwood,
        names.thranduils_caverns,
    ],
)
