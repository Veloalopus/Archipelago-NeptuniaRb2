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
from .globals import RuleToApNames,ApNamesToRule,DungeonIdDict

class NepRB2Logic():

    def can_reach_enemy(enemy:str,state:CollectionState,player:int):
        return state.can_reach_location(enemy,player)

    def can_reach_dungeon(dungeon:str,changeFlag:int,state:CollectionState,player:int):
        return state.can_reach_region(dungeon,player)

    def has_item(group:str,item:str,state:CollectionState,player:int,count:int = 1):
        #change item to itemdisplay name
        if group not in RuleToApNames:
            ValueError(f"Item group does not exist.[{group}]")
        if  item not in RuleToApNames[group]:
            ValueError(f"Item does not exist.[{item}]")
        return state.has(RuleToApNames[group][item]["DisplayName"],player,count)

    def dungeon_unlocked(dungeon:str,state:CollectionState,player:int):
        if dungeon not in RuleToApNames["Dungeon"]:
            ValueError(f"Dungeon does not exist.[{dungeon}]")
        return state.has(RuleToApNames["Dungeon"][dungeon]["DisplayName"],player)

    def has_level(level:int,state:CollectionState,player:int):
        return state.has(f"LEVEL_{level}",player)

    def has_power(power:int,state:CollectionState,player:int):
        characterPower = []
        for ruleChar,info in RuleToApNames["Character"].items():
            if state.has(info["DisplayName"],player):
                tier = state.count(RuleToApNames["ProgressiveGear"][ruleChar]["DisplayName"],player)
                characterPower.append(RuleToApNames["ProgressiveGear"][ruleChar]["Power"][tier])
        characterPower.sort(reverse=True)
        playerStrength = 0
        for i in range(0,4):
            if i >= len(characterPower): break
            playerStrength += characterPower[i]
        return playerStrength >= power

    def has_defense(armor:int,state:CollectionState,player:int):
        return state.has(RuleToApNames["ProgressiveGear"]["ARMOR"]["DisplayName"],player,armor)
    
    def has_dungeon_state(dungeonId:int,change:int,state:CollectionState,player:int):
        match change:
            case 1:
                return DungeonIdDict[dungeonId]["ChangeDungeon"] == None or state.has(DungeonIdDict[dungeonId]["ChangeDungeon"],player)
            case 2:
                return DungeonIdDict[dungeonId]["AddEnemies"] == None or state.has(DungeonIdDict[dungeonId]["AddEnemies"],player)
        raise ValueError("Dungeon change value error")            

    def has_ApEvent(event:str,state:CollectionState,player:int):
        return state.has(event,player)