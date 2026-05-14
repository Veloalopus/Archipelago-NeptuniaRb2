import typing
from ..LocationData import LocationData

JunkBox: typing.List[LocationData] = (
LocationData("Junk Box","Gather 1", 28_1, "Gather"),
LocationData("Junk Box","Gather 2", 28_2, "Gather"),
LocationData("Junk Box","Gather 3", 28_3, "Gather"),
LocationData("Junk Box","Gather 4", 28_4, "Gather"),
)


JunkBoxTreasures: typing.List[LocationData] = (
LocationData("Junk Box","Treasure 1", 28_1, "Treasure"),
LocationData("Junk Box","Treasure 2", 28_2, "Treasure"),
LocationData("Junk Box","Treasure 3", 28_3, "Treasure"),
LocationData("Junk Box","Treasure 4", 28_4, "Treasure"),
)


JunkBoxEnemies: typing.List[LocationData] = (
LocationData("Junk Box","Nanovader", 269, "Enemy"),
LocationData("Junk Box","Testri", 272, "Enemy"),
LocationData("Junk Box","Plam-met", 271, "Enemy"),
LocationData("Junk Box","Stalking Sister", 270, "Enemy"),
LocationData("Junk Box","Dagon", 273, "Big Enemy"),
)