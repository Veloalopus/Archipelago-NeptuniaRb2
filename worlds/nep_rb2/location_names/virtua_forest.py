import typing
from ..LocationData import LocationData

VirtuaForest: typing.List[LocationData] = (
LocationData("Virtua Forest","Gather 1", 1_1, "Gather"),
LocationData("Virtua Forest","Gather 1", 1_2, "Gather"),
LocationData("Virtua Forest","Gather 1", 1_3, "Gather"),
LocationData("Virtua Forest","Gather 1", 1_4, "Gather"),
)

VirtuaForestTreasures: typing.List[LocationData] = (
LocationData("Virtua Forest","Treasure 1", 1_1, "Treasure"),
LocationData("Virtua Forest","Treasure 1", 1_2, "Treasure"),
LocationData("Virtua Forest","Treasure 1", 1_3, "Treasure"),
)

VirtuaForestHiddenTreasure: typing.List[LocationData] = (
LocationData("Virtua Forest","Hidden Treasure 1", 1_1, "Treasure"),
LocationData("Virtua Forest","Hidden Treasure 2", 1_2, "Treasure"),
LocationData("Virtua Forest","Hidden Treasure 3", 1_3, "Treasure"),
)

VirtuaForestEnemies: typing.List[LocationData] = (
LocationData("Virtua Forest","Dogoo", 1, "Enemy"),
LocationData("Virtua Forest","Tulip", 1, "Enemy"),
LocationData("Virtua Forest","Radisher", 1, "Enemy"),
LocationData("Virtua Forest","Real Gamer", 1, "Enemy"),
LocationData("Virtua Forest","Grandogoo", 1, "Enemy"),
LocationData("Virtua Forest","Horsebird Leader", 1, "Big Enemy"),
)