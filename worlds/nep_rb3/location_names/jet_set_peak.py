import typing
from ..LocationData import LocationData

JetSetPeak: typing.List[LocationData] = (
LocationData("Jet Set Peak","Gather 1", 5_1, "Gather"),
LocationData("Jet Set Peak","Gather 2", 5_2, "Gather"),
LocationData("Jet Set Peak","Gather 3", 5_3, "Gather"),
LocationData("Jet Set Peak","Gather 4", 5_4, "Gather"),
LocationData("Jet Set Peak","Gather 5", 5_5, "Gather"),
)

JetSetPeakTreasures: typing.List[LocationData] = (
LocationData("Jet Set Peak","Treasure 1", 5_1, "Treasure"),
LocationData("Jet Set Peak","Treasure 2", 5_2, "Treasure"),
LocationData("Jet Set Peak","Treasure 3", 5_3, "Treasure"),
LocationData("Jet Set Peak","Treasure 4", 5_4, "Treasure"),
LocationData("Jet Set Peak","Treasure 5", 5_5, "Treasure"),
)
JetSetPeakEnemies: typing.List[LocationData] = (
LocationData("Jet Set Peak","Pal Shell", 195, "Enemy"), 
LocationData("Jet Set Peak","Shoebill", 113, "Enemy"),
LocationData("Jet Set Peak","Viral Shoebill", 118, "Enemy"),
LocationData("Jet Set Peak","Fungus", 264, "Enemy"),
LocationData("Jet Set Peak","Alraune", 244, "Enemy"),
LocationData("Jet Set Peak","Viral Alraune", 251, "Enemy"),
LocationData("Jet Set Peak","Ancient Dragon", 401, "Big Enemy"),
)