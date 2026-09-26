import typing
from ..LocationData import LocationData

GraphicPass: typing.List[LocationData] = (
LocationData("Graphic Pass","Gather 1", 50_1, "Gather"),
LocationData("Graphic Pass","Gather 2", 50_2, "Gather"),
LocationData("Graphic Pass","Gather 3", 50_3, "Gather"),
LocationData("Graphic Pass","Gather 4", 50_4, "Gather"),
LocationData("Graphic Pass","Gather 5", 50_5, "Gather"),
LocationData("Graphic Pass","Gather 6", 50_6, "Gather"),
)

GraphicPassTreasures: typing.List[LocationData] = (
LocationData("Graphic Pass","Treasure 1", 50_1, "Treasure"),
LocationData("Graphic Pass","Treasure 2", 50_2, "Treasure"),
LocationData("Graphic Pass","Treasure 3", 50_3, "Treasure"),
LocationData("Graphic Pass","Treasure 4", 50_4, "Treasure"),
)
GraphicPassEnemies: typing.List[LocationData] = (
LocationData("Graphic Pass","Tetrisi", 326, "Enemy"),
LocationData("Graphic Pass","Cass Trap", 203, "Enemy"),
LocationData("Graphic Pass","Old Death", 243, "Enemy"),
LocationData("Graphic Pass","Nue", 116, "Enemy"),
LocationData("Graphic Pass","Viral Nue", 121, "Enemy"),
LocationData("Graphic Pass","Orthros", 432, "Big Enemy"),
)