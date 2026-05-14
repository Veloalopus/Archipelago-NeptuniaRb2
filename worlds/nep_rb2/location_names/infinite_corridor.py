import typing
from ..LocationData import LocationData

InfiniteCorridor: typing.List[LocationData] = (
LocationData("Infinite Corridor","Gather 1", 27_1, "Gather"),
LocationData("Infinite Corridor","Gather 2", 27_2, "Gather"),
LocationData("Infinite Corridor","Gather 3", 27_3, "Gather"),
LocationData("Infinite Corridor","Gather 4", 27_4, "Gather"),
LocationData("Infinite Corridor","Gather 5", 27_5, "Gather"),
)


InfiniteCorridorTreasures: typing.List[LocationData] = (
LocationData("Infinite Corridor","Treasure 1", 27_1, "Treasure"),
LocationData("Infinite Corridor","Treasure 2", 27_2, "Treasure"),
LocationData("Infinite Corridor","Treasure 3", 27_3, "Treasure"),
LocationData("Infinite Corridor","Treasure 4", 27_4, "Treasure"),
)


InfiniteCorridorEnemies: typing.List[LocationData] = (
LocationData("Infinite Corridor","Betavader", 263, "Enemy"),
LocationData("Infinite Corridor","Tesrit", 264, "Enemy"),
LocationData("Infinite Corridor","Plom-met", 265, "Enemy"),
LocationData("Infinite Corridor","Guardragon", 266, "Big Enemy"),
)