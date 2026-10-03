import logging
import json
import os
import pkgutil
import typing
import settings
from typing import Set, Dict, Any, Callable, Optional

from BaseClasses import CollectionState, Region
from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess
from Options import Option

from .region import *
from .items import NepRb2Item, item_table
from .region import loadLocations,Nep2RegionDeft
from .options import NepRb2Options
from .names import ItemNames,progressiveGear
from .globals import ApNamesToRule


class NepRb2World(World):
    """Nep"""

    game="Hyperdimension Neptunia Re;Birth2 Sisters Generation"
    ut_can_gen_without_yaml = True
    options: NepRb2Options
    options_dataclass = NepRb2Options
    location_name_to_id = {loc_data["LocationName"]: loc_data["LocationID"] for loc_data in loadLocations()}

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    item_pool: list[NepRb2Item] = []

    disabled_locations = Set[str]
    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.item_quantities = {name: 0 for name, data in item_table.items()}

    def create_item(self, name:str) -> NepRb2Item:
        if name in item_table:
            return NepRb2Item(name, item_table[name].classification, item_table[name].code, self.player)
        name = ItemNames.healing_grass
        return NepRb2Item(name, item_table[name].classification, item_table[name].code, self.player)
    

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

        for name, data in item_table.items():
            self.item_quantities[name] = data.default_quantity


        if self.options.random_character.value > 0:
            starting_character = self.random.choice(list(ApNamesToRule["Character"].keys()))
        else:
            starting_character = "Character - Neptune"
        self.item_quantities[starting_character] = -1
        self.multiworld.push_precollected(self.create_item(starting_character))

        numbersOfItemsInTheGame = len(self.multiworld.get_unfilled_locations(self.player))
        while numbersOfItemsInTheGame > len(item_pool):
                item_pool.append(self.create_item("Herb"))
        
        for item,quantity in self.item_quantities.items():
            item_pool += [self.create_item(item) for _ in range(0, quantity)]

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        return
    
    def fill_slot_data(self) -> dict:
        return {
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


