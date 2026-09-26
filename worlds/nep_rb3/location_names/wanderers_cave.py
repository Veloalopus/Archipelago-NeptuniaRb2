import typing
from ..LocationData import LocationData

WanderersCave: typing.List[LocationData] = (
LocationData("Wanderer's Cave","Gather 1", 6_1, "Gather"),
LocationData("Wanderer's Cave","Gather 2", 6_2, "Gather"),
LocationData("Wanderer's Cave","Gather 3", 6_3, "Gather"),
LocationData("Wanderer's Cave","Gather 4", 6_4, "Gather"),
LocationData("Wanderer's Cave","Gather 5", 6_5, "Gather"),
LocationData("Wanderer's Cave","Gather 6", 6_6, "Gather"),
LocationData("Wanderer's Cave","Gather 7", 6_7, "Gather"),
)
WanderersCaveTreasures: typing.List[LocationData] = (
LocationData("Wanderer's Cave","Treasure 1", 6_1, "Treasure"),
LocationData("Wanderer's Cave","Treasure 2", 6_2, "Treasure"),
LocationData("Wanderer's Cave","Treasure 3", 6_3, "Treasure"),
LocationData("Wanderer's Cave","Treasure 4", 6_4, "Treasure"),
LocationData("Wanderer's Cave","Treasure 5", 6_5, "Treasure"),
)
WanderersCaveEnemies: typing.List[LocationData] = (
LocationData("Wanderer's Cave","Frog-in-the-box", 150, "Enemy"),
LocationData("Wanderer's Cave","Heal Dogoo", 105, "Enemy"),
LocationData("Wanderer's Cave","Crystal Golem", 156, "Enemy"),
LocationData("Wanderer's Cave","Viral Crystal Golem", 164, "Enemy"),
LocationData("Wanderer's Cave","Ice Skeleton", 131, "Enemy"),
LocationData("Wanderer's Cave","Dolphin", 407, "Big Enemy"),
)