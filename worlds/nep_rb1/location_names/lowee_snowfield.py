import typing
from ..LocationData import LocationData

LoweeSnowfield: typing.List[LocationData] = (
LocationData("Lowee Snowfield","Gather 1", 12_1, "Gather"),
LocationData("Lowee Snowfield","Gather 2", 12_2, "Gather"),
LocationData("Lowee Snowfield","Gather 3", 12_3, "Gather"),
LocationData("Lowee Snowfield","Gather 4", 12_4, "Gather"),
LocationData("Lowee Snowfield","Gather 5", 12_5, "Gather"),
)


LoweeSnowfieldTreasures: typing.List[LocationData] = (
LocationData("Lowee Snowfield","Treasure 1", 12_1, "Treasure"),
LocationData("Lowee Snowfield","Treasure 2", 12_2, "Treasure"),
LocationData("Lowee Snowfield","Treasure 3", 12_3, "Treasure"),
)


LoweeSnowfieldEnemies: typing.List[LocationData] = (
LocationData("Lowee Snowfield","Frozen Skull", 164, "Enemy"),
LocationData("Lowee Snowfield","Violent Good Girl", 165, "Enemy"),
LocationData("Lowee Snowfield","Lowee Soldier", 163, "Enemy"),
LocationData("Lowee Snowfield","Gold Lizard", 161, "Enemy"),
LocationData("Lowee Snowfield","Viral Gold Lizard", 162, "Enemy"),
LocationData("Lowee Snowfield","Plaid Dolphin", 166, "Big Enemy"),
)
