from . import Nep1RBTestBase
from ..names import DungeonNames,progressiveGear,ItemNames,DungeonIDs
from ..items import dungeonItemList

class TestLocationCheck(Nep1RBTestBase):
    def test_Region(self) -> None:
        region = DungeonNames.adaldik_forest
        items = [self.get_item_by_name("Dungeon Unlock - Adaldik Forest")]
        self.assertFalse(self.can_reach_region(region))
        self.collect([self.get_item_by_name("Character - Neptune")])
        self.assertFalse(self.can_reach_region(region))
        self.collect(items)
        self.assertTrue(self.can_reach_region(region))


    def test_Goal(self) -> None:
        location = "City Center - True Rei Ryghts"
        items = [self.get_item_by_name("Dungeon Unlock - City Center"),self.get_item_by_name("Character - Uni"),self.get_item_by_name("Character - Vert"),self.get_item_by_name("Character - Noire"),self.get_item_by_name("Character - Blanc"),self.get_item_by_name("Character - Rom")]
        self.collect(items)
        gear = [self.get_item_by_name(progressiveGear.neptune_progressive_gear),self.get_item_by_name(progressiveGear.vert_progressive_gear),self.get_item_by_name(progressiveGear.blanc_progressive_gear),self.get_item_by_name(progressiveGear.noire_progressive_gear)]
        self.collect(gear)
        self.collect(gear)
        self.collect(gear)
        self.collect(gear)
        self.assertFalse(self.can_reach_location(location))
        goalItems = [self.get_item_by_name(ItemNames.neps_pudding),self.get_item_by_name(ItemNames.compas_syringe),self.get_item_by_name(ItemNames.ifs_notebook),self.get_item_by_name(ItemNames.stuffed_doll),self.get_item_by_name(ItemNames.peashys_drawing)]
        self.collect(goalItems)
        self.assertTrue(self.can_reach_location(location))
    
    def test_AllRegion(self) -> None:
        items = [self.get_item_by_name("Character - Rom"),self.get_item_by_name("Character - Ram"),self.get_item_by_name("Character - Peashy"),self.get_item_by_name("Character - Uni")]
        self.collect(items)
        gear = [self.get_item_by_name(progressiveGear.rom_progressive_gear),self.get_item_by_name(progressiveGear.ram_progressive_gear),self.get_item_by_name(progressiveGear.peashy_progressive_gear),self.get_item_by_name(progressiveGear.uni_progressive_gear)]
        self.collect(gear)
        self.collect(gear)
        self.collect(gear)
        self.collect(gear)
        for dungeon in DungeonIDs.all_dungeons.keys():
            if "Safe Zone" in dungeon: continue
            if "Game Dimension" == dungeon: continue
            print(dungeon)
            self.assertFalse(self.can_reach_region(dungeon))
        for dungeonUnlock in dungeonItemList.keys():
            self.collect(self.get_item_by_name(dungeonUnlock))
        for dungeon in DungeonIDs.all_dungeons.keys():
            if "Game Dimension" == dungeon: continue
            print(dungeon)
            self.assertTrue(self.can_reach_region(dungeon))
