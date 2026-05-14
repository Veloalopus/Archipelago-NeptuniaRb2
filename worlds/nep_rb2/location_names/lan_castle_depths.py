import typing
from ..LocationData import LocationData

LANCastleDepths: typing.List[LocationData] = (
LocationData("LAN Castle Depths","Gather 1", 23_1, "Gather"),
LocationData("LAN Castle Depths","Gather 2", 23_2, "Gather"),
LocationData("LAN Castle Depths","Gather 3", 23_3, "Gather"),
)


LANCastleDepthsTreasures: typing.List[LocationData] = (
LocationData("LAN Castle Depths","Treasure 1", 23_1, "Treasure"),
LocationData("LAN Castle Depths","Treasure 2", 23_2, "Treasure"),
LocationData("LAN Castle Depths","Treasure 3", 23_3, "Treasure"),
)


LANCastleDepthsEnemies: typing.List[LocationData] = (
LocationData("LAN Castle Depths","Blue Sun", 241, "Enemy"),
LocationData("LAN Castle Depths","Viral Blue Sun", 242, "Enemy"),
LocationData("LAN Castle Depths","Numbing Spider", 243, "Enemy"),
LocationData("LAN Castle Depths","Metal Dogoo", 244, "Enemy"),
)