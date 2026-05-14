import typing
from ..LocationData import LocationData

ArfoiresFactory: typing.List[LocationData] = (
LocationData("Arfoire's Factory","Gather 1", 21_1, "Gather"),
LocationData("Arfoire's Factory","Gather 2", 21_2, "Gather"),
LocationData("Arfoire's Factory","Gather 3", 21_3, "Gather"),
LocationData("Arfoire's Factory","Gather 4", 21_4, "Gather"),
LocationData("Arfoire's Factory","Gather 5", 21_5, "Gather"),
)


ArfoiresFactoryTreasures: typing.List[LocationData] = (
LocationData("Arfoire's Factory","Treasure 1", 21_1, "Treasure"),
LocationData("Arfoire's Factory","Treasure 2", 21_2, "Treasure"),
LocationData("Arfoire's Factory","Treasure 3", 21_3, "Treasure"),
)


ArfoiresFactoryEnemies: typing.List[LocationData] = (
LocationData("Arfoire's Factory","Calicovader", 223, "Enemy"),
LocationData("Arfoire's Factory","Viral Calicovader", 224, "Enemy"),
LocationData("Arfoire's Factory","Aimable", 225, "Enemy"),
LocationData("Arfoire's Factory","Ganglord Panther", 226, "Enemy"),
LocationData("Arfoire's Factory","Lady Sun", 227, "Enemy"),
LocationData("Arfoire's Factory","Viral Lady Sun", 228, "Enemy"),
LocationData("Arfoire's Factory","Self-Defense System", 229, "Big Enemy"),
)