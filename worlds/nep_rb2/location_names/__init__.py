import typing
from ..LocationData import LocationData

from .arfoires_factory import *
from .atari_marsh_depths import *
from .atari_marsh import *
from .darkness_60 import *
from .endless_zone import *
from .gamindustri_graveyard import *
from .gapain_field import *
from .graveyard_depths import *
from .graveyard_oblivion import *
from .hellfire_hollow import *
from .icicle_pathway import *
from .infinite_corridor import *
from .iris_field import *
from .junk_box import *
from .lan_castle_depths import *
from .lan_castle_underground import *
from .lan_castle import *
from .lost_ruins import *
from .lowee_global_expo_east import *
from .lowee_global_expo_west import *
from .midcompany import *
from .panan_jungle import *
from .powerlevel_island import *
from .rebeat_resort import *
from .septent_resort import *
from .severed_dimension_depths import *
from .severed_dimension import *
from .sublie_road import *
from .trinity_marsh import *
from .underverse_depths import *
from .underverse import *
from .virtua_forest_depths import *
from .virtua_forest import *
from .world_labyrinth_1st_floor import *
from .world_labyrinth_2nd_floor import *

goalLocation: typing.List[LocationData] = (
    GraveyardGoal,
)

gathers: typing.List[LocationData] = (
    ArfoiresFactory,
    AtariMarshDepths,
    AtariMarsh,
    Darkness60,
    EndlessZone,
    GamindustriGraveyard,
    GapainField,
    GraveyardDepths,
    HellfireHollow,
    IciclePathway,
    InfiniteCorridor,
    IrisField,
    JunkBox,
    LANCastleDepths,
    LANCastleUnderground,
    LANCastle,
    LostRuins,
    LoweeGlobalExpoEast,
    LoweeGlobalExpoWest,
    Midcompany,
    PananJungle,
    PowerlevelIsland,
    RebeatResort,
    SeptentResort,
    SeveredDimension,
    SeveredDimensionDepths,
    SublieRoad,
    TrinityMarsh,
    Underverse,
    UnderverseDepths,
    VirtuaForestDepths,
    VirtuaForest,
    WorldLabyrinth1st,
    WorldLabyrinth2nd,
)

treasures: typing.List[LocationData] = (
    ArfoiresFactoryTreasures,
    AtariMarshDepthsTreasures,
    AtariMarshTreasures,
    Darkness60Treasures,
    EndlessZoneTreasures,
    GamindustriGraveyardTreasures,
    GapainFieldTreasures,
    GraveyardDepthsTreasures,
    HellfireHollowTreasures,
    IciclePathwayTreasures,
    InfiniteCorridorTreasures,
    IrisFieldTreasures,
    JunkBoxTreasures,
    LANCastleDepthsTreasures,
    LANCastleUndergroundTreasures,
    LANCastleTreasures,
    LostRuinsTreasures,
    LoweeGlobalExpoEastTreasures,
    LoweeGlobalExpoWestTreasures,
    MidcompanyTreasures,
    PananJungleTreasures,
    PowerlevelIslandTreasures,
    RebeatResortTreasures,
    SeptentResortTreasures,
    SeveredDimensionDepthsTreasures,
    SeveredDimensionTreasures,
    SublieRoadTreasures,
    TrinityMarshTreasures,
    UnderverseDepthsTreasures,
    UnderverseTreasures,
    VirtuaForestDepthsTreasures,
    VirtuaForestTreasures,
    WorldLabyrinth1stTreasures,
    WorldLabyrinth2ndTreasures,
)

enemies: typing.List[LocationData] = (
    ArfoiresFactoryEnemies,
    AtariMarshDepthsEnemies,
    AtariMarshEnemies,
    Darkness60Enemies,
    EndlessZoneEnemies,
    GamindustriGraveyardEnemies,
    GapainFieldEnemies,
    GraveyardDepthsEnemies,
    HellfireHollowEnemies,
    IciclePathwayEnemies,
    InfiniteCorridorEnemies,
    IrisFieldEnemies,
    JunkBoxEnemies,
    LANCastleDepthsEnemies,
    LANCastleUndergroundEnemies,
    LANCastleEnemies,
    LostRuinsEnemies,
    LoweeGlobalExpoEastEnemies,
    LoweeGlobalExpoWestEnemies,
    MidcompanyEnemies,
    PananJungleEnemies,
    PowerlevelIslandEnemies,
    RebeatResortEnemies,
    SeptentResortEnemies,
    SeveredDimensionDepthsEnemies,
    SeveredDimensionEnemies,
    SublieRoadEnemies,
    TrinityMarshEnemies,
    UnderverseDepthsEnemies,
    UnderverseEnemies,
    VirtuaForestDepthsEnemies,
    VirtuaForestEnemies,
    WorldLabyrinth1stEnemies,
    WorldLabyrinth2ndEnemies,
)

levels: typing.List[LocationData] = (
    LocationData("Arfoire's Factory","Grinding",50,"Level"),
    LocationData("Atari Marsh Depths","Grinding",30,"Level"),
    LocationData("Atari Marsh","Grinding",30,"Level"),
    LocationData("Darkness 60","Grinding",10,"Level"),
    LocationData("Endless Zone","Grinding",10,"Level"),
    LocationData("Gamindustri Graveyard","Grinding",40,"Level"),
    LocationData("Graveyard Depths","Grinding",60,"Level"),
    LocationData("Gapain Field","Grinding",30,"Level"),
    LocationData("Hellfire Hollow","Grinding",80,"Level"),
    LocationData("Icicle Pathway","Grinding",70,"Level"),
    LocationData("Infinite Corridor","Grinding",70,"Level"),
    LocationData("Iris Field","Grinding",40,"Level"),
    LocationData("Junk Box","Grinding",70,"Level"),
    LocationData("LAN Castle Depths","Grinding",40,"Level"),
    LocationData("LAN Castle","Grinding",40,"Level"),
    LocationData("LAN Castle - Depths","Grinding",40,"Level"),
    LocationData("Lost Ruins","Grinding",80,"Level"),
    LocationData("Lowee Global Expo - East","Grinding",20,"Level"),
    LocationData("Lowee Global Expo - West","Grinding",20,"Level"),
    LocationData("Midcompany","Grinding",10,"Level"),
    LocationData("Panan Jungle","Grinding",80,"Level"),
    LocationData("Powerlevel Island","Grinding",30,"Level"),
    LocationData("Rebeat Resort","Grinding",10,"Level"),
    LocationData("Septent Resort","Grinding",10,"Level"),
    LocationData("Severed Dimension Depths","Grinding",30,"Level"),
    LocationData("Severed Dimension","Grinding",30,"Level"),
    LocationData("Sublie Road","Grinding",70,"Level"),
    LocationData("Trinity Marsh","Grinding",80,"Level"),
    LocationData("Underverse Depths","Grinding",30,"Level"),
    LocationData("Underverse","Grinding",30,"Level"),
    LocationData("Virtua Forest - Depths","Grinding",10,"Level"),
    LocationData("Virtua Forest","Grinding",10,"Level"),
    LocationData("World Labyrinth - 1st Floor","Grinding",20,"Level"),
    LocationData("World Labyrinth - 2nd Floor","Grinding",20,"Level"),
)
