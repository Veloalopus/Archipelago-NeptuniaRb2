import typing
from ..LocationData import LocationData

Midcompany: typing.List[LocationData] = (
LocationData("Midcompany","Gather 1", 6_1, "Gather"),
LocationData("Midcompany","Gather 2", 6_2, "Gather"),
LocationData("Midcompany","Gather 3", 6_3, "Gather"),
LocationData("Midcompany","Gather 4", 6_4, "Gather"),
LocationData("Midcompany","Gather 5", 6_5, "Gather"),
LocationData("Midcompany","Gather 6", 6_6, "Gather"),
LocationData("Midcompany","Gather 7", 6_7, "Gather"),
)


MidcompanyTreasures: typing.List[LocationData] = (
LocationData("Midcompany","Treasure 1", 6_1, "Treasure"),
LocationData("Midcompany","Treasure 2", 6_2, "Treasure"),
LocationData("Midcompany","Treasure 3", 6_3, "Treasure"),
LocationData("Midcompany","Treasure 4", 6_4, "Treasure"),
LocationData("Midcompany","Treasure 5", 6_5, "Treasure"),
LocationData("Midcompany","Treasure 6", 6_6, "Treasure"),
LocationData("Midcompany","Treasure 7", 6_7, "Treasure"),
)


MidcompanyEnemies: typing.List[LocationData] = (
LocationData("Midcompany","Dogoo", 101, "Enemy"),
LocationData("Midcompany","Tulip", 103, "Enemy"),
LocationData("Midcompany","Radisher", 106, "Enemy"),
LocationData("Midcompany","Real Gamer", 104, "Enemy"),
LocationData("Midcompany","Grandogoo", 102, "Enemy"),
LocationData("Midcompany","Horsebird Leader", 105, "Enemy"),
)