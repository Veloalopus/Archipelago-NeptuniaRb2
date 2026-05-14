import typing
from ..LocationData import LocationData

Midcompany: typing.List[LocationData] = (
LocationData("Midcompany","Gather 1", 6_1, "Gather"),
LocationData("Midcompany","Gather 2", 6_2, "Gather"),
LocationData("Midcompany","Gather 3", 6_3, "Gather"),
LocationData("Midcompany","Gather 4", 6_4, "Gather"),
)


MidcompanyTreasures: typing.List[LocationData] = (
LocationData("Midcompany","Treasure 1", 6_1, "Treasure"),
LocationData("Midcompany","Treasure 2", 6_2, "Treasure"),
LocationData("Midcompany","Treasure 3", 6_3, "Treasure"),
)


MidcompanyEnemies: typing.List[LocationData] = (
LocationData("Midcompany","Red Dogoo", 129, "Enemy"),
LocationData("Midcompany","Elephantvader", 130, "Enemy"),
LocationData("Midcompany","Viral Elephantvader", 131, "Enemy"),
LocationData("Midcompany","R-4", 132, "Enemy"),
LocationData("Midcompany","Bit", 125, "Enemy"),
LocationData("Midcompany","R4i-SDHC", 133, "Big Enemy"),
)