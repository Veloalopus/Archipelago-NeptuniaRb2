import typing
from ..LocationData import LocationData

VirtuaForest: typing.List[LocationData] = (
LocationData("Virtua Forest","Gather 1", 54_1, "Gather"),
LocationData("Virtua Forest","Gather 2", 54_2, "Gather"),
LocationData("Virtua Forest","Gather 3", 54_3, "Gather"),
LocationData("Virtua Forest","Gather 4", 54_4, "Gather"),
LocationData("Virtua Forest","Gather 5", 54_5, "Gather"),
)

VirtuaForestTreasures: typing.List[LocationData] = (
LocationData("Virtua Forest","Treasure 1", 54_1, "Treasure"),
LocationData("Virtua Forest","Treasure 2", 54_2, "Treasure"),
LocationData("Virtua Forest","Treasure 3", 54_3, "Treasure"),
LocationData("Virtua Forest","Treasure 4", 54_4, "Treasure"),
LocationData("Virtua Forest","Treasure 5", 54_5, "Treasure"),
)
VirtuaForestEnemies: typing.List[LocationData] = (
LocationData("Virtua Forest","Invader", 155, "Enemy"),
LocationData("Virtua Forest","Jellyfish Dogoo", 110, "Enemy"),
LocationData("Virtua Forest","Forest Guardian", 162, "Enemy"),
LocationData("Virtua Forest","Viral Forest Guardian", 170, "Enemy"),
LocationData("Virtua Forest","Sentientree", 232, "Enemy"),
LocationData("Virtua Forest","Viral Sentientree", 236, "Enemy"),
LocationData("Virtua Forest","Forest Lord", 433, "Big Enemy"),
)