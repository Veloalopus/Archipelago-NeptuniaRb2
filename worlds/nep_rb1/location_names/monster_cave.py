import typing
from ..LocationData import LocationData

MonsterCave: typing.List[LocationData] = (
LocationData("Monster Cave","Gather 1", 2_1, "Gather"),
LocationData("Monster Cave","Gather 2", 2_2, "Gather"),
LocationData("Monster Cave","Gather 3", 2_3, "Gather"),
LocationData("Monster Cave","Gather 4", 2_4, "Gather"),
LocationData("Monster Cave","Gather 5", 2_5, "Gather"),
)


MonsterCaveTreasures: typing.List[LocationData] = (
LocationData("Monster Cave","Treasure 1", 2_1, "Treasure"),
LocationData("Monster Cave","Treasure 2", 2_2, "Treasure"),
LocationData("Monster Cave","Treasure 3", 2_3, "Treasure"),
)


MonsterCaveEnemies: typing.List[LocationData] = (
LocationData("Monster Cave","Clyde", 106, "Enemy"),
LocationData("Monster Cave","Super Otaku", 108, "Enemy"),
LocationData("Monster Cave","Contracted Angel", 109, "Enemy"),
LocationData("Monster Cave","Pixelvader", 105, "Enemy"),
LocationData("Monster Cave","Ms. Clyde", 107, "Enemy"),
)
