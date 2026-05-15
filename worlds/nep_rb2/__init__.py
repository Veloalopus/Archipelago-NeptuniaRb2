import logging
import os
import pkgutil
import typing
import settings
from .items import dungeonItemList, filler_items, useful_items,characterItemList
from typing import Set, Dict, Any, Callable, Optional

from BaseClasses import CollectionState, Region
from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess


from .items import NepRb2Item, item_data, allItemData,apCharacterItemBaseID
from .locations import NepRb2Location
from .options import NepRb2Options
from .locations import all_locations, gathers, location_table
from .names import ItemNames,progressiveGear
from .Regions import Nep2RegionDef
from .Rules import *


class NepRb2World(World):
    """Nep"""

    game="Hyperdimension Neptunia Re;Birth2 Sisters Generation"
    options: NepRb2Options
    options_dataclass = NepRb2Options
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}

    item_name_to_id = {name: data.code for name, data in allItemData.items()}
    item_pool: list[NepRb2Item] = []

    disabled_locations = Set[str]

    def create_item(self, name:str) -> NepRb2Item:
        return NepRb2Item(name, allItemData[name].type, allItemData[name].code, self.player)
    

    def create_regions(self) -> None:
        self.disabled_locations = set()
        # Create
        devin = Nep2RegionDef(self.multiworld,self.player,self.options)
        devin.setup_regions()
        devin.setup_dungeon_entrace()
        devin.setup_locations()
        set_win_condition(self)

    def create_items(self) -> None:
        item_pool= []

        for i in range(0, self.options.goal_total):
            item_pool.append(self.create_item(ItemNames.key_old_sword)) # Old sword doesnt even- OH
        item_pool.append(self.create_item(ItemNames.key_sharicite))
        item_pool.append(self.create_item(ItemNames.key_purple_disc))
        item_pool.append(self.create_item(ItemNames.key_black_disc))
        item_pool.append(self.create_item(ItemNames.key_white_disc))
        item_pool.append(self.create_item(ItemNames.key_green_disc))
        for DungeonName in dungeonItemList.keys():
            if DungeonName == "Dungeon Unlock - Virtua Forest":
                self.multiworld.push_precollected(self.create_item(DungeonName)) # nvm i lied
            else:
                item_pool.append(self.create_item(DungeonName))

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
        while numbersOfItemsInTheGame > len(item_pool):
            if self.random.randrange(0,100) > 55:
                item_pool.append(self.create_item(useful_items[self.random.randrange(0,len(useful_items))]))
            else:
                item_pool.append(self.create_item(filler_items[self.random.randrange(0,len(filler_items))]))
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


