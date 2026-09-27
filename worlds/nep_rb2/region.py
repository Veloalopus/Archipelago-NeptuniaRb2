import os
import json,pkgutil
from offsets import AddIdOffest
from BaseClasses import Location, Region, MultiWorld, ItemClassification,LocationProgressType,EntranceType

from worlds.generic.Rules import set_rule

from .options import NepRb2Options
from .items import item_id_to_name,apDungeonItemBaseID,NepRb2Item,DungeonUnlockExists



class Rb2Location(Location):
    game: str = "Hyperdimension Neptunia Re;birth 2 Sisters Generation"


class Nep2RegionDeft:
    """
    This class provides methods associated with defining and connecting regions, locations,
    and the access rules for those regions and locations.
    """
  
    def __init__(self, multiworld: MultiWorld, player: int, options:NepRb2Options):
        from importlib.resources import files 

        self.data = {}
        self.player = player
        self.multiworld = multiworld

        resourcesFiles = files(__name__) / "resources"

        locationsFiles = resourcesFiles / "locations"

        self.locations = []
        for file in locationsFiles.glob("*.json"):
            self.locations += json.loads(file.read_text())

        self.regions = json.loads(resourcesFiles.joinpath("region.json").read_text())


    def set_regions(self):
        for region in self.regions:
            self.multiworld.regions.append(Region(region["Name"], self.player, self.multiworld))

    def connect_regions(self):
        regionCache = self.multiworld.regions.region_cache[self.player]

        for region in self.regions:
            for exit in region["Connections"]:
                rule = exit["Method"]
                #ap_rule = parse_expression_logic(rule)
                #ap_rule = evaluate_rule(ap_rule,self.player,regions,self.options,True)
                ap_rule = lambda _: True
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

            #ap_rule = parse_expression_logic(rule)
            #ap_rule = evaluate_rule(ap_rul e,self.player,regions,self.options)

                

            ap_location = Rb2Location(
                self.player,
                location_name,
                id,
                region_name
            )
            if id == None:
                ap_location.place_locked_item(NepRb2Item(location["Item"],ItemClassification.progression,None,self.player))
                ap_location.show_in_spoiler = False
            regions[region_name].locations.append(ap_location)

            #set_rule(ap_location,ap_rule)


