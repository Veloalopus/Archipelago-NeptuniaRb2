import typing
from ..LocationData import LocationData

LostRuins: typing.List[LocationData] = (
LocationData("Lost Ruins","Gather 1", 32_1, "Gather"),
LocationData("Lost Ruins","Gather 2", 32_2, "Gather"),
LocationData("Lost Ruins","Gather 3", 32_3, "Gather"),
LocationData("Lost Ruins","Gather 4", 32_4, "Gather"),
LocationData("Lost Ruins","Gather 5", 32_5, "Gather"),
)


LostRuinsTreasures: typing.List[LocationData] = (
LocationData("Lost Ruins","Treasure 1", 32_1, "Treasure"),
LocationData("Lost Ruins","Treasure 2", 32_2, "Treasure"),
LocationData("Lost Ruins","Treasure 3", 32_3, "Treasure"),
)


LostRuinsEnemies: typing.List[LocationData] = (
LocationData("Lost Ruins","Custom Bit", 294, "Enemy"),
LocationData("Lost Ruins","Malvader", 295, "Enemy"),
LocationData("Lost Ruins","Killer Spider", 296, "Enemy"),
LocationData("Lost Ruins","Boxer Cat", 297, "Enemy"),
LocationData("Lost Ruins","Heavy Tank", 298, "Big Enemy"),
)