function Faction(name, adjective, resources = 150000) {
    this.name = name;
    this.adjective = adjective;
    this.resources = resources;
};

var Gondor = new Faction("Gondor", "Gondorian");
var Mordor = new Faction("Mordor", "Orcish");
var Elves = new Faction("the Elves", "Elven");
var Dwarves = new Faction("the Dwarves", "Dwarven");
var Harad = new Faction("Harad", "Haradrim");
var Isengard = new Faction("Isengard", "Isengard");

var factionList = new Array(
    Gondor,
    Mordor,
    Elves,
    Dwarves,
    Harad,
    Isengard
);

function Unit(name, strength, moral, cost, faction, imageUrl) {
    this.name = name;
    this.strength = strength;
    this.moral = moral;
    this.cost = cost;
    this.faction = faction;
    this.lives = 1;
    this.image = imageUrl;
};

function InfantryUnit(name, faction, imageUrl = null, cost = 10) {
    this.name = name;
    this.faction = faction;
    this.cost = cost;
    this.moral = 90;
    this.strength = 100;
    this.type = "infantry";
    this.image = imageUrl;
};
InfantryUnit.prototype = new Unit();

function HeavyUnit(name, faction, imageUrl = null, cost = 20) {
    this.name = name;
    this.faction = faction;
    this.cost = cost;
    this.moral = 100;
    this.strength = 70;
    this.type = "heavy";
    this.image = imageUrl;
};
HeavyUnit.prototype = new Unit();

function ArcherUnit(name, faction, imageUrl = null, cost = 20) {
    this.name = name;
    this.faction = faction;
    this.cost = cost;
    this.moral = 90;
    this.strength = 80;
    this.type = "archer";
    this.image = imageUrl;
};
ArcherUnit.prototype = new Unit();

function MountedUnit(name, faction, imageUrl = null, cost = 40) {
    this.name = name;
    this.faction = faction;
    this.cost = cost;
    this.moral = 100;
    this.strength = 60;
    this.type = "cavalry";
    this.image = imageUrl;
};
MountedUnit.prototype = new Unit();

//Gondorian Units
var gondorians = new InfantryUnit("Soldiers of Gondor", Gondor, "../images/unit_images/soldiers_gondor.jpg");
var towerGuard = new HeavyUnit("Guard of the Citadel", Gondor, "../images/unit_images/tower_guard.jpg");
var gondorArchers = new ArcherUnit("Gondorian Archers", Gondor, "../images/unit_images/gondor_archers.jpg");
var rohirrim = new MountedUnit("Rohirrim", Gondor, "../images/unit_images/rohirrim.jpg");
var swanKnights = new MountedUnit("Knights of Dol Amroth", Gondor, "../images/unit_images/knights_amroth.jpg");

//Mordor Units
var orcs = new InfantryUnit("Mordor Orcs", Mordor, "../images/unit_images/mordor_orcs.jpg");
var uruks = new HeavyUnit("Mordor Uruks", Mordor, "../images/unit_images/mordor_uruk.jpg");
var mordorArchers = new ArcherUnit("Mordor Archers", Mordor);

//Elves Units
var mithlondSentries = new InfantryUnit("Mithlond Sentries", Elves, "../images/unit_images/noldor.jpg");
var galadhrim = new ArcherUnit("Galadhrim", Elves, "../images/unit_images/galadhrim.jpg");
var woodlandGuards = new ArcherUnit("Greenwood Guards", Elves, "../images/unit_images/silvan_elves.jpg");
var rivendellLancers = new MountedUnit("Rivendell Lancers", Elves);

//Dwarves Units
var ereborGuards = new InfantryUnit("Erebor Guards", Dwarves, "../images/unit_images/dwarves.jpg");
var moriaVeterans = new InfantryUnit("Moria Veterans", Dwarves, "../images/unit_images/moria_dwarves.jpg");
var lakeMen = new ArcherUnit("Lake Men", Dwarves);

//Harad Units
var southrons = new InfantryUnit("Southrons", Harad);
var variags = new InfantryUnit("Variags of Khand", Harad);

//Isengard
var urukHai = new HeavyUnit("Uruk-hai", Isengard, "../images/unit_images/uruk_hai.jpg");
var urukHaiArcher = new ArcherUnit("Uruk-hai Archer", Isengard);
var wargRiders = new MountedUnit("Warg Riders", Isengard, "../images/unit_images/warg_riders.jpg");

var unitList = new Array(
    gondorians,
    towerGuard,
    gondorArchers,
    rohirrim,
    swanKnights,
    orcs,
    uruks,
    mordorArchers,
    mithlondSentries,
    galadhrim,
    woodlandGuards,
    rivendellLancers,
    ereborGuards,
    moriaVeterans,
    lakeMen,
    southrons,
    variags,
    urukHai,
    urukHaiArcher,
    wargRiders
);

function Province(name, territories = null) {
    this.name = name;
    this.territories = territories;
};

var provinceArnor = new Province("Arnor");
var provinceEnedwaith = new Province("Enedwaith");
var provinceWestGondor = new Province("Western Gondor");
var provinceForodwaith = new Province("Forodwaith");
var provinceMirkwood = new Province("Mirkwood");
var provinceRohan = new Province("Rohan");
var provinceEastGondor = new Province("Eastern Gondor");
var provinceMordor = new Province("Mordor");
var provinceHarad = new Province("Harad");
var provinceRhovanion = new Province("Rhovanion");
var provinceRhun = new Province("Rhun");

var provinceList = new Array(
    provinceArnor,
    provinceEastGondor,
    provinceEnedwaith,
    provinceForodwaith,
    provinceHarad,
    provinceMirkwood,
    provinceMordor,
    provinceRhovanion,
    provinceRhun,
    provinceRohan,
    provinceWestGondor
);

function Territory(name, province) {
    this.name = name;
    this.province = province;
};

var territoryRivendell = new Territory("Rivendell", provinceArnor);

var territoryList = new Array(
    territoryRivendell
);