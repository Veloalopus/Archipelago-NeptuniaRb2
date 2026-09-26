import typing
from ..LocationData import LocationData

LoweeCastleInterior: typing.List[LocationData] = (
LocationData("Lowee Castle Interior","Gather 1", 14_1, "Gather"),
LocationData("Lowee Castle Interior","Gather 2", 14_2, "Gather"),
LocationData("Lowee Castle Interior","Gather 3", 14_3, "Gather"),
LocationData("Lowee Castle Interior","Gather 4", 14_4, "Gather"),
LocationData("Lowee Castle Interior","Gather 5", 14_5, "Gather"),
)

LoweeCastleInteriorTreasures: typing.List[LocationData] = (
LocationData("Lowee Castle Interior","Treasure 1", 14_1, "Treasure"),
LocationData("Lowee Castle Interior","Treasure 2", 14_2, "Treasure"),
LocationData("Lowee Castle Interior","Treasure 3", 14_3, "Treasure"),
LocationData("Lowee Castle Interior","Treasure 4", 14_4, "Treasure"),
LocationData("Lowee Castle Interior","Treasure 5", 14_5, "Treasure"),
)
LoweeCastleInteriorEnemies: typing.List[LocationData] = (    
LocationData("Lowee Castle Interior","Child Wolf", 178, "Enemy"),
LocationData("Lowee Castle Interior","Viral Child Wolf", 184, "Enemy"),
LocationData("Lowee Castle Interior","Lowee Defense Guard", 292, "Enemy"),
LocationData("Lowee Castle Interior","Strange Person", 240, "Enemy"),
LocationData("Lowee Castle Interior","Skeleton", 132, "Enemy"),
LocationData("Lowee Castle Interior","Fenrir", 427, "Big Enemy"),
)