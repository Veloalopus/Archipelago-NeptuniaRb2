import typing
from ..LocationData import LocationData

NationalFactory: typing.List[LocationData] = (
LocationData("National Factory","Gather 1", 20_1, "Gather"),
LocationData("National Factory","Gather 2", 20_2, "Gather"),
LocationData("National Factory","Gather 3", 20_3, "Gather"),
LocationData("National Factory","Gather 4", 20_4, "Gather"),
LocationData("National Factory","Gather 5", 20_5, "Gather"),
)

NationalFactoryTreasures: typing.List[LocationData] = (
LocationData("National Factory","Treasure 1", 20_1, "Treasure"),
LocationData("National Factory","Treasure 2", 20_2, "Treasure"),
LocationData("National Factory","Treasure 3", 20_3, "Treasure"),
LocationData("National Factory","Treasure 4", 20_4, "Treasure"),
)
NationalFactoryEnemies: typing.List[LocationData] = (
LocationData("National Factory","High Bit Custom", 126, "Enemy"),
LocationData("National Factory","Inky", 209, "Enemy"),
LocationData("National Factory","Ms. Inky", 220, "Enemy"),
LocationData("National Factory","DSTT", 141, "Enemy"),
LocationData("National Factory","Heavy Tank", 421, "Big Enemy"),
)