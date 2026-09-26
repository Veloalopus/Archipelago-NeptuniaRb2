import typing
from ..LocationData import LocationData

PSDimension: typing.List[LocationData] = (
LocationData("PS Dimension","Gather 1", 40_1, "Gather"),
LocationData("PS Dimension","Gather 2", 40_2, "Gather"),
LocationData("PS Dimension","Gather 3", 40_3, "Gather"),
LocationData("PS Dimension","Gather 4", 40_4, "Gather"),
LocationData("PS Dimension","Gather 5", 40_5, "Gather"),
)

PSDimensionTreasures: typing.List[LocationData] = (
LocationData("PS Dimension","Treasure 1", 40_1, "Treasure"),
LocationData("PS Dimension","Treasure 2", 40_2, "Treasure"),
LocationData("PS Dimension","Treasure 3", 40_3, "Treasure"),
LocationData("PS Dimension","Treasure 4", 40_4, "Treasure"),
LocationData("PS Dimension","Treasure 5", 40_5, "Treasure"),
LocationData("PS Dimension","Treasure 6", 40_6, "Treasure"),
)
PSDimensionEnemies: typing.List[LocationData] = (
LocationData("PS Dimension","Plam-met", 318, "Enemy"),
LocationData("PS Dimension","High Heal Dogoo", 107, "Enemy"),
LocationData("PS Dimension","Cuberial", 260, "Enemy"),
LocationData("PS Dimension","Dragon Warrior", 269, "Enemy"),     
LocationData("PS Dimension","Viral Dragon Warrior", 279, "Enemy"),
LocationData("PS Dimension","Giant Dogoo", 517, "Big Enemy"),
)