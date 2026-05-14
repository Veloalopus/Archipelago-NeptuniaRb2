location_base_id = 7489397493
treasure_base_id = 1000000
enemy_base_id = 2000000

class LocationData:
    def __init__(self,region, name, id_, itemType):
        if itemType == 0:
            itemType = "Gather"
        self.region = region
        self.name = f"{region} - {name}"
        self.objectiven_name = name
        self.itemType = itemType
        self.id = id_

        if itemType == "Treasure":
            self.id = self.id + treasure_base_id
        if itemType =="Enemy":
            self.id = self.id + enemy_base_id
            self.name = self.objectiven_name
        if itemType =="Big Enemy":
            self.id = self.id + enemy_base_id
            self.name = self.objectiven_name
