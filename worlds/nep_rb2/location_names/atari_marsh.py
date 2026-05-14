import typing
from ..LocationData import LocationData

AtariMarsh: typing.List[LocationData] = (
LocationData("Atari Marsh","Gather 1", 18_1, "Gather"),
LocationData("Atari Marsh","Gather 2", 18_2, "Gather"),
LocationData("Atari Marsh","Gather 3", 18_3, "Gather"),
LocationData("Atari Marsh","Gather 4", 18_4, "Gather"),
LocationData("Atari Marsh","Gather 5", 18_5, "Gather"),
)


AtariMarshTreasures: typing.List[LocationData] = (
LocationData("Atari Marsh","Treasure 1", 18_1, "Treasure"),
LocationData("Atari Marsh","Treasure 2", 18_2, "Treasure"),
LocationData("Atari Marsh","Treasure 3", 18_3, "Treasure"),
LocationData("Atari Marsh","Treasure 4", 18_4, "Treasure"),
)


AtariMarshEnemies: typing.List[LocationData] = (
LocationData("Atari Marsh","Harevader", 210, "Enemy"),
LocationData("Atari Marsh","Viral Harevader", 211, "Enemy"),
LocationData("Atari Marsh","Met Froggy", 204, "Enemy"),
LocationData("Atari Marsh","Matango", 205, "Enemy"),
LocationData("Atari Marsh","Viral Matango", 206, "Enemy"),
LocationData("Atari Marsh","Plaid Dolphin", 207, "Big Enemy"),
)