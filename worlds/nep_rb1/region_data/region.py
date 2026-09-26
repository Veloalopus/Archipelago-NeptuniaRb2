from BaseClasses import List,Dict
from ..names.DungeonIDs import all_dungeons
from ..names.DungeonNames import *

class RegionData:
    def __init__(self,name:str,power:int, defense:int, level:int,partnerRegion:str = None):
        self.name = name
        self.power = power
        self.defense = defense
        self.level = level
        self.partnerDungeon = partnerRegion 

all_dungeon_regions:List[RegionData] = [
    #planeptune
RegionData(virtua_forest,                        000, 0, 000),
RegionData(monster_cave,                         000, 0, 000),
RegionData(west_wind_valley,                     250, 1, 10),
RegionData(thelad_sanctuary,                     350, 1, 10),
RegionData(avenir_storage_no3,                   450, 1, 10),
RegionData(ms_mountain,                          450, 1, 10,     ms_mountain_peak),
RegionData(marubaco_forest,                      450, 1, 30),
RegionData(halo_mountain,                        450, 1, 30,     halo_mountain_peak),
RegionData(halo_mountain_peak,                   450, 1, 30,     halo_mountain),
RegionData(lowee_snowfield,                      550, 2, 40),
RegionData(avenir_storage_no4,                   550, 2, 40),
RegionData(hyrarule_snowfield,                   550, 2, 40),
RegionData(stella_plains,                        550, 2, 40),
RegionData(soulsac_cave,                         550, 2, 50),
RegionData(fantasy_zone,                         550, 2, 50),
RegionData(neo_geofront,                         950, 3, 60,     neo_geofront_depths),
RegionData(neo_geofront_depths,                  950, 3, 60,     neo_geofront),
RegionData(factory_no459,                        950, 3, 60,     factory_no459_depths),
RegionData(factory_no459_depths,                 950, 3, 60,     factory_no459),
RegionData(m_frontier_cave,                      950, 3, 60),
RegionData(gheytz_forest,                        950, 3, 60),
RegionData(road_to_celestia,                     2300, 4, 70),
RegionData(ms_mountain_peak,                     750, 1, 10,     ms_mountain),
RegionData(zeca_ruins_no1,                       750, 1, 10),
RegionData(mechtro_factory,                      750, 1, 10),
RegionData(ortan_fields,                         750, 1, 10),
RegionData(toh_kiden_cave,                       750, 1, 20),
RegionData(gravidaze_ruins,                      950, 2, 30),
RegionData(gunbreak_underground_cavern,          950, 2, 30),
RegionData(duty_space,                           950, 2, 40),
RegionData(donkong_ruins,                        1150, 3, 50),
RegionData(naasne_volcano,                       1150, 3, 50),
RegionData(millenium_labryinth,                  2300, 4, 70),
RegionData(kinest_range,                         1150, 3, 60),
RegionData(yukawa_ruins,                         2300, 4, 70),
RegionData(adjiten_forest_pass,                  1150, 3, 60),
RegionData(uwii_ruins,                           2300, 4, 70),
RegionData(zeca_ruins_no2,                       2750, 5, 80),
RegionData(dees_snow_forest,                     2300, 4, 70),
RegionData(graphic_pass,                         2750, 5, 80,     graphic_pass_peak),
RegionData(graphic_pass_peak,                    2750, 5, 80,     graphic_pass),
RegionData(naasne_volcano_depths,                1150, 3, 50),

]

all_dungeon_regions_dict ={ k.name:k for k in all_dungeon_regions}
