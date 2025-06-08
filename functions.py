import random
from lists import character_class_ls, character_race_ls, character_alignment_ls, backgrounds_ls

def Character_Class():
    class_random_val = random.randint(0, len(character_class_ls) - 1)
    return character_class_ls[class_random_val]

def Character_Race():
    race_random_val = random.randint(0, len(character_race_ls) - 1)
    return character_race_ls[race_random_val]

def Character_Alignment():
    alignment_random_val = random.randint(0, len(character_alignment_ls) - 1)
    return character_alignment_ls[alignment_random_val]

def Character_Background():
    background_random_val = random.randint(0, len(backgrounds_ls) - 1)
    return backgrounds_ls[background_random_val]

def Point_Buy_Randomizer():
    pool = 27

    ability_scores = {
        "STR": 8,
        "DEX": 8,
        "CON": 8,
        "INT": 8,
        "WIS": 8,
        "CHA": 8
    }

    def point_cost(val):
        costs = {9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
        return costs.get(val, 0)

    stats = list(ability_scores.keys())
    random.shuffle(stats)

    for stat in stats:
        while True:
            val = random.randint(8, 15)
            cost = point_cost(val)
            if pool - cost >= 0:
                ability_scores[stat] = val
                pool -= cost
                break

    while pool > 0:
        made_progress = False
        for stat in stats:
            current_val = ability_scores[stat]
            if current_val < 15:
                next_val = current_val + 1
                upgrade_cost = point_cost(next_val) - point_cost(current_val)
                if pool - upgrade_cost >= 0:
                    ability_scores[stat] = next_val
                    pool -= upgrade_cost
                    made_progress = True
        if not made_progress:
            break

    return ability_scores, pool

def generate_character():
    ch_race = Character_Race()
    ch_class = Character_Class()
    ch_background = Character_Background()
    ch_alignment = Character_Alignment()
    ch_stats, ch_pool = Point_Buy_Randomizer()

    return {
        'race': ch_race,
        'class': ch_class,
        'background': ch_background,
        'alignment': ch_alignment,
        'stats': ch_stats,
        'remaining_points': ch_pool,
        'message': "This is a good starting point, feel free to build from here or go your own direction... that is half the fun!"
    }
