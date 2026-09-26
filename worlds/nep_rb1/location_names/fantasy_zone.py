import typing
from ..LocationData import LocationData

FantasyZone: typing.List[LocationData] = (
LocationData("Fantasy Zone","Gather 1", 17_1, "Gather"),
LocationData("Fantasy Zone","Gather 2", 17_2, "Gather"),
LocationData("Fantasy Zone","Gather 3", 17_3, "Gather"),
LocationData("Fantasy Zone","Gather 4", 17_4, "Gather"),
LocationData("Fantasy Zone","Gather 5", 17_5, "Gather"),
)


FantasyZoneTreasures: typing.List[LocationData] = (
LocationData("Fantasy Zone","Treasure 1", 17_1, "Treasure"),
LocationData("Fantasy Zone","Treasure 2", 17_2, "Treasure"),
LocationData("Fantasy Zone","Treasure 3", 17_3, "Treasure"),
LocationData("Fantasy Zone","Treasure 4", 17_4, "Treasure"),
LocationData("Fantasy Zone","Treasure 5", 17_5, "Treasure"),
)


FantasyZoneEnemies: typing.List[LocationData] = (
LocationData("Fantasy Zone","Plom-met", 193, "Enemy"),
LocationData("Fantasy Zone","Testri", 194, "Enemy"),
LocationData("Fantasy Zone","Malvader", 195, "Enemy"),
LocationData("Fantasy Zone","Cyberfly", 196, "Enemy"),
LocationData("Fantasy Zone","Viral Cyberfly", 197, "Enemy"),
LocationData("Fantasy Zone","Cerberus", 198, "Big Enemy"),
)
