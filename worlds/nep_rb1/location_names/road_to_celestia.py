import typing
from ..LocationData import LocationData

RoadToCelestiaTreasures: typing.List[LocationData] = (
LocationData("Road to Celestia","Treasure 1", 25_1, "Treasure"),
LocationData("Road to Celestia","Treasure 2", 25_2, "Treasure"),
LocationData("Road to Celestia","Treasure 3", 25_3, "Treasure"),
LocationData("Road to Celestia","Treasure 4", 25_4, "Treasure"),
LocationData("Road to Celestia","Treasure 5", 25_5, "Treasure"),
LocationData("Road to Celestia","Treasure 6", 25_6, "Treasure"),
)


RoadToCelestiaEnemies: typing.List[LocationData] = (
LocationData("Road to Celestia","Demon Spider", 240, "Enemy"),
LocationData("Road to Celestia","Skull", 241, "Enemy"),
LocationData("Road to Celestia","Prince Boxbird", 242, "Enemy"),
LocationData("Road to Celestia","Lizard Knight", 238, "Enemy"),
LocationData("Road to Celestia","Viral Lizard Knight", 239, "Enemy"),
LocationData("Road to Celestia","Lost Dragon", 243, "Big Enemy"),
)


RoadToCelestiaGoal: typing.List[LocationData] = (
LocationData("Road to Celestia","True Dragon Arfoire",None,0),
)