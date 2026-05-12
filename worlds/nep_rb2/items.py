from typing import NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .names import ItemNames

apDungeonItemBaseID = 2_000_000
apCharacterItemBaseID = 3_000_000
progressiveGearBaseID = 3_500_000
class NepRb2Item(Item):
    game = "Hyperdimension Neptunia Re;Birth 2 Sisters Generation"

class NepRb2ItemData(NamedTuple):
    code: Optional[int] = None
    type ItemClassification = ItemClassification.filler
    group:str = ""


item_data: dict[str, NepRb2ItemData] = {
    #fmt: off
    #INDEX_NOTHING
    ItemNames.healing_grass:                       NepRb2ItemData(1,ItemClassification.useful),
    ItemNames.healing_pod:                         NepRb2ItemData(2,ItemClassification.useful),
    ItemNames.healing_drink:                       NepRb2ItemData(3,ItemClassification.useful),
    ItemNames.healing_bottle:                      NepRb2ItemData(4,ItemClassification.useful),
    ItemNames.nepbull:                             NepRb2ItemData(5,ItemClassification.useful),
    ItemNames.nepbull_c:                           NepRb2ItemData(6,ItemClassification.useful),
    ItemNames.nepbull_sp:                          NepRb2ItemData(7,ItemClassification.useful),
    ItemNames.nepbull_ex:                          NepRb2ItemData(8,ItemClassification.useful),
    ItemNames.nepbull_ex2:                         NepRb2ItemData(9,ItemClassification.useful),
    ItemNames.special_drink_c:                     NepRb2ItemData(10,ItemClassification.useful),
    ItemNames.special_drink_h:                     NepRb2ItemData(11,ItemClassification.useful),
    ItemNames.compas_bandaid_kit:                  NepRb2ItemData(12,ItemClassification.useful),
    ItemNames.compas_medical_kit:                  NepRb2ItemData(13,ItemClassification.useful),
    ItemNames.sp_charger:                          NepRb2ItemData(14,ItemClassification.useful),
    ItemNames.p_sp_charger:                        NepRb2ItemData(15,ItemClassification.useful),
    ItemNames.p_sp_charger_2:                      NepRb2ItemData(16,ItemClassification.useful),
}