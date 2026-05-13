import typing
from ..LocationData import LocationData

JunkBox: typing.List[LocationData] = (
LocationData("Junk Box","Gather 1", 28_1, "Gather"),
LocationData("Junk Box","Gather 2", 28_2, "Gather"),
LocationData("Junk Box","Gather 3", 28_3, "Gather"),
LocationData("Junk Box","Gather 4", 28_4, "Gather"),
LocationData("Junk Box","Gather 5", 28_5, "Gather"),
LocationData("Junk Box","Gather 6", 28_6, "Gather"),
LocationData("Junk Box","Gather 7", 28_7, "Gather"),
)


JunkBoxTreasures: typing.List[LocationData] = (
LocationData("Junk Box","Treasure 1", 28_1, "Treasure"),
LocationData("Junk Box","Treasure 2", 28_2, "Treasure"),
LocationData("Junk Box","Treasure 3", 28_3, "Treasure"),
LocationData("Junk Box","Treasure 4", 28_4, "Treasure"),
LocationData("Junk Box","Treasure 5", 28_5, "Treasure"),
LocationData("Junk Box","Treasure 6", 28_6, "Treasure"),
LocationData("Junk Box","Treasure 7", 28_7, "Treasure"),
)


JunkBoxEnemies: typing.List[LocationData] = (
LocationData("Junk Box","Dogoo", 101, "Enemy"),
LocationData("Junk Box","Tulip", 103, "Enemy"),
LocationData("Junk Box","Radisher", 106, "Enemy"),
LocationData("Junk Box","Real Gamer", 104, "Enemy"),
LocationData("Junk Box","Grandogoo", 102, "Enemy"),
LocationData("Junk Box","Horsebird Leader", 105, "Enemy"),
)