import typing
from ..LocationData import LocationData

LoweeCastleExterior: typing.List[LocationData] = (
LocationData("Lowee Castle Exterior","Gather 1", 13_1, "Gather"),
LocationData("Lowee Castle Exterior","Gather 2", 13_2, "Gather"),
LocationData("Lowee Castle Exterior","Gather 3", 13_3, "Gather"),
LocationData("Lowee Castle Exterior","Gather 4", 13_4, "Gather"),
LocationData("Lowee Castle Exterior","Gather 5", 13_5, "Gather"),
)

LoweeCastleExteriorTreasures: typing.List[LocationData] = (
LocationData("Lowee Castle Exterior","Treasure 1", 13_1, "Treasure"),
LocationData("Lowee Castle Exterior","Treasure 2", 13_2, "Treasure"),
LocationData("Lowee Castle Exterior","Treasure 3", 13_3, "Treasure"),
LocationData("Lowee Castle Exterior","Treasure 4", 13_4, "Treasure"),
LocationData("Lowee Castle Exterior","Treasure 5", 13_5, "Treasure"),
)
LoweeCastleExteriorEnemies: typing.List[LocationData] = (
LocationData("Lowee Castle Exterior","High Bit", 125, "Enemy"),
LocationData("Lowee Castle Exterior","Lowee Defense Guard", 292, "Enemy"),
LocationData("Lowee Castle Exterior","Child Wolf", 178, "Enemy"),
LocationData("Lowee Castle Exterior","Viral Child Wolf", 184, "Enemy"),
LocationData("Lowee Castle Exterior","Skeleton", 132, "Enemy"),
LocationData("Lowee Castle Exterior","Fenrir", 427, "Big Enemy"),
)