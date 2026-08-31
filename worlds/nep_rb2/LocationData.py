from .region_data.region import RegionData,all_dungeon_regions_dict

location_base_id = 7489397493
treasure_base_id = 1000000
enemy_base_id = 2000000
quest_base_id = 4_500_000

class LocationData:
    def __init__(self,region:RegionData, name, id_, itemType,dungeonChange:int=0):
        if itemType == 0:
            itemType = "Gather"
        self.region = region
        self.name = f"{region} - {name}"
        self.objectiven_name = name
        self.itemType = itemType
        self.id = id_
        self.dungeonChange = dungeonChange
        self.plans = []
        if itemType == "Treasure":
            self.id = self.id + treasure_base_id
        if itemType =="Enemy":
            self.id = self.id + enemy_base_id
            self.name = self.objectiven_name
        if itemType =="Big Enemy":
            self.id = self.id + enemy_base_id
            self.name = self.objectiven_name
        if itemType == "Quest":
            self.id = self.id+quest_base_id
            self.name = "Quest - "+self.objectiven_name
            for reg in region:
                reg = all_dungeon_regions_dict[reg]
                if dungeonChange == 1:
                    self.plans.append(reg.changeDungeon)
                if dungeonChange == 2:
                    self.plans.append(reg.bigChangeDungeon)
        else:
            if dungeonChange == 1:
                self.plans.append(region.changeDungeon)
            if dungeonChange == 2:
                self.plans.append(region.bigChangeDungeon)
