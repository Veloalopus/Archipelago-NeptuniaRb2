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

def launch_client():
    """Launch a Rb2 Client"""
    from .client import launch
    launch_subprocess(launch, name="NepRb2Client")

components.append(Component(
    "Hyperdimension Neptunia Re;Birth2 Sisters Generation Client"
    "NepRb2Client",
    func=launch_client,
    component_type=Type.CLIENT
))
from .items import NepRb2Item, item_data, allItemData, location_table
from .locations import NepRb2Location
from .options import NepRb2Options
from .locations import all_locations, gathers, location_table
from .names import ItemNames


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
        return

    def create_items(self) -> None:
        item_pool= []
        item_pool.append(self.create_item(ItemNames.healing_grass))


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
    



