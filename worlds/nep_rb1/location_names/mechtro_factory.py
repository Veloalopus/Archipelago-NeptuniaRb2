import typing
from ..LocationData import LocationData

MechtroFactory: typing.List[LocationData] = (
LocationData("Mechtro Factory","Gather 1", 102_1, "Gather"),
LocationData("Mechtro Factory","Gather 2", 102_2, "Gather"),
LocationData("Mechtro Factory","Gather 3", 102_3, "Gather"),
LocationData("Mechtro Factory","Gather 4", 102_4, "Gather"),
LocationData("Mechtro Factory","Gather 5", 102_5, "Gather"),
)


MechtroFactoryTreasures: typing.List[LocationData] = (
LocationData("Mechtro Factory","Treasure 1", 102_1, "Treasure"),
LocationData("Mechtro Factory","Treasure 2", 102_2, "Treasure"),
LocationData("Mechtro Factory","Treasure 3", 102_3, "Treasure"),
LocationData("Mechtro Factory","Treasure 4", 102_4, "Treasure"),
)


MechtroFactoryEnemies: typing.List[LocationData] = (
LocationData("Mechtro Factory","Child Wolf", 256, "Enemy"),
LocationData("Mechtro Factory","Viral Child Wolf", 257, "Enemy"),
LocationData("Mechtro Factory","Heal Dogoo", 255, "Enemy"),
LocationData("Mechtro Factory","Heavy Dragoon", 253, "Enemy"),
LocationData("Mechtro Factory","Viral Heavy Dragoon", 254, "Enemy"),
LocationData("Mechtro Factory","Nidhogg", 258, "Enemy"),
)
