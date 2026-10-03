import json,pkgutil
from importlib.resources import files

from . import Nep2RBTestBase

class TestApWorld(Nep2RBTestBase):
    resources = files(__name__) / '..' / 'resources' / 'items' 
    def test_Region(self) -> None:
        region = "Darkness 60"
        items = [self.get_item_by_name("Dungeon - Darkness 60")]
        self.assertFalse(self.can_reach_region(region))
        self.collect([self.get_item_by_name("Character - Nepgear")])
        self.assertFalse(self.can_reach_region(region))
        self.collect(items)
        self.assertTrue(self.can_reach_region(region))

    def test_Progressive_Gear(self) -> None:
        file = self.resources / 'ProgressiveGear.json'
        file = file.open()
        progessiveGear = json.load(file)
        file.close
        failedChar = []
        for character in progessiveGear:
            if len(character["Power"]) != len(character["Weapon"]):
                failedChar.append(character["Name"])
        self.assertTrue(len(failedChar) == 0,"Not every Weapon tier has a power value!"+",".join(failedChar))
        for character in progessiveGear:
            if character["Maximum_Quantity"] < len(character["Weapon"]):
                failedChar.append(character["Name"])
        self.assertTrue(len(failedChar) == 0,"Not enough Weapons in pool!"+",".join(failedChar))
        
    def test_Goal(self) -> None:
        self.collect_all_but([])
        self.assertTrue(self.can_reach_location("Gamindustri Graveyard - Deity Of Sin Arfoire"))