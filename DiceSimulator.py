import random

dice_rollable = 1 # Dice that can be rolled
dice_rolled = 0 # Dice that have been rolled
roll_hystory = [] # History of rolls
doin = 100 # Curency in the game

def rounder(n): # Function to round numbers for better readability
    if n >= 1000000000000000000000000:
        return str(round(n / 1000000000000000000000000, 2)) + "sp"
    elif n >= 1000000000000000000000:
        return str(round(n / 1000000000000000000000, 2)) + "sx"
    elif n >= 1000000000000000000:
        return str(round(n / 1000000000000000000, 2)) + "qt"
    elif n >= 1000000000000000:
        return str(round(n / 1000000000000000, 2)) + "qa"
    elif n >= 1000000000000:
        return str(round(n / 1000000000000, 2)) + "t"
    elif n >= 1000000000:
        return str(round(n / 1000000000, 2)) + "b"
    elif n >= 1000000:
        return str(round(n / 1000000, 2)) + "m"
    elif n >= 1000:
        return str(round(n / 1000, 2)) + "k"
    else:
        return str(n)

def roll_dice(d_rollable, d_sides, d_multiplier, d_crit_chance, d_crit_multiplier):
    roll = 0
    r = 0
    for i in range(d_rollable):
        r = random.randint(1, d_sides)
        dis = rounder(r)
        print(f"You Rolled {dis} In Your {i + 1}")

        roll += r
    
    ro = rounder(roll)
    print(f"Your Total Roll Is {ro}")

    roll *= d_multiplier
    ro = rounder(roll)
    print(f"Your Roll Multiplier Is {d_multiplier} And Made Your Roll {ro}")

    if d_crit_chance > 0:
        if random.random() < d_crit_chance / 100:
            print("You Rolled A Critical Hit!")
            roll *= d_crit_multiplier
            roll = rounder(roll)
            print(f"Your Roll Was Multiplied By {d_crit_multiplier} And Is Now {roll}")

roll_dice(5, 6, 52, 50, 100)