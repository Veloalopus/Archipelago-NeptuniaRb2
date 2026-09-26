import typing
from ..LocationData import LocationData

from .adaldik_forest import *
from .anonydeaths_lab import *
from .anonydeaths_lab_depths import *
from .ario_plateau import *
from .bandicrash import *
from .castle_chambers import *
from .city_center import *
from .digital_future_land import *
from .digital_future_depths import *
from .do_temple import *
from .duo_r_ruins import *
from .em_es_magma_cave import *
from .em_es_magma_cave_depths import *
from .extradimensional_space import *
from .gigo_depths import *
from .gigo_main_entrance import *
from .graphic_pass import *
from .graphic_pass_peak import *
from .halo_forest import *
from .haneda_mountain_range import *
from .haneda_mountain_peak import *
from .jet_set_range import *
from .jet_set_peak import *
from .keraga_dimension import *
from .koagura_plateau import *
from .kobaba_ruins import *
from .kuzarat_facility_1 import *
from .kuzarat_facility_2 import *
from .lowee_castle_exterior import *
from .lowee_castle_interior import *
from .lowee_castle_northern_space import *
from .lowee_castle_southern_space import *
from .luji_plateau import *
from .magma_cave import *
from .magma_cave_depths import *
from .metroid_shelter import *
from .metroid_shelter_depths import *
from .mines import *
from .national_factory import *
from .nekutoki_forest import *
from .otori_cave import *
from .otori_forest import *
from .pii_shii_game_factory import *
from .planeptune_alley import *
from .powerlevel_island import *
from .powerlevel_island_interior import *
from .ps_dimension import *
from .reload_grasslands import *
from .rud_arms_sewer_n import *
from .rud_arms_sewer_s import *
from .so_shal_forest import *
from .soni_wetlands import *
from .station_area import *
from .suaho_mountain_range import *
from .suaho_mountain_peak import *
from .under_inverse import *
from .under_inverse_depths import *
from .underground_cave import *
from .vida_dimension import *
from .virtua_forest import *
from .virtua_forest_depths import *
from .virtua_forest_safe_zone import *
from .wanderers_cave import *
from .wanderers_cave_depths import *
from .zeca_ruins_no1 import *
from .zeca_ruins_no2 import *
from .zega_forest import *
from .quests import Quests

gathers: typing.List[LocationData] = (
    AdaldikForest,
    AnonydeathsLab,
    AnonydeathsLabDepths,
    ArioPlateau,
    Bandicrash,
    CastleChambers,
    CityCenter,
    DigitalFutureLand,
    DigitalFutureDepths,
    DoTemple,
    DuoRRuins,
    EmEsMagmaCave,
    EmEsMagmaCaveDepths,
    ExtradimensionalSpace,
    GigoMainEntrance,
    GigoDepths,
    GraphicPass,
    GraphicPassPeak,
    HaloForest,
    HanedaMountainRange,
    HanedaMountainPeak,
    JetSetRange,
    JetSetPeak,
    KeragaDimension,
    KoaguraPlateau,
    KobabaRuins,
    KuzaratFacility1,
    KuzaratFacility2,
    LoweeCastleExterior,
    LoweeCastleInterior,
    LoweeCastleNorthernSpace,
    LoweeCastleSouthernSpace,
    LujiPlateau,
    MagmaCave,
    MagmaCaveDepths,
    MetroidShelter,
    MetroidShelterDepths,
    Mines,
    NationalFactory,
    NekutokiForest,
    OtoriCave,
    OtoriForest,
    PiiShiiGameFactory,
    PlaneptuneAlley,
    PowerlevelIsland,
    PowerlevelIslandInterior,
    PSDimension,
    ReloadGrasslands,
    RudArmsSewerN,
    RudArmsSewerS,
    SoShalForest,
    SoniWetlands,
    StationArea,
    SuahoMountainRange,
    SuahoMountainPeak,
    UnderInverse,
    UnderInverseDepths,
    UndergroundCave,
    VidaDimension,
    VirtuaForest,
    VirtuaForestDepths,
    VirtuaForestSafeZone,
    WanderersCave,
    WanderersCaveDepths,
    ZecaRuinsNo1,
    ZecaRuinsNo2,
    ZegaForest,
)

questLocation: typing.List[LocationData] = Quests

treasures: typing.List[LocationData] = (
    AdaldikForestTreasures,
    AnonydeathsLabTreasures,
    AnonydeathsLabDepthsTreasures,
    ArioPlateauTreasures,
    BandicrashTreasures,
    CastleChambersTreasures,
    CityCenterTreasures,
    DigitalFutureLandTreasures,
    DigitalFutureDepthsTreasures,
    DoTempleTreasures,
    DuoRRuinsTreasures,
    EmEsMagmaCaveTreasures,
    EmEsMagmaCaveDepthsTreasures,
    ExtradimensionalSpaceTreasures,
    GigoMainEntranceTreasures,
    GigoDepthsTreasures,
    GraphicPassTreasures,
    GraphicPassPeakTreasures,
    HaloForestTreasures,
    HanedaMountainRangeTreasures,
    HanedaMountainPeakTreasures,
    JetSetRangeTreasures,
    JetSetPeakTreasures,
    KeragaDimensionTreasures,
    KoaguraPlateauTreasures,
    KobabaRuinsTreasures,
    KuzaratFacility1Treasures,
    KuzaratFacility2Treasures,
    LoweeCastleExteriorTreasures,
    LoweeCastleInteriorTreasures,
    LoweeCastleNorthernSpaceTreasures,
    LoweeCastleSouthernSpaceTreasures,
    LujiPlateauTreasures,
    MagmaCaveTreasures,
    MagmaCaveDepthsTreasures,
    MetroidShelterTreasures,
    MetroidShelterDepthsTreasures,
    MinesTreasures,
    NationalFactoryTreasures,
    NekutokiForestTreasures,
    OtoriCaveTreasures,
    OtoriForestTreasures,
    PiiShiiGameFactoryTreasures,
    PlaneptuneAlleyTreasures,
    PowerlevelIslandTreasures,
    PowerlevelIslandInteriorTreasures,
    PSDimensionTreasures,
    ReloadGrasslandsTreasures,
    RudArmsSewerNTreasures,
    RudArmsSewerSTreasures,
    SoShalForestTreasures,
    SoniWetlandsTreasures,
    StationAreaTreasures,
    SuahoMountainRangeTreasures,
    SuahoMountainPeakTreasures,
    UnderInverseTreasures,
    UnderInverseDepthsTreasures,
    UndergroundCaveTreasures,
    VidaDimensionTreasures,
    VirtuaForestTreasures,
    VirtuaForestDepthsTreasures,
    VirtuaForestSafeZoneTreasures,
    WanderersCaveTreasures,
    WanderersCaveDepthsTreasures,
    ZecaRuinsNo1Treasures,
    ZecaRuinsNo2Treasures,
    ZegaForestTreasures,
)

enemies: typing.List[LocationData] = (
    AdaldikForestEnemies,
    AnonydeathsLabDepthsEnemies,
    AnonydeathsLabEnemies,
    ArioPlateauEnemies,
    BandicrashEnemies,
    CastleChambersEnemies,
    CityCenterEnemies,
    #DigitalFutureDepthsEnemies,
    DigitalFutureLandEnemies,
    DoTempleEnemies,
    DuoRRuinsEnemies,
    #EmEsMagmaCaveDepthsEnemies,
    EmEsMagmaCaveEnemies,
    ExtradimensionalSpaceEnemies,
    GigoDepthsEnemies,
    GigoMainEntranceEnemies,
    GraphicPassEnemies,
    #GraphicPassPeakEnemies,
    HaloForestEnemies,
    HanedaMountainPeakEnemies,
    HanedaMountainRangeEnemies,
    JetSetPeakEnemies,
    JetSetRangeEnemies,
    KeragaDimensionEnemies,
    KoaguraPlateauEnemies,
    KobabaRuinsEnemies,
    KuzaratFacility1Enemies,
    KuzaratFacility2Enemies,
    LoweeCastleExteriorEnemies,
    #LoweeCastleInteriorEnemies,
    LoweeCastleNorthernSpaceEnemies,
    LoweeCastleSouthernSpaceEnemies,
    LujiPlateauEnemies,
    MagmaCaveDepthsEnemies,
    MagmaCaveEnemies,
    MetroidShelterDepthsEnemies,
    MetroidShelterEnemies,
    MinesEnemies,
    NationalFactoryEnemies,
    NekutokiForestEnemies,
    OtoriCaveEnemies,
    OtoriForestEnemies,
    PiiShiiGameFactoryEnemies,
    PlaneptuneAlleyEnemies,
    PowerlevelIslandEnemies,
    #PowerlevelIslandInteriorEnemies,
    PSDimensionEnemies,
    ReloadGrasslandsEnemies,
    RudArmsSewerNEnemies,
    RudArmsSewerSEnemies,
    SoShalForestEnemies,
    SoniWetlandsEnemies,
    StationAreaEnemies,
    #SuahoMountainPeakEnemies,
    SuahoMountainRangeEnemies,
    UndergroundCaveEnemies,
    #UnderInverseDepthsEnemies,
    UnderInverseEnemies,
    VidaDimensionEnemies,
    VirtuaForestEnemies,
    VirtuaForestSafeZoneEnemies,
    WanderersCaveDepthsEnemies,
    WanderersCaveEnemies,
    ZecaRuinsNo1Enemies,
    ZecaRuinsNo2Enemies,
    ZegaForestEnemies,
)

goalLocation: typing.List[LocationData] = (
    CityCenterGoal,
)

levels: typing.List[LocationData] = (
LocationData("Adaldik Forest","Grinding",40,"Level"),
LocationData("Anonydeath's Lab Depths","Grinding",60,"Level"),
LocationData("Anonydeath's Lab","Grinding",60,"Level"),
LocationData("Ario Plateau","Grinding",60,"Level"),
LocationData("Bandicrash","Grinding",20,"Level"),
LocationData("Castle Chambers","Grinding",30,"Level"),
LocationData("City Center","Grinding",70,"Level"),
LocationData("Do Temple","Grinding",100,"Level"),
LocationData("Duo R Ruins","Grinding",90,"Level"),
LocationData("EM ES Magma Cave Depths","Grinding",80,"Level"),
LocationData("EM ES Magma Cave","Grinding",80,"Level"),
LocationData("Extradimensional Space","Grinding",70,"Level"),
LocationData("Gigo Depths","Grinding",40,"Level"),
LocationData("Gigo Main Entrance","Grinding",40,"Level"),
LocationData("Graphic Pass Peak","Grinding",70,"Level"),
LocationData("Graphic Pass","Grinding",70,"Level"),
LocationData("Halo Forest","Grinding",40,"Level"),
LocationData("Haneda Mountain Peak","Grinding",60,"Level"),
LocationData("Haneda Mountain Range","Grinding",60,"Level"),
LocationData("Jet Set Peak","Grinding",10,"Level"),
LocationData("Jet Set Range","Grinding",10,"Level"),
LocationData("Keraga Dimension","Grinding",60,"Level"),
LocationData("Koagura Plateau","Grinding",100,"Level"),
LocationData("Kobaba Ruins","Grinding",60,"Level"),
LocationData("Kuzarat Facility 1","Grinding",20,"Level"),
LocationData("Kuzarat Facility 2","Grinding",20,"Level"),
LocationData("Lowee Castle Exterior","Grinding",30,"Level"),
LocationData("Lowee Castle Interior","Grinding",30,"Level"),
LocationData("Lowee Castle Northern Space","Grinding",80,"Level"),
LocationData("Lowee Castle Southern Space","Grinding",60,"Level"),
LocationData("Luji Plateau","Grinding",60,"Level"),
LocationData("Magma Cave Depths","Grinding",60,"Level"),
LocationData("Magma Cave","Grinding",60,"Level"),
LocationData("Metroid Shelter","Grinding",50,"Level"),
LocationData("Metroid Shelter Depths","Grinding",50,"Level"),
LocationData("Mines","Grinding",50,"Level"),
LocationData("National Factory","Grinding",50,"Level"),
LocationData("Nekutoki Forest","Grinding",60,"Level"),
LocationData("Otori Cave","Grinding",60,"Level"),
LocationData("Otori Forest","Grinding",10,"Level"),
LocationData("Pii Shii Game Factory","Grinding",70,"Level"),
LocationData("Planeptune Alley","Grinding",100,"Level"),
LocationData("Powerlevel Island Interior","Grinding",70,"Level"),
LocationData("Powerlevel Island","Grinding",70,"Level"),
LocationData("PS Dimension","Grinding",50,"Level"),
LocationData("Reload Grasslands","Grinding",30,"Level"),
LocationData("Rud Arms Sewer N.","Grinding",30,"Level"),
LocationData("Rud Arms Sewer S.","Grinding",30,"Level"),
LocationData("So Shal Forest","Grinding",80,"Level"),
LocationData("Soni Wetlands","Grinding",30,"Level"),
LocationData("Station Area","Grinding",10,"Level"),
LocationData("Suaho Mountain Range","Grinding",40,"Level"),
LocationData("Suaho Mountain Peak","Grinding",40,"Level"),
LocationData("Under Inverse","Grinding",100,"Level"),
LocationData("Under Inverse Depths","Grinding",100,"Level"),
LocationData("Underground Cave","Grinding",30,"Level"),
LocationData("Vida Dimension","Grinding",80,"Level"),
LocationData("Virtua Forest Depths","Grinding",70,"Level"),
LocationData("Virtua Forest Safe Zone","Grinding",10,"Level"),
LocationData("Virtua Forest","Grinding",70,"Level"),
LocationData("Wanderer's Cave","Grinding",20,"Level"),
LocationData("Wanderer's Cave Depths","Grinding",20,"Level"),
LocationData("Zeca Ruins No.1","Grinding",10,"Level"),
LocationData("Zeca Ruins No.2","Grinding",20,"Level"),
LocationData("Zega Forest","Grinding",50,"Level"),
)