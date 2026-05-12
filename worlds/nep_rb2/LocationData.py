location_base_id = 5239857209
treasure_base_id = 1000000
enemy_base_id = 2000000


class LocationData:
    def __init__(self,region, name, id_, itemType):

        self.region = region
        self.name = f"{region} - {name}"
        self.objectiven_name = name
        self.itemType = itemType
        self.id = id_