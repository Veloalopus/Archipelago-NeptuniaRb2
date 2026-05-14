import typing
from ..LocationData import LocationData

IciclePathway: typing.List[LocationData] = (
LocationData("Icicle Pathway","Gather 1", 26_1, "Gather"),
LocationData("Icicle Pathway","Gather 2", 26_2, "Gather"),
LocationData("Icicle Pathway","Gather 3", 26_3, "Gather"),
LocationData("Icicle Pathway","Gather 4", 26_4, "Gather"),
)


IciclePathwayTreasures: typing.List[LocationData] = (
LocationData("Icicle Pathway","Treasure 1", 26_1, "Treasure"),
LocationData("Icicle Pathway","Treasure 2", 26_2, "Treasure"),
LocationData("Icicle Pathway","Treasure 3", 26_3, "Treasure"),
LocationData("Icicle Pathway","Treasure 4", 26_4, "Treasure"),
)


IciclePathwayEnemies: typing.List[LocationData] = (
LocationData("Icicle Pathway","King Cardbird", 256, "Enemy"),
LocationData("Icicle Pathway","Shrotamon", 257, "Enemy"),
LocationData("Icicle Pathway","Viral Shirotamon", 258, "Enemy"),
LocationData("Icicle Pathway","Monkey Balancer", 259, "Enemy"),
LocationData("Icicle Pathway","Vanargandr", 260, "Big Enemy"),
)