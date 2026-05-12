from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, DefaultOnToggle


@dataclass
class NepRb2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool


    #Deathlink is always on. Always
    # Death_link: Deathlink