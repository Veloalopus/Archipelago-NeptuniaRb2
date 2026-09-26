import typing
from ..LocationData import LocationData

MagmaCaveDepths: typing.List[LocationData] = (
LocationData("Magma Cave Depths","Gather 1", 32_1, "Gather"),
LocationData("Magma Cave Depths","Gather 2", 32_2, "Gather"),
LocationData("Magma Cave Depths","Gather 3", 32_3, "Gather"),
LocationData("Magma Cave Depths","Gather 4", 32_4, "Gather"),
LocationData("Magma Cave Depths","Gather 5", 32_5, "Gather"),
)

MagmaCaveDepthsTreasures: typing.List[LocationData] = (
LocationData("Magma Cave Depths","Treasure 1", 32_1, "Treasure"),
LocationData("Magma Cave Depths","Treasure 2", 32_2, "Treasure"),
LocationData("Magma Cave Depths","Treasure 3", 32_3, "Treasure"),
LocationData("Magma Cave Depths","Treasure 4", 32_4, "Treasure"),
)
MagmaCaveDepthsEnemies: typing.List[LocationData] = (
LocationData("Magma Cave Depths","King Cardbird", 175, "Enemy"), 
LocationData("Magma Cave Depths","Magma Crab", 301, "Enemy"),
LocationData("Magma Cave Depths","Viral Magma Crab", 304, "Enemy"),
LocationData("Magma Cave Depths","Flame Skeleton", 135, "Enemy"),
LocationData("Magma Cave Depths","Rafflesia", 247, "Enemy"),
LocationData("Magma Cave Depths","Viral Rafflesia", 254, "Enemy"),
LocationData("Magma Cave Depths","Dolichorhynchops", 410, "Big Enemy"),
)