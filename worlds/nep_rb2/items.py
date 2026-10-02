
from typing import NamedTuple, Optional
import json,pkgutil,os
from BaseClasses import Item, ItemClassification
from typing import Dict, Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from . import TeviWorld

apDungeonItemBaseID = 2_000_000
apCharacterItemBaseID = 3_000_000
progressiveGearBaseID = 3_500_000
apEventItemBaseID = 4_000_000
class NepRb2Item(Item):
    game = "Hyperdimension Neptunia Re;Birth 2 Sisters Generation"

class NepRb2ItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    group:str = ""
    default_quantity: int = 1
    max_quantity: int = 1
    weight: int = 1
    def __init__(self,category: str,
                code: Optional[int] = None,
                classification: ItemClassification = ItemClassification.filler,
                default_quantity: int = 1,
                max_quantity: int = 1,
                weight: int = 100):
        self.category= category
        self.code: Optional[int] = code
        self.classification = classification
        self.default_quantity: int = default_quantity
        self.max_quantity: int = max_quantity
        self.weight: int = weight

item_table: Dict[str,NepRb2ItemData] ={
}
dungeon_table: Dict[str,NepRb2ItemData] = {
}
event_table: Dict[str, NepRb2ItemData] = {
}
trap_table: Dict[str,NepRb2ItemData] = {
}
character_table: Dict[str,NepRb2ItemData] = {
}
progressive_gear: Dict[str,NepRb2ItemData] = {
}

RuleToApNames = {}
ApNamesToRule = {}
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
        if item["Classification"] == "progression":
            itemData.classification = ItemClassification.progression
        elif item["Classification"] == "trap":
            itemData.classification = ItemClassification.trap
        elif item["Classification"] == "useful":
            itemData.classification = ItemClassification.useful

        if itemData.classification == ItemClassification.trap:
            trap_table[item["DisplayName"]] = itemData

        RuleToApNames[item["Name"]] = item["DisplayName"]
        ApNamesToRule[item["DisplayName"]] = item["Name"]
    
loadItems()