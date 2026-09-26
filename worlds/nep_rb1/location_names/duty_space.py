import typing
from ..LocationData import LocationData

DutySpace: typing.List[LocationData] = (
LocationData("Duty Space","Gather 1", 109_1, "Gather"),
LocationData("Duty Space","Gather 2", 109_2, "Gather"),
LocationData("Duty Space","Gather 3", 109_3, "Gather"),
LocationData("Duty Space","Gather 4", 109_4, "Gather"),
LocationData("Duty Space","Gather 5", 109_5, "Gather"),
)


DutySpaceTreasures: typing.List[LocationData] = (
LocationData("Duty Space","Treasure 1", 109_1, "Treasure"),
LocationData("Duty Space","Treasure 2", 109_2, "Treasure"),
LocationData("Duty Space","Treasure 3", 109_3, "Treasure"),
LocationData("Duty Space","Treasure 4", 109_4, "Treasure"),
LocationData("Duty Space","Treasure 5", 109_5, "Treasure"),
LocationData("Duty Space","Treasure 6", 109_6, "Treasure"),
)


DutySpaceEnemies: typing.List[LocationData] = (
LocationData("Duty Space","Plam-met", 293, "Enemy"),
LocationData("Duty Space","Magic Dogoo", 295, "Enemy"),
LocationData("Duty Space","Cuberial", 294, "Enemy"),
LocationData("Duty Space","Death Stalker", 296, "Enemy"),
LocationData("Duty Space","Viral Death Stalker", 297, "Enemy"),
LocationData("Duty Space","Giant Dogoo", 298, "Big Enemy"),
)
