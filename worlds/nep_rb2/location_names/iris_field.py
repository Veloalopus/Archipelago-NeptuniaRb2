import typing
from ..LocationData import LocationData

IrisField: typing.List[LocationData] = (
LocationData("Iris Field","Gather 1", 17_1, "Gather"),
LocationData("Iris Field","Gather 2", 17_2, "Gather"),
LocationData("Iris Field","Gather 3", 17_3, "Gather"),
LocationData("Iris Field","Gather 4", 17_4, "Gather"),
LocationData("Iris Field","Gather 5", 17_5, "Gather"),
LocationData("Iris Field","Gather 6", 17_6, "Gather"),
)


IrisFieldTreasures: typing.List[LocationData] = (
LocationData("Iris Field","Treasure 1", 17_1, "Treasure"),
LocationData("Iris Field","Treasure 2", 17_2, "Treasure"),
LocationData("Iris Field","Treasure 3", 17_3, "Treasure"),
)


IrisFieldEnemies: typing.List[LocationData] = (
LocationData("Iris Field","Rabbit Balancer", 195, "Enemy"),
LocationData("Iris Field","Moulin Rouge", 196, "Enemy"),
LocationData("Iris Field","Viral Moulin Rouge", 197, "Enemy"),
LocationData("Iris Field","Meow", 198, "Enemy"),
LocationData("Iris Field","Forest Turtle", 199, "Big Enemy"),
)