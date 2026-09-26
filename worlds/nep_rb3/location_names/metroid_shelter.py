import typing
from ..LocationData import LocationData

MetroidShelter: typing.List[LocationData] = (
LocationData("Metroid Shelter","Gather 1", 25_1, "Gather"),
LocationData("Metroid Shelter","Gather 2", 25_2, "Gather"),
LocationData("Metroid Shelter","Gather 3", 25_3, "Gather"),
LocationData("Metroid Shelter","Gather 4", 25_4, "Gather"),
LocationData("Metroid Shelter","Gather 5", 25_5, "Gather"),
)

MetroidShelterTreasures: typing.List[LocationData] = (
LocationData("Metroid Shelter","Treasure 1", 25_1, "Treasure"),
LocationData("Metroid Shelter","Treasure 2", 25_2, "Treasure"),
LocationData("Metroid Shelter","Treasure 3", 25_3, "Treasure"),
LocationData("Metroid Shelter","Treasure 4", 25_4, "Treasure"),
)
MetroidShelterEnemies: typing.List[LocationData] = (
LocationData("Metroid Shelter","Blinky", 211, "Enemy"),
LocationData("Metroid Shelter","Ms. Blinky", 222, "Enemy"),
LocationData("Metroid Shelter","Magma Stone", 197, "Enemy"),
LocationData("Metroid Shelter","Plom-met", 319, "Enemy"),
LocationData("Metroid Shelter","Flame Fenrir", 430, "Big Enemy"),
)