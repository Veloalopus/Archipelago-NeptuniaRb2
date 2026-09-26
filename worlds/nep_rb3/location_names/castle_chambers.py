import typing
from ..LocationData import LocationData

CastleChambers: typing.List[LocationData] = (
LocationData("Castle Chambers","Gather 1", 16_1, "Gather"),
LocationData("Castle Chambers","Gather 2", 16_2, "Gather"),
LocationData("Castle Chambers","Gather 3", 16_3, "Gather"),
LocationData("Castle Chambers","Gather 4", 16_4, "Gather"),
LocationData("Castle Chambers","Gather 5", 16_5, "Gather"),
)

CastleChambersTreasures: typing.List[LocationData] = (
LocationData("Castle Chambers","Treasure 1", 16_1, "Treasure"),
LocationData("Castle Chambers","Treasure 2", 16_2, "Treasure"),
LocationData("Castle Chambers","Treasure 3", 16_3, "Treasure"),
LocationData("Castle Chambers","Treasure 4", 16_4, "Treasure"),
LocationData("Castle Chambers","Treasure 5", 16_5, "Treasure"),
)
CastleChambersEnemies: typing.List[LocationData] = (
LocationData("Castle Chambers","Lowee Soldier", 293, "Enemy"),
LocationData("Castle Chambers","Apeldoom", 199, "Enemy"),
LocationData("Castle Chambers","Aluna", 245, "Enemy"),
LocationData("Castle Chambers","Viral Aluna", 252, "Enemy"),
LocationData("Castle Chambers","Lowee High Guard", 294, "Enemy"),
LocationData("Castle Chambers","Self-Defense System", 420, "Big Enemy"),
)