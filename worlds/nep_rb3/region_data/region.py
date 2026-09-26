from BaseClasses import List,Dict
from ..names.DungeonIDs import all_dungeons
from ..names.DungeonNames import *
from ..names.ItemNames import *
class RegionData:
    def __init__(self,name:str,power:int, defense:int, level:int,partnerRegion:str = None,changeDungeon:str = None,bigChangeDungeon:str = None,):
        self.name = name
        self.power = power
        self.defense = defense
        self.level = level
        self.partnerDungeon = partnerRegion
        self.changeDungeon = changeDungeon
        self.bigChangeDungeon = bigChangeDungeon 

all_dungeon_regions:List[RegionData] = [
    #planeptune
    RegionData(jet_set_range,                       250,    1,   0,    jet_set_peak                    ,changeDungeon=plan_dungeonchangejetsetrange),
    RegionData(otori_forest,                        1,      0,  000                                    ,changeDungeon=plan_dungeonchangeotoriforest),
    RegionData(zeca_ruins_no1,                      250,    0,  000                                    ,changeDungeon=plan_dungeonchangezecaruinsno1),
    RegionData(zeca_ruins_no2,                      500,    1,  10                                     ,changeDungeon=plan_dungeonchangezecaruinsno2,bigChangeDungeon=plan_bigdungeonchangezecaruinsno2),
    RegionData(haneda_mountain_range,               2750,   2,  50,    haneda_mountain_peak            ,changeDungeon=plan_dungeonchangehanedamountainrange,bigChangeDungeon=plan_bigdungeonchangehanedamountainrange),
    RegionData(haneda_mountain_peak,                2750,   2,  50,    haneda_mountain_range           ,changeDungeon=plan_dungeonchangehanedamountainrange,bigChangeDungeon=plan_bigdungeonchangehanedamountainrange),
    RegionData(otori_cave,                          2300,   2,  50                                     ,changeDungeon=plan_dungeonchangeotoricave,bigChangeDungeon=plan_bigdungeonchangeotoricave),
    RegionData(powerlevel_island,                   3050,   3,  60,    powerlevel_island_interior      ,changeDungeon=plan_dungeonchangepowerlevelisland,bigChangeDungeon=plan_bigdungeonchangepowerlevelisland),
    RegionData(powerlevel_island_interior,          3050,   3,  60,    powerlevel_island               ,changeDungeon=plan_dungeonchangepowerlevelisland,bigChangeDungeon=plan_bigdungeonchangepowerlevelisland),
    RegionData(digital_future_land,                 5050,   4,  90,    digital_future_depths           ,changeDungeon=plan_dungeonchangedigitalfutureland,bigChangeDungeon=plan_bigdungeonchangedigitalfutureland),
    RegionData(digital_future_depths,               5050,   4,  90,    digital_future_land             ,changeDungeon=plan_dungeonchangedigitalfutureland,bigChangeDungeon=plan_bigdungeonchangedigitalfutureland),

    #laststation
    RegionData(jet_set_peak,                        250,    1,  000,    jet_set_range                  ,changeDungeon=plan_dungeonchangejetsetrange),
    RegionData(rud_arms_sewer_n,                    950,    1,  20,    rud_arms_sewer_s                ,changeDungeon=plan_dungeonchangerudarmssewer,bigChangeDungeon=plan_bigdungeonchangerudarmssewer),
    RegionData(vida_dimension,                      3050,   4,  70                                     ,changeDungeon=plan_dungeonchangevidadimension,bigChangeDungeon=plan_bigdungeonchangevidadimension),
    RegionData(gigo_main_entrance,                  900,    1,  30,    gigo_depths                     ,changeDungeon=plan_dungeonchangegigo,bigChangeDungeon=plan_bigdungeonchangegigo),
    RegionData(gigo_depths,                         900,    1,  30,    gigo_main_entrance              ,changeDungeon=plan_dungeonchangegigo,bigChangeDungeon=plan_bigdungeonchangegigo),
    RegionData(anonydeaths_lab,                     4550,   4,  50,    anonydeaths_lab_depths          ,changeDungeon=plan_dungeonchangeanonydeathslab,bigChangeDungeon=plan_bigdungeonchangeanonydeathslab),
    RegionData(anonydeaths_lab_depths,              4550,   4,  50,    anonydeaths_lab                 ,changeDungeon=plan_dungeonchangeanonydeathslab,bigChangeDungeon=plan_bigdungeonchangeanonydeathslab),
    RegionData(soni_wetlands,                       400,    1,  20                                     ,changeDungeon=plan_dungeonchangesoniwetlands,bigChangeDungeon=plan_bigdungeonchangesoniwetlands),
    RegionData(wanderers_cave,                      450,    1,  10,    wanderers_cave_depths           ,changeDungeon=plan_dungeonchangewandererscave,bigChangeDungeon=plan_bigdungeonchangewandererscave),
    RegionData(wanderers_cave_depths,               450,    1,  10,    wanderers_cave                  ,changeDungeon=plan_dungeonchangewandererscave,bigChangeDungeon=plan_bigdungeonchangewandererscave),
    RegionData(kuzarat_facility_1,                  450,    1,  10,    kuzarat_facility_2              ,changeDungeon=plan_dungeonchangekuzaratfacility,bigChangeDungeon=plan_bigdungeonchangekuzaratfacility),
    RegionData(kuzarat_facility_2,                  450,    1,  10,    kuzarat_facility_1              ,changeDungeon=plan_dungeonchangekuzaratfacility,bigChangeDungeon=plan_bigdungeonchangekuzaratfacility),
    RegionData(bandicrash,                          400,    1,  10                                     ,changeDungeon=plan_dungeonchangebandicrash,bigChangeDungeon=plan_bigdungeonchangebandicrash),
    RegionData(national_factory,                    1000,   2,  40                                     ,changeDungeon=plan_dungeonchangenationalfactory,bigChangeDungeon=plan_bigdungeonchangenationalfactory),
    RegionData(ps_dimension,                        1300,   2,  40                                     ,changeDungeon=plan_dungeonchangepsdimension,bigChangeDungeon=plan_bigdungeonchangepsdimension),

    #lowee
    RegionData(rud_arms_sewer_s,                    950,    1,  20,    rud_arms_sewer_n                ,changeDungeon=plan_dungeonchangerudarmssewer,bigChangeDungeon=plan_bigdungeonchangerudarmssewer),
    RegionData(ario_plateau,                        3530,   2,  50                                     ,changeDungeon=plan_dungeonchangearioplateau,bigChangeDungeon=plan_bigdungeonchangearioplateau),
    RegionData(castle_chambers,                     350,    1,  20                                     ,changeDungeon=plan_dungeonchangeundergroundcave,bigChangeDungeon=plan_bigdungeonchangeundergroundcave),
    RegionData(lowee_castle_exterior,               300,    1,  20,    lowee_castle_interior           ,changeDungeon=plan_dungeonchangeloweecastle,bigChangeDungeon=plan_bigdungeonchangeloweecastle),
    RegionData(lowee_castle_interior,               300,    1,  20,    lowee_castle_exterior           ,changeDungeon=plan_dungeonchangeloweecastle,bigChangeDungeon=plan_bigdungeonchangeloweecastle),
    RegionData(lowee_castle_northern_space,         3500,   4,  70,    lowee_castle_southern_space     ,changeDungeon=plan_dungeonchangeloweecastlens,bigChangeDungeon=plan_bigdungeonchangeloweecastlens),
    RegionData(lowee_castle_southern_space,         2550,   3,  50,    lowee_castle_northern_space     ,changeDungeon=plan_dungeonchangeloweecastlens,bigChangeDungeon=plan_bigdungeonchangeloweecastlens),
    RegionData(luji_plateau,                        1250,   2,  50                                     ,changeDungeon=plan_dungeonchangelujiplateau,bigChangeDungeon=plan_bigdungeonchangelujiplateau),
    RegionData(metroid_shelter,                     1350,   2,  40,    metroid_shelter_depths          ,changeDungeon=plan_dungeonchangemetroidshelter,bigChangeDungeon=plan_bigdungeonchangemetroidshelter),
    RegionData(metroid_shelter_depths,              1350,   2,  40,    metroid_shelter                 ,changeDungeon=plan_dungeonchangemetroidshelter,bigChangeDungeon=plan_bigdungeonchangemetroidshelter),
    RegionData(reload_grasslands,                   1100,   2,  20                                     ,changeDungeon=plan_dungeonchangereloadgrasslands,bigChangeDungeon=plan_bigdungeonchangereloadgrasslands),
    RegionData(underground_cave,                    350,    1,  20,    castle_chambers                 ,changeDungeon=plan_dungeonchangeundergroundcave,bigChangeDungeon=plan_bigdungeonchangeundergroundcave),
    RegionData(mines,                               1100,   3,  40                                     ,changeDungeon=plan_dungeonchangemines,bigChangeDungeon=plan_bigdungeonchangemines),

    #leanbox
    RegionData(halo_forest,                         350,    1,  30                                     ,changeDungeon=plan_dungeonchangehaloforest,bigChangeDungeon=plan_bigdungeonchangehaloforest),
    RegionData(zega_forest,                         650,    2,  40                                     ,changeDungeon=plan_dungeonchangezegaforest,bigChangeDungeon=plan_bigdungeonchangezegaforest),
    RegionData(em_es_magma_cave,                    4250,   4,  70,    em_es_magma_cave_depths         ,changeDungeon=plan_dungeonchangeemesmagmacave,bigChangeDungeon=plan_bigdungeonchangeemesmagmacave),
    RegionData(em_es_magma_cave_depths,             4250,   4,  70,    em_es_magma_cave                ,changeDungeon=plan_dungeonchangeemesmagmacave,bigChangeDungeon=plan_bigdungeonchangeemesmagmacave),
    RegionData(kobaba_ruins,                        3145,   4,  50                                     ,changeDungeon=plan_dungeonchangekobabaruins,bigChangeDungeon=plan_bigdungeonchangekobabaruins),
    RegionData(nekutoki_forest,                     3150,   4,  50                                     ,changeDungeon=plan_dungeonchangenekutokiforest,bigChangeDungeon=plan_bigdungeonchangenekutokiforest),
    
    #pc continent
    RegionData(adaldik_forest,                      1450,   2,  30                                     ,changeDungeon=plan_dungeonchangeadaldikforest,bigChangeDungeon=plan_bigdungeonchangeadaldikforest),
    RegionData(pii_shii_game_factory,               5050,   3,  60                                     ,changeDungeon=plan_dungeonchangepiishiigamefactory,bigChangeDungeon=plan_bigdungeonchangepiishiigamefactory),
    RegionData(do_temple,                           4675,   4,  90                                     ,changeDungeon=plan_dungeonchangedotemple,bigChangeDungeon=plan_bigdungeonchangedotemple),

    #hello
    RegionData(keraga_dimension,                    3750,   4,  50                                     ,changeDungeon=plan_dungeonchangekeragadimension,bigChangeDungeon=plan_bigdungeonchangekeragadimension),
    RegionData(suaho_mountain_range,                1750,   2,  30,    suaho_mountain_peak             ,changeDungeon=plan_dungeonchangesuahomountainrange,bigChangeDungeon=plan_bigdungeonchangesuahomountainrange),
    RegionData(suaho_mountain_peak,                 1750,   2,  30,    suaho_mountain_range            ,changeDungeon=plan_dungeonchangesuahomountainrange,bigChangeDungeon=plan_bigdungeonchangesuahomountainrange),
    RegionData(so_shal_forest,                      3250,   4,  70                                     ,changeDungeon=plan_dungeonchangesoshalforest,bigChangeDungeon=plan_bigdungeonchangesoshalforest),

    #eden
    RegionData(magma_cave,                          2750,   2,  50,    magma_cave_depths               ,changeDungeon=plan_dungeonchangemagmacave,bigChangeDungeon=plan_bigdungeonchangemagmacave),
    RegionData(magma_cave_depths,                   2750,   2,  50,    magma_cave                      ,changeDungeon=plan_dungeonchangemagmacave,bigChangeDungeon=plan_bigdungeonchangemagmacave),
    RegionData(extradimensional_space,              2750,   3,  60                                     ,changeDungeon=plan_dungeonchangeextradimensionalspace,bigChangeDungeon=plan_bigdungeonchangeextradimensionalspace),
    RegionData(graphic_pass,                        3750,   3,  60,    graphic_pass_peak               ,changeDungeon=plan_dungeonchangegraphicpass,bigChangeDungeon=plan_bigdungeonchangegraphicpass),
    RegionData(graphic_pass_peak,                   3750,   3,  60,    graphic_pass                    ,changeDungeon=plan_dungeonchangegraphicpass,bigChangeDungeon=plan_bigdungeonchangegraphicpass),
    RegionData(duo_r_ruins,                         3750,   4,  80                                     ,changeDungeon=plan_dungeonchangeduorruins,bigChangeDungeon=plan_bigdungeonchangeduorruins),
    RegionData(koagura_plateau,                     4750,   4,  90                                     ,changeDungeon=plan_dungeonchangekoaguraplateau,bigChangeDungeon=plan_bigdungeonchangekoaguraplateau),
    
    #hyperdimension
    RegionData(city_center,                         5080,   5,  60                                     ,changeDungeon=plan_dungeonchangecitycenter,bigChangeDungeon=plan_bigdungeonchangecitycenter),
    RegionData(virtua_forest_safe_zone,             0,      0,  000                                    ,changeDungeon=plan_dungeonchangevirtuaforestsafezone),
    RegionData(station_area,                        0,      0,  000                                    ,changeDungeon=plan_dungeonchangeplaneptunestationfr),
    RegionData(virtua_forest,                       3650,   3,  60,    virtua_forest_depths            ,changeDungeon=plan_dungeonchangevirtuaforest,bigChangeDungeon=plan_bigdungeonchangevirtuaforest),
    RegionData(virtua_forest_depths,                3650,   3,  60,    virtua_forest                   ,changeDungeon=plan_dungeonchangevirtuaforest,bigChangeDungeon=plan_bigdungeonchangevirtuaforest),
    RegionData(under_inverse,                       5550,   4,  90,    under_inverse_depths            ,changeDungeon=plan_dungeonchangeunderinverse,bigChangeDungeon=plan_bigdungeonchangeunderinverse),
    RegionData(under_inverse_depths,                5550,   4,  90,    under_inverse                   ,changeDungeon=plan_dungeonchangeunderinverse,bigChangeDungeon=plan_bigdungeonchangeunderinverse),
    RegionData(planeptune_alley,                    9000,   5,  90                                     ,changeDungeon=plan_dungeonchangeplaneptunealley,bigChangeDungeon=plan_bigdungeonchangeplaneptunealley),
    #RegionData(32650,0,0,planeptune_alley),treasure ruins
    
    #RegionData(,0,0,),
]

all_dungeon_regions_dict ={ k.name:k for k in all_dungeon_regions}
