import typing
from ..LocationData import LocationData

GraveyardDepths: typing.List[LocationData] = (
LocationData("Graveyard Depths","Gather 1", 24_1, "Gather"),
LocationData("Graveyard Depths","Gather 2", 24_2, "Gather"),
LocationData("Graveyard Depths","Gather 3", 24_3, "Gather"),
)


GraveyardDepthsTreasures: typing.List[LocationData] = (
LocationData("Graveyard Depths","Treasure 1", 24_1, "Treasure"),
LocationData("Graveyard Depths","Treasure 2", 24_2, "Treasure"),
LocationData("Graveyard Depths","Treasure 3", 24_3, "Treasure"),
LocationData("Graveyard Depths","Treasure 4", 24_4, "Treasure"),
)


GraveyardDepthsEnemies: typing.List[LocationData] = (
LocationData("Graveyard Depths","Prince Cardbird", 245, "Enemy"),
LocationData("Graveyard Depths","Dark Disc", 246, "Enemy"),
LocationData("Graveyard Depths","Spotted Plum-met", 247, "Enemy"),
LocationData("Graveyard Depths","Dolichorhynchops", 248, "Big Enemy"),
)