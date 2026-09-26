import typing
from ..LocationData import LocationData

StellaPlains: typing.List[LocationData] = (
LocationData("Stella Plains","Gather 1", 15_1, "Gather"),
LocationData("Stella Plains","Gather 2", 15_2, "Gather"),
LocationData("Stella Plains","Gather 3", 15_3, "Gather"),
LocationData("Stella Plains","Gather 4", 15_4, "Gather"),
)


StellaPlainsTreasures: typing.List[LocationData] = (
LocationData("Stella Plains","Treasure 1", 15_1, "Treasure"),
LocationData("Stella Plains","Treasure 2", 15_2, "Treasure"),
LocationData("Stella Plains","Treasure 3", 15_3, "Treasure"),
)


StellaPlainsEnemies: typing.List[LocationData] = (
LocationData("Stella Plains","Call Boy", 178, "Enemy"),
LocationData("Stella Plains","Cold Girl", 179, "Enemy"),
LocationData("Stella Plains","Lowee Defense Guard", 180, "Enemy"),
LocationData("Stella Plains","Ice Golem", 176, "Enemy"),
LocationData("Stella Plains","Viral Ice Golem", 177, "Enemy"),
LocationData("Stella Plains","King Crab", 181, "Big Enemy"),
)
