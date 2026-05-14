import typing
from ..LocationData import LocationData

GamindustriGraveyard: typing.List[LocationData] = (
LocationData("Gamindustri Graveyard","Gather 1", 20_1, "Gather"),
LocationData("Gamindustri Graveyard","Gather 2", 20_2, "Gather"),
LocationData("Gamindustri Graveyard","Gather 3", 20_3, "Gather"),
LocationData("Gamindustri Graveyard","Gather 4", 20_4, "Gather"),
LocationData("Gamindustri Graveyard","Gather 5", 20_5, "Gather"),
)


GamindustriGraveyardTreasures: typing.List[LocationData] = (
LocationData("Gamindustri Graveyard","Treasure 1", 20_1, "Treasure"),
LocationData("Gamindustri Graveyard","Treasure 2", 20_2, "Treasure"),
LocationData("Gamindustri Graveyard","Treasure 3", 20_3, "Treasure"),
)


GamindustriGraveyardEnemies: typing.List[LocationData] = (
LocationData("Gamindustri Graveyard","Swinevader", 216, "Enemy"),
LocationData("Gamindustri Graveyard","Viral Swinevader", 217, "Enemy"),
LocationData("Gamindustri Graveyard","Inky", 218, "Enemy"),
LocationData("Gamindustri Graveyard","Ms. Inky", 219, "Enemy"),
LocationData("Gamindustri Graveyard","Disc", 220, "Enemy"),
LocationData("Gamindustri Graveyard","Plaid Dolphin", 207, "Big Enemy"),
)




GraveyardGoal: typing.List[LocationData] = (
LocationData("Gamindustri Graveyard","Deity Of Sin Arfoire",None,0),
)