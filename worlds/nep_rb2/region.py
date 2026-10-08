import os
import json,pkgutil
from BaseClasses import Location, Region, MultiWorld, ItemClassification,LocationProgressType,EntranceType
from importlib.resources import files 

from worlds.generic.Rules import set_rule

from .globals import *
from .offsets import AddIdOffest
from .options import NepRb2Options
from .logic_parser import parse_expression_logic,evaluate_rule
from .items import NepRb2Item
class Rb2Location(Location):
    game: str = "Hyperdimension Neptunia Re;birth 2 Sisters Generation"



def loadResources():
    resourcesFiles = files(__name__) / "resources"
    locationsFiles = resourcesFiles / "locations"
    locations = []
    for file in locationsFiles.glob("*.json"):
        locations += json.loads(file.read_text())
    for loc in locations:
        match loc["Type"]:
            case "LocationID":
                loc["ID"] += TreasureBaseID
            case "Enemy":
                loc["LocationID"] += EnemyBaseID
                EnemyDict[loc["LocationName"]] = loc
            case "Quest":
                loc["LocationID"] += QuestBaseID

    resourcesFiles = files(__name__) / "resources"
    regions = json.loads(resourcesFiles.joinpath("region.json").read_text())
    for region in regions:
        if region["DungeonID"] != 0:
            DungeonIdDict[region["DungeonID"]] = region
    return locations

loadResources()

class Nep2RegionDeft:
    """
    This class provides methods associated with defining and connecting regions, locations,
    and the access rules for those regions and locations.
    """
  
    def __init__(self, multiworld: MultiWorld, player: int, options:NepRb2Options):

        self.data = {}
        self.player = player
        self.multiworld = multiworld
        self.options = options
        self.locations = loadResources()
        resourcesFiles = files(__name__) / "resources"

        self.regions = json.loads(resourcesFiles.joinpath("region.json").read_text())



    def set_regions(self):
        for region in self.regions:
            self.multiworld.regions.append(Region(region["Name"], self.player, self.multiworld))

    def connect_regions(self):
        regionCache = self.multiworld.regions.region_cache[self.player]

        for region in self.regions:
            for exit in region["Connections"]:
                rule = exit["Method"]
                ap_rule = parse_expression_logic(rule)
                ap_rule = evaluate_rule(ap_rule,self.player,self.options)
                entrance = regionCache[region["Name"]].add_exits([exit["Exit"]],{exit["Exit"]:ap_rule})


    def set_locations(self):

      
        regions = self.multiworld.regions.region_cache[self.player]
        for location in self.locations:

            if location["DLC"] != 0:
                continue
            id = location["LocationID"]
            if id == 0:
                id = None
            else:
                id = AddIdOffest(id,location["Type"])
                
            location_name = location["LocationName"]
            if len(location["Region"]) == 1:
                region_name = location["Region"][0]
            else:
                region_name = location["LocationName"]
                self.multiworld.regions.append(Region(region_name, self.player, self.multiworld))
                for multiRegion in location["Region"]:
                    regions[multiRegion].add_exits([region_name])

            rule = ""
            for partial_rule in location["Requirement"]:
                rule += f"({partial_rule["Method"]})"

            ap_rule = parse_expression_logic(rule)
            ap_rule = evaluate_rule(ap_rule,self.player,self.options)

                

            ap_location = Rb2Location(
                self.player,
                location_name,
                id,
                regions[region_name]
            )
            set_rule(ap_location,ap_rule)
            if id == None:
                ap_location.place_locked_item(NepRb2Item(location["Item"],ItemClassification.progression,None,self.player))
                
            regions[region_name].locations.append(ap_location)

            #set_rule(ap_location,ap_rule)

