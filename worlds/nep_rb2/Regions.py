from typing import List, Dict, TYPE_CHECKING, Optional,Set
import math
from BaseClasses import Region, Location,MultiWorld,Entrance,CollectionState,ItemClassification
from .LocationData import LocationData
from .locations import all_locations
from .location_names import levels
from .options import NepRb2Options
from .items import item_id_to_name,apDungeonItemBaseID,NepRb2Item,DungeonUnlockExists
from .names import DungeonIDs
from .region_data.region import all_dungeon_regions
from .Rules import createDungeonLogic
if TYPE_CHECKING:
    from . import NepRb2World

class Rb2Location(Location):
    game: str = "Hyperdimension Neptunia Re;birth 2 Sisters Generation"


class Nep2RegionDef:
    def __init__(self,world:MultiWorld,player:int, options:NepRb2Options):
        self.multiworld = world
        self.player = player
        self.option = options
        self.locations = all_locations #add option for dlc dungeons and include them in this list
        self.regions:Dict[str,Region]={}
        self.monsterRegion:Dict[int,List[LocationData]] = {}
        self.menu = Region("Menu", self.player, self.multiworld)
        self.regions["Menu"] = self.menu

    def setup_regions(self):
        self.multiworld.regions.append(self.menu)
        for dungeon in all_dungeon_regions:
            newRegion = self.create_region(dungeon.name)
            self.multiworld.regions.append(newRegion)
            self.regions[newRegion.name] = newRegion


    def setup_dungeon_entrace(self):
        for dungeon in all_dungeon_regions:
            if DungeonUnlockExists(dungeon.name):
                self.menu.add_exits([dungeon.name],{dungeon.name:createDungeonLogic(dungeon,self.player)})
            if dungeon.partnerDungeon != None:
                self.regions[dungeon.partnerDungeon].add_exits([dungeon.name],{dungeon.name:lambda _:True})

    def setup_locations(self):
        for loc in self.locations:
            region = self.regions[loc.region]
            if "Enemy" in loc.itemType:
                if loc.id in self.monsterRegion:
                    self.monsterRegion[loc.id].append(loc)
                else:
                    self.monsterRegion[loc.id] = [loc]
                continue
            newLocation = self.create_location(loc,region)
            region.locations.append(newLocation)
        
        # handle all enemies
        self.create_monster_regions_and_connect()
        self.create_level_events()

    def create_monster_regions_and_connect(self):
        for monsters in self.monsterRegion.values():
            newLoc = Rb2Location(self.player, monsters[0].objectiven_name, monsters[0].id)
            if len(monsters) > 1:
                newMonsterRegion = self.create_region(monsters[0].objectiven_name)
                newLoc.parent_region = newMonsterRegion
                self.multiworld.regions.append(newMonsterRegion)
                for monster in monsters:
                    self.regions[monster.region].add_exits([newMonsterRegion.name],{newMonsterRegion.name:lambda _:True})
                monsters[0].name = monsters[0].objectiven_name
                newMonsterRegion.locations.append(newLoc)
            else:
                region = self.regions[monsters[0].region]
                newLoc.parent_region = region
                region.locations.append(newLoc)

    def create_level_events(self):
        dungeonGrindCapList:List[LocationData] =levels
        for grindSpot in dungeonGrindCapList:
            region = self.regions[grindSpot.region]
            location = Rb2Location(self.player,f"{grindSpot.name} {grindSpot.itemType} {grindSpot.id}",None,region)
            item = NepRb2Item(f"{grindSpot.itemType} {grindSpot.id}",ItemClassification.progression,None,self.player)
            location.place_locked_item(item)
            region.locations.append(location)
            #self.multiworld.worlds[self.player].item_name_to_id[item.name] = item.code

    def create_dungeon_exits(self):
        menu = self.multiworld.get_region("Menu", self.player)
        newExit:Entrance
        for region in self.regions.values():
            id = DungeonIDs.all_dungeons[region.name]

            newExit = menu.add_exits({region.name:region.name}) #missing rules

    def create_location(self,location_data: LocationData, region: Region) -> Location:
        location = Rb2Location(self.player, location_data.name, location_data.id, region)
        #create rule for location?
        return location

    def create_region(self, name: str) -> Region:
        region = Region(name, self.player, self.multiworld)
        return region

    def get_locations_per_region(self,locations: List[LocationData]) -> Dict[str, List[LocationData]]:
        per_region: Dict[str, List[LocationData]] = {}

        for location in locations:
            per_region.setdefault(location.region, []).append(location)

        return per_region
