import typing
from ..LocationData import LocationData

GapainField: typing.List[LocationData] = (
LocationData("Gapain Field","Gather 1", 12_1, "Gather"),
LocationData("Gapain Field","Gather 2", 12_2, "Gather"),
LocationData("Gapain Field","Gather 3", 12_3, "Gather"),
LocationData("Gapain Field","Gather 4", 12_4, "Gather"),
LocationData("Gapain Field","Gather 5", 12_5, "Gather"),
)


GapainFieldTreasures: typing.List[LocationData] = (
LocationData("Gapain Field","Treasure 1", 12_1, "Treasure"),
LocationData("Gapain Field","Treasure 2", 12_2, "Treasure"),
LocationData("Gapain Field","Treasure 3", 12_3, "Treasure"),
)


GapainFieldEnemies: typing.List[LocationData] = (
LocationData("Gapain Field","Cardbird", 164, "Enemy"),
LocationData("Gapain Field","Sunflowery", 165, "Enemy"),
LocationData("Gapain Field","Viral Sunflowery", 166, "Enemy"),
LocationData("Gapain Field","Pumpkimon", 167, "Enemy"),
LocationData("Gapain Field","Viral Pumpkimon", 168, "Enemy"),
LocationData("Gapain Field","Elemental Dragon", 169, "Big Enemy"),
)