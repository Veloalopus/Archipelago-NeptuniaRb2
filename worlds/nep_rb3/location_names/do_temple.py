import typing
from ..LocationData import LocationData

DoTemple: typing.List[LocationData] = (
LocationData("Do Temple","Gather 1", 65_1, "Gather"),
LocationData("Do Temple","Gather 2", 65_2, "Gather"),
LocationData("Do Temple","Gather 3", 65_3, "Gather"),
LocationData("Do Temple","Gather 4", 65_4, "Gather"),
LocationData("Do Temple","Gather 5", 65_5, "Gather"),
LocationData("Do Temple","Gather 6", 65_6, "Gather"),
)

DoTempleTreasures: typing.List[LocationData] = (
LocationData("Do Temple","Treasure 1", 65_1, "Treasure"),
LocationData("Do Temple","Treasure 2", 65_2, "Treasure"),
LocationData("Do Temple","Treasure 3", 65_3, "Treasure"),
LocationData("Do Temple","Treasure 4", 65_4, "Treasure"),
LocationData("Do Temple","Treasure 5", 65_5, "Treasure"),
)
DoTempleEnemies: typing.List[LocationData] = (
LocationData("Do Temple","Dinosauroid", 275, "Enemy"),
LocationData("Do Temple","Viral Dinosauroid", 285, "Enemy"),
LocationData("Do Temple","Shimamo's Brother", 309, "Enemy"),
LocationData("Do Temple","Promise Keeper", 263, "Enemy"),
LocationData("Do Temple","M-3D", 148, "Enemy"), 
LocationData("Do Temple","Suzaku", 418, "Big Enemy"),
)