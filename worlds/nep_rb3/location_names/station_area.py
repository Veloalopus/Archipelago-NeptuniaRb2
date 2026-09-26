import typing
from ..LocationData import LocationData

StationArea: typing.List[LocationData] = (
LocationData("Station Area","Gather 1", 2_1, "Gather"),
LocationData("Station Area","Gather 2", 2_2, "Gather"),
LocationData("Station Area","Gather 3", 2_3, "Gather"),
LocationData("Station Area","Gather 4", 2_4, "Gather"),
LocationData("Station Area","Gather 5", 2_5, "Gather"),
LocationData("Station Area","Gather 6", 2_6, "Gather"),
)

StationAreaTreasures: typing.List[LocationData] = (
LocationData("Station Area","Treasure 1", 2_1, "Treasure"),
LocationData("Station Area","Treasure 2", 2_2, "Treasure"),
LocationData("Station Area","Treasure 3", 2_3, "Treasure"),
LocationData("Station Area","Treasure 4", 2_4, "Treasure"),
)

StationAreaEnemies: typing.List[LocationData] = (
LocationData("Station Area","Bit", 123, "Enemy"),
LocationData("Station Area","Dogoo", 101, "Enemy"),
LocationData("Station Area","Deus Man", 239, "Enemy"),
LocationData("Station Area","M-3", 138, "Enemy"),
)
