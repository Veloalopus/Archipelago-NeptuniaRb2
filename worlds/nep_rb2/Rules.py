from typing import TYPE_CHECKING

from .names import DungeonNames, CharacterNames, progressiveGear, DungeonIDs, ItemNames
from BaseClasses import CollectionState
from .items import apDungeonItemBaseID, item_id_to_name, NepRb2Item, item_data,dungeonItemList
from .region_data.region import RegionData
from .names import ItemNames
from .locations import NepRb2Location
from BaseClasses import ItemClassification
if TYPE_CHECKING:
    from . import NepRb2World


def hasDungeonUnlocked(state:CollectionState,player:int,DungeonName:str):
    id = DungeonIDs.all_dungeons[DungeonName]
    return state.has(item_id_to_name[id+apDungeonItemBaseID],player)

## Should have logic reflect as glitched so players arent outright thinking they can't even obtain treasures or gathers in dungeons like DFL or other postgame dungeons
def hasLevel(level:int,state:CollectionState,player:int):
    if level == 0:
        return True
    return state.has(f"Level {level}",player)

def StartingCharactersStrength(ProgressiveTier:int):   # Neptune, Plutia, Noire
    if ProgressiveTier == 1:
        return 400
    elif ProgressiveTier == 2:
        return 750
    elif ProgressiveTier == 3:
        return 1050
    elif ProgressiveTier == 4:
        return 1450
    elif ProgressiveTier == 5:
        return 2150
    elif ProgressiveTier == 6:
        return 2350
    return 50

def MidCharactersStrength(ProgressiveTier:int):     # Blanc, Vert, Nepgear
    if ProgressiveTier == 1:
        return 550
    elif ProgressiveTier == 2:
        return 900
    elif ProgressiveTier == 3:
        return 1150
    elif ProgressiveTier == 4:
        return 1500
    elif ProgressiveTier == 5:
        return 2200
    return 275


def freakingPeashyStrength(ProgressiveTier:int): #Peashy
    if ProgressiveTier == 1:
        return 1200
    elif ProgressiveTier == 2:
        return 1450
    elif ProgressiveTier == 3:
        return 1800
    elif ProgressiveTier == 4:
        return 1800
    elif ProgressiveTier == 5:
        return 2200
    return 1050

def HyperCandidatesStrength(ProgressiveTier:int): # Uni, Rom, Ram
    if ProgressiveTier == 1:
        return 1300
    elif ProgressiveTier == 2:
        return 1450
    elif ProgressiveTier == 3:
        return 2100
    elif ProgressiveTier == 4:
        return 2350
    return 1150

def ArmorStrength(ProgressiveArmor:int): # All armor
    if ProgressiveArmor == 1:
        return 500
    elif ProgressiveArmor == 2:
        return 1100
    elif ProgressiveArmor == 3:
        return 1450
    elif ProgressiveArmor == 4:
        return 1750
    elif ProgressiveArmor == 5:
        return 2350
    return 100

def checkDungeonRequirements (PowerRequirement: int, state:CollectionState, player:int,ArmorRequirement:int = 1):
    playerStrength = 0
    characterStrength = []
    armorStrength = []
    if state.has(CharacterNames.neptune, player):
        characterStrength.append(StartingCharactersStrength(state.count(progressiveGear.neptune_progressive_gear,player)))
        
    if state.has(CharacterNames.nepgear, player):
        characterStrength.append(MidCharactersStrength(state.count(progressiveGear.nepgear_progressive_gear,player)))
        
    if state.has(CharacterNames.noire, player):
        characterStrength.append(StartingCharactersStrength(state.count(progressiveGear.noire_progressive_gear,player)))
        
    if state.has(CharacterNames.blanc,player):
        characterStrength.append(MidCharactersStrength(state.count(progressiveGear.blanc_progressive_gear,player)))
        
    if state.has(CharacterNames.vert,player):
        characterStrength.append(MidCharactersStrength(state.count(progressiveGear.vert_progressive_gear,player)))
            
    if state.has(CharacterNames.uni,player):
        characterStrength.append(HyperCandidatesStrength(state.count(progressiveGear.uni_progressive_gear,player)))
        
    if state.has(CharacterNames.rom,player):
        characterStrength.append(HyperCandidatesStrength(state.count(progressiveGear.rom_progressive_gear,player)))
        
    if state.has(CharacterNames.ram,player):
        characterStrength.append(HyperCandidatesStrength(state.count(progressiveGear.ram_progressive_gear,player)))
        

    characterStrength.sort(reverse=True)
    armorTier = state.count(progressiveGear.progressive_armor,player)
    for i in range(0,4):
        if i >= len(characterStrength): break
        playerStrength += characterStrength[i]
    
    return playerStrength >= PowerRequirement and armorTier >= ArmorRequirement

def dungeonLogic(region:RegionData,state:CollectionState,player:int):
    allowed = True
    id = DungeonIDs.all_dungeons[region.name]
    if id+apDungeonItemBaseID in item_id_to_name:
        allowed &= state.has(item_id_to_name[id+apDungeonItemBaseID],player)
    allowed &= hasLevel(region.level,state,player)
    allowed &= checkDungeonRequirements(region.power,state,player,region.defense)
    return allowed

def createDungeonLogic(region:RegionData,player:int):
    return lambda state: dungeonLogic(region,state,player)

def set_win_condition(world: "NepRb2World") -> None:
    goalLoc = world.multiworld.get_location("Graveyard - Oblivion - True Arfoire", world.player)


    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    world.set_rule(goalLoc, lambda state: checkDungeonRequirements(2050, state, world.player) and hasDungeonUnlocked(state,world.player,DungeonNames.graveyard_oblivion) and state.has(ItemNames.key_old_sword, world.player))
    world.multiworld.get_location("Graveyard - Oblivion - True Arfoire", world.player).place_locked_item(NepRb2Item("Victory", ItemClassification.progression, None, world.player))

