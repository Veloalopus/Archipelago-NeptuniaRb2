from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, DefaultOnToggle, Toggle, Range


@dataclass
class NepRb2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
class RandomizedStartCharacter(Toggle):
    """If enabled, starting character is randomized."""
    display_name = "Randomized Start Character"

class McguffinCountRequired(Range):
    display_name = "Goal Items Needed"
    range_start = 1
    range_end = 20
    default = 15

class McguffinCountTotal(Range):
    display_name = "Goal Items Available"
    range_start = 1
    range_end = 20
    default = 20

@dataclass
class NepRb2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    random_character:   RandomizedStartCharacter
    goal_required: McguffinCountRequired
    goal_total: McguffinCountTotal

    def get_options(self) -> dict[str]:
        return {
            "random_character":self.random_character.value,
            "goal_required":self.goal_required.value
        }

    # DeathLink is always on. Always.
    # death_link: DeathLink


    #Deathlink is always on. Always
    # Death_link: Deathlink