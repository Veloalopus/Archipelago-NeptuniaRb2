from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, Toggle

class PostGameRequired(DefaultOnToggle):
    """If enabled, Post Game Dungeons may hold key progression items."""
    display_name = "Post Game Required"


class RandomizedStartCharacter(Toggle):
    """If enabled, starting character is randomized."""
    display_name = "Randomized Start Character"

class RandomQuests(Toggle):
    """If enabled, Quest are included as Checks.
    Increases the average clear time by 3-5 hours.
    """
    display_name = "Randomized Quest Rewards"



@dataclass
class NepRb3Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    post_game_required: PostGameRequired
    random_character:   RandomizedStartCharacter
    random_quest: RandomQuests
    def get_options(self):
        return{
            "start_inventory_from_pool":self.start_inventory_from_pool.value,
            "post_game_required":self.post_game_required.value,
            "random_character": self.random_character.value,
            "random_quest": self.random_quest.value,
        }
    # DeathLink is always on. Always.
    # death_link: DeathLink
