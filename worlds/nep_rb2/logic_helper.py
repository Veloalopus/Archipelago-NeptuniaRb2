"""
This module defines helper methods used for evaluating rule lambdas.
Its probably a little haphazardly sorted.. but the method names are descriptive
enough for it not to be confusing.
"""
from BaseClasses import CollectionState, MultiWorld,Region,Entrance
from .globals import RuleToApNames
from .options import NepRb2Options
from worlds.AutoWorld import LogicMixin
from typing import Dict,Set


class NepRB2Logic():

    def can_reach_enemy(enemy:int,state:CollectionState,player:int):
        return state.can_reach_location(enemy,player)

    def can_reach_dungeon(dungeon:int,changeFlag:int,state:CollectionState,player:int):
        return True

    def has_item(item:str,state:CollectionState,player:int,count:int = 1):
        #change item to itemdisplay name
        return state.has(item,player,count)

    def dungeon_unlocked(dungeon:int,state:CollectionState,player:int):
        #check if player has the dungeon unlock item
        return True

    def has_level(level:int,state:CollectionState,player:int):

        return state.has(f"Level {level}")

    def has_power(power:int,state:CollectionState,player:int):
        #Calculate player power
        return True

    def has_defense(armor:int,state:CollectionState,player:int):
        #Calc defense amount
        return True


