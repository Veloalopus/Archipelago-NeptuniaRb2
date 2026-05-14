import typing
from ..LocationData import LocationData

VirtuaForest: typing.List[LocationData] = (
LocationData("Virtua Forest","Gather 1", 1_1, "Gather"),
LocationData("Virtua Forest","Gather 2", 1_2, "Gather"),
LocationData("Virtua Forest","Gather 3", 1_3, "Gather"),
LocationData("Virtua Forest","Gather 4", 1_4, "Gather"),
)

VirtuaForestTreasures: typing.List[LocationData] = (
LocationData("Virtua Forest","Treasure 1", 1_1, "Treasure"),
LocationData("Virtua Forest","Treasure 2", 1_2, "Treasure"),
LocationData("Virtua Forest","Treasure 3", 1_3, "Treasure"),
)

#VirtuaForestHiddenTreasure: typing.List[LocationData] = (
#LocationData("Virtua Forest","Hidden Treasure 1", 1_1, "Hidden Treasure"),
#LocationData("Virtua Forest","Hidden Treasure 2", 1_2, "Hidden Treasure"),
#LocationData("Virtua Forest","Hidden Treasure 3", 1_3, "Hidden Treasure"),
#)

VirtuaForestEnemies: typing.List[LocationData] = (
LocationData("Virtua Forest","Dogoo", 101, "Enemy"),
LocationData("Virtua Forest","Tulip", 103, "Enemy"),
LocationData("Virtua Forest","Radisher", 106, "Enemy"),
LocationData("Virtua Forest","Real Gamer", 104, "Enemy"),
LocationData("Virtua Forest","Grandogoo", 102, "Enemy"),
LocationData("Virtua Forest","Horsebird Leader", 105, "Enemy"),
#LocationData("Virtua Forest","Dogoo S", 1001, "Scripted"),
#LocationData("Virtua Forest","Grandogoo S", 1002, "Scripted"),
)