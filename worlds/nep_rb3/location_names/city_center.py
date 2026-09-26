import typing
from ..LocationData import LocationData

CityCenter: typing.List[LocationData] = (
LocationData("City Center","Gather 1", 34_1, "Gather"),
LocationData("City Center","Gather 2", 34_2, "Gather"),
LocationData("City Center","Gather 3", 34_3, "Gather"),
LocationData("City Center","Gather 4", 34_4, "Gather"),
LocationData("City Center","Gather 5", 34_5, "Gather"),
)

CityCenterTreasures: typing.List[LocationData] = (
LocationData("City Center","Treasure 1", 34_1, "Treasure"),
LocationData("City Center","Treasure 2", 34_2, "Treasure"),
LocationData("City Center","Treasure 3", 34_3, "Treasure"),
LocationData("City Center","Treasure 4", 34_4, "Treasure"),
LocationData("City Center","Treasure 5", 34_5, "Treasure"),
)
CityCenterEnemies: typing.List[LocationData] = (
LocationData("City Center","Numbing Spider", 315, "Enemy"),
LocationData("City Center","R-4 Custom", 144, "Enemy"),
LocationData("City Center","Promise Ring", 262, "Enemy"),
LocationData("City Center","High Lizard", 273, "Enemy"),
LocationData("City Center","Viral High Lizard", 282, "Enemy"),
LocationData("City Center","Crescent Dragon", 405, "Big Enemy"),
)

CityCenterLevels: typing.List[LocationData] = (
LocationData("City Center","Level 70", None,0),

)

CityCenterGoal: typing.List[LocationData] = (
LocationData("City Center","True Rei Ryghts",None,0),
)

