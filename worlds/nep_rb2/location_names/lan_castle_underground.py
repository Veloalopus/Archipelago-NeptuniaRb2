import typing
from ..LocationData import LocationData

LANCastleUnderground: typing.List[LocationData] = (
LocationData("LAN Castle - Depths","Gather 1", 25_1, "Gather"),
LocationData("LAN Castle - Depths","Gather 2", 25_2, "Gather"),
LocationData("LAN Castle - Depths","Gather 3", 25_3, "Gather"),
)


LANCastleUndergroundTreasures: typing.List[LocationData] = (
LocationData("LAN Castle - Depths","Treasure 1", 25_1, "Treasure"),
LocationData("LAN Castle - Depths","Treasure 2", 25_2, "Treasure"),
LocationData("LAN Castle - Depths","Treasure 3", 25_3, "Treasure"),
)


LANCastleUndergroundEnemies: typing.List[LocationData] = (
LocationData("LAN Castle - Depths","Deadly Spider", 251, "Enemy"),
LocationData("LAN Castle - Depths","Pinky", 252, "Enemy"),
LocationData("LAN Castle - Depths","Ms. Pinky", 253, "Enemy"),
LocationData("LAN Castle - Depths","Dolichorhynchops", 248, "Big Enemy"),
)