import typing
from ..LocationData import LocationData

from arfoires_factory import *
from atari_marsh_depths import *
from atari_marsh import *
from darkness_60 import *
from endless_zone import *
from gapain_field import *
from hellfire_hollow import *
from icicle_pathway import *
from infinite_corridor import *
from iris_field import *
from junk_box import *
from lan_castle_depths import *
from lan_castle_underground import *
from lan_castle import *
from lost_ruins import *
from lowee_global_expo_east import *
from lowee_global_expo_west import *
from midcompany import *
from panan_jungle import *
from powerlevel_island import *
from rebeat_resort import *
from septent_resort import *
from severed_dimension_depths import *
from severed_dimension import *
from sublie_road import *
from trinity_marsh import *
from underverse_depths import *
from underverse import *
from virtua_forest_depths import *
from virtua_forest import *
from world_labyrinth_1st_floor import *
from world_labyrinth_2nd_floor import *

gathers: typing.List[LocationData] = (
    ArfoiresFactory,
    AtariMarshDepths,
    AtariMarsh,
    Darkness60,
    EndlessZone,
    GapainField,
    HellfireHollow,
    IciclePathway,
    InfiniteCorridor,
    IrisField,
    JunkBox,
    LanCastleDepths,
    LanCastleUnderground,
    LanCastle,
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
    VirtuaForestTreasures

)


enemies: typing.List[LocationData] = (
    VirtuaForestEnemies

)

