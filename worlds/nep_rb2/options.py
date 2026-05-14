from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, DefaultOnToggle, Toggle


@dataclass
class NepRb2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
class RandomizedStartCharacter(Toggle):
    """If enabled, starting character is randomized."""
    display_name = "Randomized Start Character"



@dataclass
class NepRb2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    random_character:   RandomizedStartCharacter
    # DeathLink is always on. Always.
    # death_link: DeathLink


    #Deathlink is always on. Always
    # Death_link: Deathlink