import typing
from ..LocationData import LocationData

ArioPlateau: typing.List[LocationData] = (
LocationData("Ario Plateau","Gather 1", 27_1, "Gather"),
LocationData("Ario Plateau","Gather 2", 27_2, "Gather"),
LocationData("Ario Plateau","Gather 3", 27_3, "Gather"),
LocationData("Ario Plateau","Gather 4", 27_4, "Gather"),
)

ArioPlateauTreasures: typing.List[LocationData] = (
LocationData("Ario Plateau","Treasure 1", 27_1, "Treasure"),
LocationData("Ario Plateau","Treasure 2", 27_2, "Treasure"),
LocationData("Ario Plateau","Treasure 3", 27_3, "Treasure"),
LocationData("Ario Plateau","Treasure 4", 27_4, "Treasure"),
LocationData("Ario Plateau","Treasure 5", 27_5, "Treasure"),
)
ArioPlateauEnemies: typing.List[LocationData] = (
LocationData("Ario Plateau","Plumindigo", 320, "Enemy"),
LocationData("Ario Plateau","Testri", 324, "Enemy"),
LocationData("Ario Plateau","Red Dogoo", 104, "Enemy"),
LocationData("Ario Plateau","Hachibei", 261, "Enemy"),
LocationData("Ario Plateau","Plaid Dolphin", 408, "Big Enemy"),
)