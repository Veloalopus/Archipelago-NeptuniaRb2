from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, Toggle

class PostGameRequired(DefaultOnToggle):
    """If enabled, Post Game Dungeons may hold key progression items."""
    display_name = "Post Game Required"


class RandomizedStartCharacter(Toggle):
    """If enabled, starting character is randomized."""
    display_name = "Randomized Start Character"



@dataclass
class NepRb1Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    post_game_required: PostGameRequired
    random_character:   RandomizedStartCharacter
    # DeathLink is always on. Always.
    # death_link: DeathLink
