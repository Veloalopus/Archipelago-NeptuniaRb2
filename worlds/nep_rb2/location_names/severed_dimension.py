import typing
from ..LocationData import LocationData

SeveredDimension: typing.List[LocationData] = (
LocationData("Severed Dimension","Gather 1", 15_1, "Gather"),
LocationData("Severed Dimension","Gather 2", 15_2, "Gather"),
LocationData("Severed Dimension","Gather 3", 15_3, "Gather"),
)


SeveredDimensionTreasures: typing.List[LocationData] = (
LocationData("Severed Dimension","Treasure 1", 15_1, "Treasure"),
LocationData("Severed Dimension","Treasure 2", 15_2, "Treasure"),
LocationData("Severed Dimension","Treasure 3", 15_3, "Treasure"),
LocationData("Severed Dimension","Treasure 4", 15_4, "Treasure"),
)


SeveredDimensionEnemies: typing.List[LocationData] = (
LocationData("Severed Dimension","Weirdo Shadow", 183, "Enemy"),
LocationData("Severed Dimension","Sicko Shadow", 184, "Enemy"),
LocationData("Severed Dimension","Greedy Shadow", 185, "Enemy"),
LocationData("Severed Dimension","Super FX Doctor", 187, "Enemy"),
LocationData("Severed Dimension","ASCII Orchestra", 186, "Enemy"),
LocationData("Severed Dimension","Demonic Fenrir", 188, "Enemy"),
)