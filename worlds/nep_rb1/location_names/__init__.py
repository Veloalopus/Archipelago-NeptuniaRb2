import typing
from ..LocationData import LocationData

from .virtua_forest                import *
from .monster_cave                 import *
from .west_wind_valley             import *
from .thelad_sanctuary             import *
from .avenir_storage_no3           import *
from .ms_mountain                  import *
from .marubaco_forest              import *
from .halo_mountain                import *
from .halo_mountain_peak           import *
from .lowee_snowfield              import *
from .avenir_storage_no4           import *
from .hyrarule_snowfield           import *
from .stella_plains                import *
from .soulsac_cave                 import *
from .fantasy_zone                 import *
from .neo_geofront                 import *
from .neo_geofront_depths          import *
from .factory_no459                import *
from .factory_no459_depths         import *
from .m_frontier_cave              import *
from .gheytz_forest                import *
from .road_to_celestia             import *
from .ms_mountain_peak             import *
from .zeca_ruins_no1               import *
from .mechtro_factory              import *
from .ortan_fields                 import *
from .toh_kiden_cave               import *
from .gravidaze_ruins              import *
from .gunbreak_underground_cavern  import *
from .duty_space                   import *
from .donkong_ruins                import *
from .naasne_volcano               import *
from .millenium_labryinth          import *
from .kinest_range                 import *
from .yukawa_ruins                 import *
from .adjiten_forest_pass          import *
from .uwii_ruins                   import *
from .zeca_ruins_no2               import *
from .dees_snow_forest             import *
from .graphic_pass                 import *
from .graphic_pass_peak            import *
from .naasne_volcano_depths        import *

gathers: typing.List[LocationData] = (
    AdjitenForest,
    AvenirStorageNo3,
    AvenirStorageNo4,
    DeesSnowForest,
    DonkongRuins,
    DutySpace,
    FactoryNo459,
    FactoryNo459Depths,
    FantasyZone,
    GheytzForest,
    GraphicPass,
    GraphicPassPeak,
    GravidazeRuins,
    GunbreakUndergroundCavern,
    HaloMountain,
    HaloMountainPeak,
    HyraruleSnowfield,
    KinestRange,
    LoweeSnowfield,
    MFrontierCave,
    MarubacoForest,
    MechtroFactory,
    MilleniumLabryinth,
    MonsterCave,
    MsMountain,
    MsMountainPeak,
    NaasneVolcano,
    NaasneVolcanoDepths,
    NeoGeofront,
    NeoGeofrontDepths,
    OrtanFields,
    SoulsacCave,
    StellaPlains,
    TheladSanctuary,
    TohKidenCave,
    UwiiRuins,
    VirtuaForest,
    WestWindValley,
    YukawaRuins,
    ZecaRuinsNo1,
    ZecaRuinsNo2,
)

treasures: typing.List[LocationData] = (
    AdjitenForestTreasures,
    AvenirStorageNo3Treasures,
    AvenirStorageNo4Treasures,
    DeesSnowForestTreasures,
    DonkongRuinsTreasures,
    DutySpaceTreasures,
    FactoryNo459Treasures,
    FactoryNo459DepthsTreasures,
    FantasyZoneTreasures,
    GheytzForestTreasures,
    GraphicPassTreasures,
    GraphicPassPeakTreasures,
    GravidazeRuinsTreasures,
    GunbreakUndergroundCavernTreasures,
    HaloMountainTreasures,
    HaloMountainPeakTreasures,
    HyraruleSnowfieldTreasures,
    KinestRangeTreasures,
    LoweeSnowfieldTreasures,
    MFrontierCaveTreasures,
    MarubacoForestTreasures,
    MechtroFactoryTreasures,
    MilleniumLabryinthTreasures,
    MonsterCaveTreasures,
    MsMountainTreasures,
    MsMountainPeakTreasures,
    NaasneVolcanoTreasures,
    NaasneVolcanoDepthsTreasures,
    NeoGeofrontTreasures,
    NeoGeofrontDepthsTreasures,
    OrtanFieldsTreasures,
    RoadToCelestiaTreasures,
    SoulsacCaveTreasures,
    StellaPlainsTreasures,
    TheladSanctuaryTreasures,
    TohKidenCaveTreasures,
    UwiiRuinsTreasures,
    VirtuaForestTreasures,
    WestWindValleyTreasures,
    YukawaRuinsTreasures,
    ZecaRuinsNo1Treasures,
    ZecaRuinsNo2Treasures,
)

enemies: typing.List[LocationData] = (
    AdjitenForestEnemies,
    AvenirStorageNo3Enemies,
    AvenirStorageNo4Enemies,
    DeesSnowForestEnemies,
    DonkongRuinsEnemies,
    DutySpaceEnemies,
    FactoryNo459DepthsEnemies,
    FactoryNo459Enemies,
    FantasyZoneEnemies,
    GheytzForestEnemies,
    GraphicPassEnemies,
    GraphicPassPeakEnemies,
    GravidazeRuinsEnemies,
    GunbreakUndergroundCavernEnemies,
    HaloMountainEnemies,
    HaloMountainPeakEnemies,
    HyraruleSnowfieldEnemies,
    KinestRangeEnemies,
    LoweeSnowfieldEnemies,
    MFrontierCaveEnemies,
    MarubacoForestEnemies,
    MechtroFactoryEnemies,
    MilleniumLabryinthEnemies,
    MonsterCaveEnemies,
    MsMountainEnemies,
    MsMountainPeakEnemies,
    NaasneVolcanoDepthsEnemies,
    NaasneVolcanoEnemies,
    NeoGeofrontDepthsEnemies,
    NeoGeofrontEnemies,
    OrtanFieldsEnemies,
    RoadToCelestiaEnemies,
    SoulsacCaveEnemies,
    StellaPlainsEnemies,
    TheladSanctuaryEnemies,
    TohKidenCaveEnemies,
    UwiiRuinsEnemies,
    VirtuaForestEnemies,
    WestWindValleyEnemies,
    YukawaRuinsEnemies,
    ZecaRuinsNo1Enemies,
    ZecaRuinsNo2Enemies,
)

goalLocation: typing.List[LocationData] = (
    RoadToCelestiaGoal,
)

levels: typing.List[LocationData] = (
LocationData("Virtua Forest","Grinding",10,"Level"),
LocationData("Monster Cave","Grinding",10,"Level"),
LocationData("West Wind Valley","Grinding",20,"Level"),
LocationData("Zeca Ruins No.1","Grinding",20,"Level"),
LocationData("Avenir Storage No.3","Grinding",20,"Level"),
LocationData("Thelad Sanctuary","Grinding",20,"Level"),
LocationData("MS Mountain","Grinding",30,"Level"),
LocationData("MS Mountain Peak","Grinding",30,"Level"),
LocationData("Marubaco Forest","Grinding",40,"Level"),
LocationData("Halo Mountain","Grinding",40,"Level"),
LocationData("Halo Mountain Peak","Grinding",40,"Level"),
LocationData("Lowee Snowfield","Grinding",50,"Level"),
LocationData("Hyrarule Snowfield","Grinding",50,"Level"),
LocationData("Stella Plains","Grinding",50,"Level"),
LocationData("Avenir Storage No.4","Grinding",50,"Level"),
LocationData("Soulsac Cave","Grinding",60,"Level"),
LocationData("Fantasy Zone","Grinding",60,"Level"),
LocationData("Neo-Geofront","Grinding",70,"Level"),
LocationData("Neo-Geofront Depths","Grinding",70,"Level"),
LocationData("Gheytz Forest","Grinding",70,"Level"),
LocationData("M-Frontier Cave","Grinding",70,"Level"),
LocationData("Road to Celestia","Grinding",80,"Level"),
LocationData("Mechtro Factory","Grinding",20,"Level"),
LocationData("Ortan Fields","Grinding",20,"Level"),
LocationData("Yukawa Ruins","Grinding",80,"Level"),
LocationData("Factory No.459","Grinding",70,"Level"),
LocationData("Factory No.459 Depths","Grinding",70,"Level"),
LocationData("Toh-Kiden Cave","Grinding",30,"Level"),
LocationData("Gravidaze Ruins","Grinding",40,"Level"),
LocationData("Naasne Volcano","Grinding",60,"Level"),
LocationData("Naasne Volcano Depths","Grinding",60,"Level"),
LocationData("Zeca Ruins No.2","Grinding",90,"Level"),
LocationData("Gunbreak Underground Cavern","Grinding",40,"Level"),
LocationData("Duty Space","Grinding",50,"Level"),
LocationData("Kinest Range","Grinding",70,"Level"),
LocationData("Adjiten Forest Pass","Grinding",70,"Level"),
LocationData("Graphic Pass","Grinding",90,"Level"),
LocationData("Graphic Pass Peak","Grinding",90,"Level"),
LocationData("Donkong Ruins","Grinding",60,"Level"),
LocationData("Millenium Labryinth","Grinding",80,"Level"),
LocationData("Uwii Ruins","Grinding",80,"Level"),
LocationData("Dees Snow Forest","Grinding",80,"Level"),
)