import json
from . import Nep2RBTestBase

class TestApWorld(Nep2RBTestBase):
    def test_Region(self) -> None:
        region = "Darkness 60"
        items = [self.get_item_by_name("Dungeon - Darkness 60")]
        self.assertFalse(self.can_reach_region(region))
        self.collect([self.get_item_by_name("Character - Nepgear")])
        self.assertFalse(self.can_reach_region(region))
        self.collect(items)
        self.assertTrue(self.can_reach_region(region))

    def test_Progressive_Gear(self) -> None:
        pass