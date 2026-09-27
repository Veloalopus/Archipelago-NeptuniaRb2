import logging
import json
import os
import pkgutil
import typing
import settings
from .items import dungeonItemList, filler_items, useful_items,characterItemList, enemyDungeonList
from typing import Set, Dict, Any, Callable, Optional

from BaseClasses import CollectionState, Region
from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess
from Options import Option

from .region import *
from .LocationData import *
from .items import NepRb2Item, item_data, allItemData,apCharacterItemBaseID,eventItemList
from .locations import NepRb2Location
from .options import NepRb2Options
from .locations import all_locations, gathers, location_table
from .names import ItemNames,progressiveGear
from .Regions import Nep2RegionDef
from .Rules import *


class NepRb2World(World):
    """Nep"""

    game="Hyperdimension Neptunia Re;Birth2 Sisters Generation"
    ut_can_gen_without_yaml = True
    options: NepRb2Options
    options_dataclass = NepRb2Options
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}

    item_name_to_id = {name: data.code for name, data in allItemData.items()}
    item_pool: list[NepRb2Item] = []

    disabled_locations = Set[str]

    def create_item(self, name:str) -> NepRb2Item:
        if name in allItemData:
            return NepRb2Item(name, allItemData[name].type, allItemData[name].code, self.player)
        name = ItemNames.healing_grass
        return NepRb2Item(name, allItemData[name].type, allItemData[name].code, self.player)
    
    def createJsonFiles(self):
        from .region_data.region import all_dungeon_regions_dict
        from .names.DungeonIDs import all_dungeons
        regions = self.multiworld.get_regions(self.player)
        regionJson = []
        for region in regions:
            exits = []
            for exit in region.exits:
                to = exit.connected_region.name
                newExit = {
                    "Exit": to,
                    "Method": "",
                }
                if to in all_dungeon_regions_dict:
                    toInfo:RegionData = all_dungeon_regions_dict[to]
                    newExit["Method"] = f"Level {toInfo.level} && Power {toInfo.power} && Defense {toInfo.defense}"

                exits.append(newExit)
            newRegion = {
                "Name": region.name,
                "DungeonID": 0,
                "Connections":exits,
                "DLC":0,
                "ChangeDungeon":0,
                "AddEnemies":0,
            }
            if region.name in all_dungeons:
                newRegion["DungeonID"] = all_dungeons[region.name]
            if region.name in all_dungeon_regions_dict:
                x = all_dungeon_regions_dict[region.name]
                newRegion["ChangeDungeon"] = x.changeDungeon
                newRegion["AddEnemies"] = x.addEnemy
            regionJson.append(newRegion)
        file = open("./region.json","w+")
        file.write(json.dumps(regionJson,indent=4))
        file.close()
        locations = self.multiworld.get_locations(self.player)
        locationsJson = []
        for loc in locations:
            LocType = ""
            id = loc.address
            if id == None:
                LocType = "AP Tracker"
                id = 0
            elif id > quest_base_id:
                LocType = "Quest"
                id = id - quest_base_id
            elif id > enemy_base_id:
                LocType = "Enemy"
                id = id - enemy_base_id
            elif id > treasure_base_id:
                LocType = "Treasure"
                id = id - treasure_base_id
            else:
                LocationData = "GatherPoint"
                
            newLocation = {
                "Item":"",
                "LocationName": loc.name,
                "Region": [loc.parent_region.name],
                "Requirement":[],
                "LocationID":id,
                "Type":LocType,
                "DLC":0
            }
            locationsJson.append(newLocation)
        file = open("./location.json","w+")
        file.write(json.dumps(locationsJson,indent=4))
        file.close()

    def create_regions(self) -> None:
        self.disabled_locations = set()
        a = Nep2RegionDeft(self.multiworld,self.player,self.options)
        a.set_regions()
        a.connect_regions()
        a.set_locations()
        # Create
        #devin = Nep2RegionDef(self.multiworld,self.player,self.options)
        #devin.setup_regions()
        #devin.setup_dungeon_entrace()
        #devin.setup_locations()
        #set_win_condition(self)
        #self.createJsonFiles()

    def create_items(self) -> None:
        item_pool= []
        item_pool.append(self.create_item(ItemNames.key_old_sword))
        for QuestName in enemyDungeonList.keys():
            item_pool.append(self.create_item(QuestName))
        for DungeonName in dungeonItemList.keys():
            if DungeonName == "Dungeon Unlock - Virtua Forest":
                self.multiworld.push_precollected(self.create_item(DungeonName)) # nvm i lied
            else:
                item_pool.append(self.create_item(DungeonName))
        for cg in eventItemList.keys():
            item_pool.append(self.create_item(cg))
            
        if self.options.random_character.value > 0:
            starting_character = self.random.choice(list(characterItemList.keys()))
        else:
            starting_character = CharacterNames.nepgear
        self.multiworld.push_precollected(self.create_item(starting_character))
        self.starting_character = characterItemList[starting_character].code - apCharacterItemBaseID

        for CharacterName in characterItemList.keys():
            if starting_character == CharacterName: continue
            item_pool.append(self.create_item(CharacterName))
            
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.nepgear_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.IF_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.compa_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.red_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.broccoli_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.fivepb_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.cave_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.falcom_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.neptune_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.noire_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.blanc_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.vert_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.marvy_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.cyberconnect2_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.tekken_progressive_gear))
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.uni_progressive_gear))
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.rom_progressive_gear))
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.ram_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.progressive_armor))

        numbersOfItemsInTheGame = len(self.multiworld.get_unfilled_locations(self.player))
        itemCreated = []
        while numbersOfItemsInTheGame > len(item_pool):
            if self.random.randrange(0,100) > 55:
                item = useful_items[self.random.randrange(0,len(useful_items))]
                if allItemData[item].unique and item in itemCreated:
                    continue
                itemCreated.append(item)
                item_pool.append(self.create_item(item))
            else:
                item = filler_items[self.random.randrange(0,len(filler_items))]
                if allItemData[item].unique and item in itemCreated:
                    continue
                itemCreated.append(item)
                item_pool.append(self.create_item(item))
        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        return
    
    def set_rules(self) -> None:

        return
    #Its gotten worse somehow lol

    def fill_slot_data(self) -> dict:
        return {
            "start_character":self.starting_character,
            "options":self.options.get_options(),
        }
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a regen in UT
        return slot_data
    
    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            # Set all your options here instead of getting them from the yaml
            for key, value in slot_options.items():
                opt: Optional[Option] = getattr(self.options, key, None)
                if opt is not None:
                    # You can also set .value directly but that won't work if you have OptionSets
                    setattr(self.options, key, opt.from_any(value))


