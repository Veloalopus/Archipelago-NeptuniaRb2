from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, DefaultOnToggle, Toggle, Range


@dataclass
class NepRb2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
class RandomizedStartCharacter(Toggle):
    """If enabled, starting character is randomized."""
    display_name = "Randomized Start Character"

class RandomQuests(Toggle):
    """If enabled, Quest are included as Checks.
    Increases the average clear time by X-Y hours.
    """
    display_name = "Randomized Quest Rewards"


@dataclass
class NepRb2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    random_character:   RandomizedStartCharacter

    def get_options(self) -> dict[str]:
        return {
            "start_inventory_from_pool": self.start_inventory_from_pool.value,
            "random_character":self.random_character.value,
            "random_quest": self.random_quest.value,
        }

    # DeathLink is always on. Always.
    # death_link: DeathLink


    #Deathlink is always on. Always
    # Death_link: Deathlink