from BaseClasses import List,Dict
from ..names.DungeonIDs import all_dungeons
from ..names.DungeonNames import *
from ..names.ItemNames import *

class RegionData:
     def __init__(self,name:str,power:int, defense:int, level:int,partnerRegion:str = None,addEnemy:str = None,changeDungeon:str = None,):
        self.name = name
        self.power = power
        self.defense = defense
        self.level = level
        self.partnerDungeon = partnerRegion
        self.addEnemy = addEnemy
        self.changeDungeon = changeDungeon
# Can make all 0's???
all_dungeon_regions:List[RegionData] = [
    RegionData(arfoires_factory,                    2050, 2, 40, addEnemy=plan_add_enemies_arfoires_factory),
    RegionData(atari_marsh_depths,                  1450, 1, 20, atari_marsh       , addEnemy=plan_add_enemies_atari_marsh),
    RegionData(atari_marsh,                         1450, 1, 20, atari_marsh_depths, addEnemy=plan_add_enemies_atari_marsh),
    RegionData(darkness_60,                         150, 0, 000, changeDungeon=plan_change_dungeon_darkness_60),
    RegionData(endless_zone,                        250, 0, 000, addEnemy=plan_add_enemies_endless_zone),
    RegionData(gamindustri_graveyard,               2850, 3, 50, graveyard_depths, addEnemy=plan_add_enemies_gamindustri_graveyard),
    RegionData(gapain_field,                        1250, 2, 20, addEnemy=plan_add_enemies_gapain_field),
    RegionData(graveyard_depths,                    2850, 4, 50, gamindustri_graveyard),
    RegionData(graveyard_oblivion,                  4500, 4, 60),
    RegionData(hellfire_hollow,                     6360, 5, 70, addEnemy=plan_add_enemies_hellfire_hollow),
    RegionData(icicle_pathway,                      4350, 4, 60, addEnemy=plan_add_enemies_icicle_pathway),
    RegionData(infinite_corridor,                   4350, 4, 70, addEnemy=plan_add_enemies_infinite_corridor),
    RegionData(iris_field,                          1750, 3, 30, addEnemy=plan_add_enemies_iris_field),
    RegionData(junk_box,                            4950, 4, 60, addEnemy=plan_add_enemies_junk_box),
    RegionData(lan_castle_depths,                   2950, 3, 40, lan_castle, addEnemy=plan_add_enemies_lan_castle, changeDungeon=plan_change_dungeon_lan_castle),
    RegionData(lan_castle_underground,              3550, 3, 30, addEnemy=plan_add_enemies_lan_castle_underground),
    RegionData(lan_castle,                          2950, 3, 40, lan_castle_depths, addEnemy=plan_add_enemies_lan_castle, changeDungeon=plan_change_dungeon_lan_castle),
    RegionData(lost_ruins,                          6300, 5, 70, addEnemy=plan_add_enemies_lost_ruins),
    RegionData(lowee_global_expo_east,              950, 1, 10,  lowee_global_expo_west, addEnemy=plan_add_enemies_lowee_global_expo, changeDungeon=plan_change_dungeon_lowee_global_expo),
    RegionData(lowee_global_expo_west,              950, 1, 10,  lowee_global_expo_east, addEnemy=plan_add_enemies_lowee_global_expo, changeDungeon=plan_change_dungeon_lowee_global_expo),
    RegionData(midcompany,                          450, 0, 000, addEnemy=plan_add_enemies_midcompany, changeDungeon=plan_change_dungeon_midcompany),
    RegionData(panan_jungle,                        6300, 5, 70, addEnemy=plan_add_enemies_panan_jungle),
    RegionData(powerlevel_island,                   1250, 1, 20, addEnemy=plan_add_enemies_powerlevel_island, changeDungeon=plan_change_dungeon_powerlevel_island),
    RegionData(rebeat_resort,                       400, 0, 000, addEnemy=plan_add_enemies_rebeat_resort),
    RegionData(septent_resort,                      400, 0, 000, addEnemy=plan_add_enemies_septent_resort, changeDungeon=plan_change_dungeon_septent_resort),
    RegionData(severed_dimension_depths,            1950, 2, 30, severed_dimension, addEnemy=plan_add_enemies_severed_dimension, changeDungeon=plan_change_dungeon_severed_dimension),
    RegionData(severed_dimension,                   1950, 2, 30, severed_dimension_depths, addEnemy=plan_add_enemies_severed_dimension, changeDungeon=plan_change_dungeon_severed_dimension),
    RegionData(sublie_road,                         6300, 4, 60, addEnemy=plan_add_enemies_sublie_road),
    RegionData(trinity_marsh,                       6300, 5, 70, addEnemy=plan_add_enemies_trinity_marsh),
    RegionData(underverse_depths,                   1350, 1, 20, underverse, addEnemy=plan_add_enemies_underverse, changeDungeon=plan_change_dungeon_underverse),
    RegionData(underverse,                          1350, 1, 20, underverse_depths, addEnemy=plan_add_enemies_underverse, changeDungeon=plan_change_dungeon_underverse),
    RegionData(virtua_forest_depths,                50, 0, 000,  changeDungeon=plan_change_dungeon_virtua_forest_depths),
    RegionData(virtua_forest,                       50, 0, 000,),
    RegionData(world_labyrinth_1st_floor,           1150, 1, 20, world_labyrinth_2nd_floor, addEnemy=plan_add_enemies_world_labyrinth, changeDungeon=plan_change_dungeon_world_labyrinth),
    RegionData(world_labyrinth_2nd_floor,           1150, 1, 20, world_labyrinth_1st_floor, addEnemy=plan_add_enemies_world_labyrinth, changeDungeon=plan_change_dungeon_world_labyrinth),
]

all_dungeon_regions_dict ={ k.name:k for k in all_dungeon_regions}