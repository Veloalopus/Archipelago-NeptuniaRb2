import typing
from ..LocationData import LocationData

EndlessZone: typing.List[LocationData] = (
LocationData("Endless Zone","Gather 1", 5_1, "Gather"),
LocationData("Endless Zone","Gather 2", 5_2, "Gather"),
LocationData("Endless Zone","Gather 3", 5_3, "Gather"),
LocationData("Endless Zone","Gather 4", 5_4, "Gather"),
LocationData("Endless Zone","Gather 5", 5_5, "Gather"),
)


EndlessZoneTreasures: typing.List[LocationData] = (
LocationData("Endless Zone","Treasure 1", 5_1, "Treasure"),
LocationData("Endless Zone","Treasure 2", 5_2, "Treasure"),
LocationData("Endless Zone","Treasure 3", 5_3, "Treasure"),
LocationData("Endless Zone","Treasure 4", 5_4, "Treasure"),
)


EndlessZoneEnemies: typing.List[LocationData] = (
LocationData("Endless Zone","Bit", 125, "Enemy"),
LocationData("Endless Zone","Delinquent Cat", 118, "Enemy"),
LocationData("Endless Zone","Bomb-omburai", 126, "Enemy"),
LocationData("Endless Zone","Fenrisulfr", 116, "Big Enemy"),
)