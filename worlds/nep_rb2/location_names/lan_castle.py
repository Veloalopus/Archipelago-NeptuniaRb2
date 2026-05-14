import typing
from ..LocationData import LocationData

LANCastle: typing.List[LocationData] = (
LocationData("LAN Castle","Gather 1", 22_1, "Gather"),
LocationData("LAN Castle","Gather 2", 22_2, "Gather"),
LocationData("LAN Castle","Gather 3", 22_3, "Gather"),
)


LANCastleTreasures: typing.List[LocationData] = (
LocationData("LAN Castle","Treasure 1", 22_1, "Treasure"),
LocationData("LAN Castle","Treasure 2", 22_2, "Treasure"),
LocationData("LAN Castle","Treasure 3", 22_3, "Treasure"),
LocationData("LAN Castle","Treasure 4", 22_4, "Treasure"),
)


LANCastleEnemies: typing.List[LocationData] = (
LocationData("LAN Castle","Baconvader", 232, "Enemy"),
LocationData("LAN Castle","Viral Baconvader", 233, "Enemy"),
LocationData("LAN Castle","Leovader", 236, "Enemy"),
LocationData("LAN Castle","Viral Leovader", 237, "Enemy"),
LocationData("LAN Castle","Speedy", 234, "Enemy"),
LocationData("LAN Castle","Ms. Speedy", 235, "Enemy"),
LocationData("LAN Castle","Nidhogg", 238, "Big Enemy"),
)

# How to handle changed enemies
# Make rule for if "Add Enemies - Lan Castle = True then "Gargoyle" = in logic?
#LANCastleCHEnemies: typing.List[LocationData] = (
#LocationData("LAN Castle","Gargoyle",239,"Big Enemy")
#)