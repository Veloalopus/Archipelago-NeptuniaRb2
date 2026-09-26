import typing

from BaseClasses import Item, ItemClassification
from .names import ItemNames
from . import DropTables

apItemBaseID = 80000000
treasureItemIDOffset = 1000
dungeonItemIDOffset = 4000
keyItemIDOffset = 5000
consumableItemIDOffset = 10000
apTreasureBaseID = apItemBaseID + treasureItemIDOffset
apKeyItemBaseID = apItemBaseID + keyItemIDOffset
apDungeonItemBaseID = 2_000_000
apConsumableItemBaseID = apItemBaseID = consumableItemIDOffset

class ItemData(typing.NamedTuple):
    code: int
    itemName: str
    classification: ItemClassification
    table: DropTables.InternalItem

class Rb3Item(Item):
    game: str = "Hyperdimension Neptunia Re;Birth3 V GENERATION"


treasureList: typing.List[ItemData] = [
    ItemData(apTreasureBaseID + 1, ItemNames.vfsz_treasure1, ItemClassification.filler, DropTables.vfsz_treasure1),
    ItemData(apTreasureBaseID + 2, ItemNames.vfsz_treasure2, ItemClassification.filler, DropTables.vfsz_treasure2),
    ItemData(apTreasureBaseID + 3, ItemNames.vfsz_treasure3, ItemClassification.filler, DropTables.vfsz_treasure3),
    ItemData(apTreasureBaseID + 4, ItemNames.vfsz_treasure4, ItemClassification.filler, DropTables.vfsz_treasure4),
    ItemData(apTreasureBaseID + 5, ItemNames.stationArea_treasure1, ItemClassification.filler, DropTables.stationArea_treasure1)
]

keyItemList: typing.List[ItemData] = [
    ItemData(apKeyItemBaseID + 1, ItemNames.neps_pudding, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 2, ItemNames.compas_syringe, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 3, ItemNames.ifs_notebook, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 4, ItemNames.peashys_drawing, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 5, ItemNames.plutia_doll, ItemClassification.progression_skip_balancing)
]

consumableItemList: typing.List[ItemData] = [
    ItemData(apConsumableItemBaseID + 1, ItemNames.healing_grass, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 2, ItemNames.healing_pod, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 3, ItemNames.healing_drink, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 4, ItemNames.healing_bottle, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 5, ItemNames.nepbull, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 6, ItemNames.nepbull_c, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 7, ItemNames.nepbull_sp, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 8, ItemNames.nepbull_ex, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 9, ItemNames.nepbull_ex2, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 10, ItemNames.healing_circle, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 11, ItemNames.healing_rain, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 12, ItemNames.healing_field, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 13, ItemNames.healing_light, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 14, ItemNames.spcharger, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 15, ItemNames.pspcharger, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 16, ItemNames.pspcharger_2, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 17, ItemNames.hero_drink, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 18, ItemNames.hero_drink_c, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 19, ItemNames.hero_sausage, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 20, ItemNames.blanc_manju, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 21, ItemNames.plump_dogoo, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 22, ItemNames.horsebird_sashimi, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 23, ItemNames.detoxin, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 24, ItemNames.paralaxin, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 25, ItemNames.reflex, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 26, ItemNames.tuffmil, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 27, ItemNames.anti_venom, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 28, ItemNames.anti_paralysis, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 29, ItemNames.anti_seal, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 30, ItemNames.anti_virus, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 31, ItemNames.panacea, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 32, ItemNames.super_panacea, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 33, ItemNames.int_booster, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 34, ItemNames.int_booster_z, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 35, ItemNames.agi_booster, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 36, ItemNames.agi_booster_z, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 37, ItemNames.str_booster, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 38, ItemNames.str_booster_z, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 39, ItemNames.life_fragment, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 40, ItemNames.exuberant_fragment, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 41, ItemNames.exuberant_lump, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 42, ItemNames.angel_wings, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 43, ItemNames.real_angel_wings, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 44, ItemNames.eject_button, ItemClassification.filler)
]
