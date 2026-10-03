
from typing import NamedTuple, Optional
import json,pkgutil,os
from BaseClasses import Item, ItemClassification
from typing import Dict, Optional, TYPE_CHECKING

from .globals import ApNamesToRule,RuleToApNames

if TYPE_CHECKING:
    from . import NepRb2World

apDungeonItemBaseID = 2_000_000
apCharacterItemBaseID = 3_000_000
progressiveGearBaseID = 3_500_000
apEventItemBaseID = 4_000_000
class NepRb2Item(Item):
    game = "Hyperdimension Neptunia Re;Birth 2 Sisters Generation"

class NepRb2ItemData():
    def __init__(self,group: str,
                code: Optional[int] = None,
                classification: ItemClassification = ItemClassification.filler,
                default_quantity: int = 1,
                max_quantity: int = 1,
                weight: int = 100):
        self.group= group
        self.code: Optional[int] = code
        self.classification = classification
        self.default_quantity: int = default_quantity
        self.max_quantity: int = max_quantity
        self.weight: int = weight

item_table: Dict[str,NepRb2ItemData] ={
}



def loadItems():
    from importlib.resources import files
    resourcesFiles = files(__name__) / "resources"

    locationsFiles = resourcesFiles / "items"

    items = []
    for file in locationsFiles.glob("*.json"):
        items += json.loads(file.read_text()) 



    for item in items:
        match item["Group"]:
            case "Dungeon":
                item["ID"] += apDungeonItemBaseID
            case "Character":
                item["ID"] += apCharacterItemBaseID
            case "Event":
                item["ID"] += apEventItemBaseID
            case "ProgressiveGear":
                item["ID"] += progressiveGearBaseID

        itemData = NepRb2ItemData(item["Group"],item["ID"],ItemClassification.filler,item["Default_Quantity"],item["Maximum_Quantity"],item["Weight"])
        match item["Classification"]:
            case "progression":
                itemData.classification = ItemClassification.progression
            case "trap":
                itemData.classification = ItemClassification.trap
            case "useful":
                itemData.classification = ItemClassification.useful


        if not item["Group"] in RuleToApNames:
            RuleToApNames[item["Group"]] = {}
            ApNamesToRule[item["Group"]] = {}
           
        RuleToApNames[item["Group"]][item["Name"]] = item
        ApNamesToRule[item["Group"]][item["DisplayName"]] = item
        item_table[item["DisplayName"]] = itemData


    
loadItems()