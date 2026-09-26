import typing
from ..LocationData import LocationData

Mines: typing.List[LocationData] = (
LocationData("Mines","Gather 1", 21_1, "Gather"),
LocationData("Mines","Gather 2", 21_2, "Gather"),
LocationData("Mines","Gather 3", 21_3, "Gather"),
LocationData("Mines","Gather 4", 21_4, "Gather"),
LocationData("Mines","Gather 5", 21_5, "Gather"),
LocationData("Mines","Gather 6", 21_6, "Gather"),
LocationData("Mines","Gather 7", 21_7, "Gather"),
LocationData("Mines","Gather 8", 21_8, "Gather"),
)

MinesTreasures: typing.List[LocationData] = (
LocationData("Mines","Treasure 1", 21_1, "Treasure"),
LocationData("Mines","Treasure 2", 21_2, "Treasure"),
LocationData("Mines","Treasure 3", 21_3, "Treasure"),
LocationData("Mines","Treasure 4", 21_4, "Treasure"),
LocationData("Mines","Treasure 5", 21_5, "Treasure"),
)
MinesEnemies: typing.List[LocationData] = (
LocationData("Mines","Frozen Skull", 133, "Enemy"),
LocationData("Mines","Ruffian Cat", 288, "Enemy"),
LocationData("Mines","Cold Lizard", 268, "Enemy"),
LocationData("Mines","Viral Cold Lizard", 278, "Enemy"),
LocationData("Mines","Old Man Deus", 241, "Enemy"),
LocationData("Mines","Ice Fenrir", 428, "Big Enemy"),
)