# Import all the essential libraries.

import random
from lists import character_class_ls, character_race_ls, character_alignment_ls, backgrounds_ls


# 
def Character_Class():
   class_random_val = random.randint(0,len(character_class_ls)-1)
   print(f'Class: {character_class_ls[class_random_val]}')


def Character_Race():
   race_random_val = random.randint(0,len(character_race_ls)-1)
   print(f'Race: {character_race_ls[race_random_val]}')


def Character_Alignment():
    alignment_random_val = random.randint(0,len(character_alignment_ls)-1)
    print(f'Alignment: {character_alignment_ls[alignment_random_val]}')


def Character_Background():
    background_random_val = random.randint(0,len(backgrounds_ls)-1)
    print(f'Background: {backgrounds_ls[background_random_val]}')


#Point buy Radomizer: A system that starts with a Value of 8 in all stats and uses a random value to assign point from a pool of 27 point. Depending on the incread it will subtract from the pool of point at varying cost.
#Cost: 8(-0), 9(-1), 10(-2), 11(-3), 12(-4),13(-5),14(-7),15(-9)

def Point_Buy_Randomizer():
    pool = 27 # This is the classic starting ammount for the "point-Buy" system.

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

    # Step 1: Assign all stats to 8 (default), then try random upgrades
    stats = list(ability_scores.keys())
    random.shuffle(stats)  # Shuffle stat order for more variety

    for stat in stats:
        while True:
            val = random.randint(8, 15)
            cost = point_cost(val)
            if pool - cost >= 0:
                ability_scores[stat] = val
                pool -= cost
                break

    # Step 2: Use leftover pool to upgrade stats, if possible
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
   
    print(f"\nFinal stats: {ability_scores}")
    print(f"Remaining point(s): {pool}")

def generate_character():
    ch_race = Character_Race()
    ch_class = Character_Class()
    ch_background = Character_Background()
    ch_alignment = Character_Alignment()
    ch_point_buy = Point_Buy_Randomizer()
    

   return {        
        'race': ch_race,
        'class': ch_class,
        'background': ch_background,
        'alignment': ch_alignment,
        'stats': ch_point_buy  # whatever variable stores your stats
   }