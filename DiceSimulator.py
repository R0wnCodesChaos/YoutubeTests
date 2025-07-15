import random

dice_rollable = 1 # Dice that can be rolled
dice_rolled = 0 # Dice that have been rolled
dice_multiplier = 1 # Multiplier for the dice roll
dice_crit_chance = 5 # Chance of a critical hit
dice_crit_multiplier = 100 # Multiplier for a critical hit
roll_hystory = [] # History of rolls
dice_type = "d6" # Type of dice to roll, can be "d2", "d4", "d6", "d8", "d10", "d12", "d20", or "d100"
dice_s = 6 # Number of sides on the dice, can be 2, 4, 6, 8, 10, 12, 20, or 100
upgrade_cost = {
    "d8": 3000, 
    "d10":8500, 
    "d12": 12000, 
    "d20": 30000, 
    "d25": 85000,
    "d50": 120000,
    "d80": 300000,
    "d100": 850000,
}
dice_types = ["d6", "d8", "d10", "d12", "d20", "d100"]
dice_sides = {
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100
}

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
    
def dice_ammount_upgrade_cost():
    if dice_s == 6:
        return 1000 * dice_rollable
    elif dice_s == 8:
        return 1500 * dice_rollable
    elif dice_s == 10:
        return 2000 * dice_rollable
    elif dice_s == 12:
        return 2500 * dice_rollable
    elif dice_s == 20:
        return 4500 * dice_rollable
    elif dice_s == 100:
        return 7500 * dice_rollable

def roll_dice(d_rollable, d_type, d_multiplier, d_crit_chance, d_crit_multiplier, doin):
    d_sides = dice_sides[d_type]
    roll = 0

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
            ro = rounder(roll)
            print(f"Your Roll Was Multiplied By {d_crit_multiplier} And Is Now {ro}")
    doin += roll
    print(f"You Now Have {rounder(doin)} Doins")
    menu(doin)

def menu(doin):
    global dice_type, dice_s, dice_rollable, dice_multiplier, dice_crit_chance, dice_crit_multiplier
    print("Welcome To The Dice Simulator!")
    while True:
        print("1. Roll Dice")
        print(f"2. Upgrade Dice, Cost Is {rounder(upgrade_cost[dice_type])} Doins")
        print(f"3. Upgrade Rollable Dice, Cost Is {rounder(dice_ammount_upgrade_cost())} Doins")
        print(f"4. Upgrade Multiplier, Current Multiplier Is {dice_multiplier}, Cost Is {rounder(1000 * dice_multiplier)} Doins")
        print(f"5. Upgrade Critical Hit Chance, Current Chance Is {dice_crit_chance}%, Cost Is {rounder(1000 * dice_crit_chance)} Doins")
        print(f"6. Upgrade Critical Hit Multiplier, Current Multiplier Is {dice_crit_multiplier}, Cost Is {rounder(250 * dice_crit_multiplier)} Doins")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            roll_dice(dice_rollable, dice_type, dice_multiplier, dice_crit_chance, dice_crit_multiplier, doin)
        elif choice == "2":
            if doin >= upgrade_cost[dice_type]:
                doin -= upgrade_cost[dice_type]
                if dice_type == "d6":
                    dice_type = "d8"
                    dice_s = 8
                elif dice_type == "d8":
                    dice_type = "d10"
                    dice_s = 10
                elif dice_type == "d10":
                    dice_type = "d12"
                    dice_s = 12
                elif dice_type == "d12":
                    dice_type = "d20"
                    dice_s = 20
                elif dice_type == "d20":
                    dice_type = "d100"
                    dice_s = 100
                else:
                    print("You Have Reached The Maximum Dice Type!")
            else:
                print(f"You Do Not Have Enough Doins To Upgrade Your Dice, You Need {rounder(upgrade_cost[dice_type])} Doins")
            continue
        elif choice == "3":
            if doin > dice_ammount_upgrade_cost():
                doin -= dice_ammount_upgrade_cost()
                dice_rollable += 1
                print(f"You Have Upgraded Your Rollable Dice To {dice_rollable} Dice")
            else:
                print(f"You Do Not Have Enough Doins To Upgrade Your Rollable Dice, You Need {rounder(dice_ammount_upgrade_cost())} Doins")
            continue
        elif choice == "4":
            if doin >= 1000 * dice_multiplier:
                doin -= 1000 * dice_multiplier
                dice_multiplier += 1
                print(f"You Have Upgraded Your Multiplier To {dice_multiplier}")
            else:
                print(f"You Do Not Have Enough Doins To Upgrade Your Multiplier, You Need {rounder(1000 * dice_multiplier)} Doins")
            continue
        elif choice == "5":
            if doin >= 1000 * dice_crit_chance:
                doin -= 1000 * dice_crit_chance
                dice_crit_chance += 2
                print(f"You Have Upgraded Your Critical Hit Chance To {dice_crit_chance}%")
            elif dice_crit_chance == 100:
                print("You Have Reached The Maximum Critical Hit Chance!")
            else:
                print(f"You Do Not Have Enough Doins To Upgrade Your Critical Hit Chance, You Need {rounder(1000 * dice_crit_chance)} Doins")
            continue
        elif choice == "6":
            if doin >= 250 * dice_crit_multiplier:
                doin -= 250 * dice_crit_multiplier
                dice_crit_multiplier += 50
                print(f"You Have Upgraded Your Critical Hit Multiplier To {dice_crit_multiplier}")
            else:
                print(f"You Do Not Have Enough Doins To Upgrade Your Critical Hit Multiplier, You Need {rounder(250 * dice_crit_multiplier)} Doins")
            continue
        elif choice == "7":
            print("Thank you for using the Dice Simulator!")
            exit()
        else:
            print("Invalid choice, please try again.")
            continue

menu(doin)