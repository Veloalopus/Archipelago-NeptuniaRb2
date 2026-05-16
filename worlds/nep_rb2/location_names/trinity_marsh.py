import typing
from ..LocationData import LocationData

TrinityMarsh: typing.List[LocationData] = (
LocationData("Trinity Marsh","Gather 1", 35_1, "Gather"),
LocationData("Trinity Marsh","Gather 2", 35_2, "Gather"),
LocationData("Trinity Marsh","Gather 3", 35_3, "Gather"),
LocationData("Trinity Marsh","Gather 4", 35_4, "Gather"),
LocationData("Trinity Marsh","Gather 5", 35_5, "Gather"),
)


TrinityMarshTreasures: typing.List[LocationData] = (
LocationData("Trinity Marsh","Treasure 1", 34_1, "Treasure"),
LocationData("Trinity Marsh","Treasure 2", 34_2, "Treasure"),
LocationData("Trinity Marsh","Treasure 3", 34_3, "Treasure"),
LocationData("Trinity Marsh","Treasure 4", 34_4, "Treasure"),
)


TrinityMarshEnemies: typing.List[LocationData] = (
LocationData("Trinity Marsh","Tote", 314, "Enemy"),
LocationData("Trinity Marsh","Tempo", 315, "Enemy"),
LocationData("Trinity Marsh","Empole", 316, "Enemy"),
LocationData("Trinity Marsh","Pole", 317, "Enemy"),
LocationData("Trinity Marsh","Totempole", 318, "Enemy"),
LocationData("Trinity Marsh","Royal Dragon", 319, "Big Enemy"),
)