## Locations
treasure_base_id = 1_000_000
enemy_base_id = 2_000_000
quest_base_id = 4_500_000

def AddIdOffest(id,type):
    match type:
        case "Quest":
            id = id + quest_base_id
        case "Enemy":
            id = id + enemy_base_id
        case "Treasure":
            id = id + treasure_base_id
    return id