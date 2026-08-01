import typing
from BaseClasses import Location
from .location_names import gathers,treasures,goalLocation,enemies,questLocation
from .LocationData import LocationData

ap_location_base_id = 696969
class NepRb2Location(Location):
    game = "Hyperdimension Neptunia Re;Birth2 Sisters Generation"


all_locations: typing.List[LocationData] = ()

for map in gathers:
    all_locations += map

for map in treasures:
    all_locations += map

for map in goalLocation:
    all_locations += map

for map in enemies:
    all_locations += map

all_locations += questLocation

location_table: typing.Dict[str, int] = {location.name: location.id for location in all_locations}

