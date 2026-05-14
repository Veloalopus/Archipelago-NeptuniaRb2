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
# Can make all 0's???
all_dungeon_regions:List[RegionData] = [
    RegionData(arfoires_factory,                    1250, 2, 40),
    RegionData(atari_marsh_depths,                  650, 1, 20,           atari_marsh  ),
    RegionData(atari_marsh,                         650, 1, 20,           atari_marsh_depths),
    RegionData(darkness_60,                         50, 0, 000),
    RegionData(endless_zone,                        200, 0, 000),
    RegionData(gamindustri_graveyard,               2350, 4, 50,           graveyard_depths),
    RegionData(gapain_field,                        950, 2, 20),
    RegionData(graveyard_depths,                    2350, 4, 50,           gamindustri_graveyard),
    RegionData(graveyard_oblivion,                  4500, 4, 60),
    RegionData(hellfire_hollow,                     6360, 5, 70),
    RegionData(icicle_pathway,                      4350, 4, 60),
    RegionData(infinite_corridor,                   4350, 4, 70),
    RegionData(iris_field,                          1350, 3, 30),
    RegionData(junk_box,                            4350, 4, 60),
    RegionData(lan_castle_depths,                   2650, 3, 40,           lan_castle),
    RegionData(lan_castle_underground,              2650, 3, 30),
    RegionData(lan_castle,                          2650, 3, 40,           lan_castle_depths),
    RegionData(lost_ruins,                          6300, 5, 70),
    RegionData(lowee_global_expo_east,              300, 1, 10,           lowee_global_expo_west),
    RegionData(lowee_global_expo_west,              300, 1, 10,           lowee_global_expo_east),
    RegionData(midcompany,                          50, 0, 000),
    RegionData(panan_jungle,                        6300, 5, 70),
    RegionData(powerlevel_island,                   750, 1, 20),
    RegionData(rebeat_resort,                       250, 0, 000),
    RegionData(septent_resort,                      250, 0, 000),
    RegionData(severed_dimension_depths,            1350, 1, 30,           severed_dimension),
    RegionData(severed_dimension,                   1350, 1, 30,           severed_dimension_depths),
    RegionData(sublie_road,                         6300, 4, 60),
    RegionData(trinity_marsh,                       6300, 5, 70),
    RegionData(underverse_depths,                   750, 1, 20,           underverse),
    RegionData(underverse,                          750, 1, 20,           underverse_depths),
    RegionData(virtua_forest_depths,                50, 0, 000),
    RegionData(virtua_forest,                       50, 0, 000),
    RegionData(world_labyrinth_1st_floor,           350, 0, 10,           world_labyrinth_2nd_floor),
    RegionData(world_labyrinth_2nd_floor,           350, 0, 10,           world_labyrinth_1st_floor),
]

