tiers_power = {"1": 4, "2": 6, "3": 8, "4": 12, "5": 15, "6": 20, "7": 25, "8": 33, "9": 45, "10": 60, "11": 80, "12": 100}
tiers_capacity_A_I = {"1": 10, "2": 12, "3": 14, "4": 16, "5": 18, "6": 18, "7": 20, "8": 22, "9": 24, "10": 26, "11": 28, "12": 30}
tiers_capacity_C = {"1": 8, "2": 8, "3": 10, "4": 12, "5": 12, "6": 14, "7": 14, "8": 16, "9": 16, "10": 18, "11": 20, "12": 22}
tiers_capacity_V = {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}

cost_V = {"food": {"1": 27, "2": 50, "3": 154, "4": 98, "5": 100, "6": 179, "7": 230, "8": 177, "9": 262, "10": 280, "11": 443, "12": 0}
          , "wood": {"1": 0, "2": 30, "3": 43, "4": 63, "5": 91, "6": 125, "7": 174, "8": 190, "9": 262, "10": 358, "11": 470, "12": 0}
          , "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 2, "6": 4, "7": 8, "8": 7, "9": 15, "10": 18, "11": 36, "12": 0}
          , "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 2, "10": 3, "11": 7, "12": 0}}

cost_C = {"food": {"1": 48, "2": 68, "3": 94, "4": 128, "5": 182, "6": 235, "7": 316, "8": 392, "9": 411, "10": 514, "11": 581, "12": 0}
          , "wood": {"1": 0, "2": 15, "3": 21, "4": 31, "5": 45, "6": 62, "7": 87, "8": 120, "9": 131, "10": 179, "11": 235, "12": 0}
          , "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 3, "6": 6, "7": 10, "8": 17, "9": 21, "10": 33, "11": 47, "12": 0}
          , "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 1, "9": 2, "10": 5, "11": 9, "12": 0}}

cost_A = {"food": {"1": 45, "2": 61, "3": 90, "4": 121, "5": 165, "6": 223, "7": 287, "8": 373, "9": 472, "10": 467, "11": 553, "12": 0}
          , "wood": {"1": 0, "2": 19, "3": 26, "4": 41, "5": 54, "6": 75, "7": 113, "8": 156, "9": 199, "10": 233, "11": 282, "12": 0}
          , "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 3, "6": 6, "7": 10, "8": 16, "9": 25, "10": 30, "11": 45, "12": 0}
          , "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 1, "9": 3, "10": 5, "11": 8, "12": 0}}

cost_I = {"food": {"1": 54, "2": 61, "3": 108, "4": 121, "5": 199, "6": 223, "7": 345, "8": 373, "9": 566, "10": 467, "11": 0, "12": 0}
          , "wood": {"1": 0, "2": 19, "3": 21, "4": 38, "5": 45, "6": 75, "7": 87, "8": 144, "9": 165, "10": 215, "11": 0, "12": 0}
          , "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 4, "6": 6, "7": 11, "8": 16, "9": 30, "10": 30, "11": 0, "12": 0}
          , "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 1, "9": 4, "10": 5, "11": 0, "12": 0}}

time_to_train = {"1": 6, "2": 7, "3": 10, "4": 13, "5": 17, "6": 22, "7": 29, "8": 38, "9": 50, "10": 100, "11": 0} # Time to train troops in seconds

def rounder(n): # Function to round numbers for better readability
    if n >= 1000000000:
        return str(round(n / 1000000000, 2)) + "b"
    elif n >= 1000000:
        return str(round(n / 1000000, 2)) + "m"
    elif n >= 1000:
        return str(round(n / 1000, 2)) + "k"
    else:
        return str(n)


def get_tier_power(tier): # Function to get the power of a troop based on its tier
    power = tiers_power[tier]
    return power
def get_tier_capacity(tier, troop_type): # Function to get the capacity of a troop based on its tier and type
    if troop_type == "A" or troop_type == "I":
        capacity = tiers_capacity_A_I[tier]
    elif troop_type == "C":
        capacity = tiers_capacity_C[tier]
    elif troop_type == "V":
        capacity = tiers_capacity_V[tier]
    return capacity
def get_tier_cost(tier, troop_type, amount): # Function to get the cost of a troop based on its tier and type
    if tier == 12:
        print("Tier 12 troop cost are not available yet.")
    elif troop_type == "A":
        cost_food = cost_A["food"][tier]
        cost_wood = cost_A["wood"][tier]
        cost_stone = cost_A["stone"][tier]
        cost_iron = cost_A["iron"][tier]
    elif troop_type == "I":
        cost_food = cost_I["food"][tier]
        cost_wood = cost_I["wood"][tier]
        cost_stone = cost_I["stone"][tier]
        cost_iron = cost_I["iron"][tier]
    elif troop_type == "C":
        cost_food = cost_C["food"][tier]
        cost_wood = cost_C["wood"][tier]
        cost_stone = cost_C["stone"][tier]
        cost_iron = cost_C["iron"][tier]
    elif troop_type == "V":
        cost_food = cost_V["food"][tier]
        cost_wood = cost_V["wood"][tier]
        cost_stone = cost_V["stone"][tier]
        cost_iron = cost_V["iron"][tier]
    cost_food = cost_food * amount  # Multiply the cost by the amount of troops
    cost_wood = cost_wood * amount  
    cost_stone = cost_stone * amount  
    cost_iron = cost_iron * amount  
    cost_food = rounder(cost_food)  # Round the cost for better readability
    cost_wood = rounder(cost_wood)  
    cost_stone = rounder(cost_stone)  
    cost_iron = rounder(cost_iron)  
    cost = f"Food: {cost_food},\nWood: {cost_wood}\nStone: {cost_stone}\nIron: {cost_iron}"  # Format the cost string
    return cost

def get_info(): # Function to get user input for tier, type, and amount of troops
    while True:
        troop_tier = input("Enter the troop tier (1-12): ")
        if troop_tier in tiers_power:
            break
        else:
            print("Invalid tier. Please enter a number between 1 and 12.")
            continue
    while True: # Loop to ensure valid troop type input
        troop_type = input("Enter the troop type (A for Archers, I for Infantry, C for Calvery, V for Vehicle): ").upper()
        if troop_type in ["A", "I", "C", "V"]:
            break
        else:
            print("Invalid troop type. Please enter A, I, C, or V.")
            continue
    troop_amount = input("Enter the amount of troops your either training or have: ")
    while not troop_amount.isdigit():  # Ensure the amount is a digit
        print("Invalid amount. Please enter a valid number.")
        troop_amount = input("Enter the amount of troops your either training or have: ")
    troop_amount = int(troop_amount)
    return troop_tier, troop_type, troop_amount

def do_math(tier, type, amount): # Function to calculate total power and capacity based on tier, type, and amount
    total_power = get_tier_power(tier) * (amount)
    total_capacity = get_tier_capacity(tier, type) * (amount)
    total_power = rounder(total_power)  # Round the total power for better readability
    total_capacity = rounder(total_capacity)  # Round the total capacity for better readability
    
    return total_power, total_capacity

def check_if_digit(speedup_type):
    while True:
        value = input(f"How many {speedup_type} speed ups do you have? ")
        if value.isdigit():
            print(f'You have {value} "{speedup_type} speed ups".')
            return int(value)
        else:
            print("Invalid input. Please enter a valid number.")

def get_max_troop_training():
    while True:
        troop_tier = input("Enter the troop tier (1-12): ")
        if troop_tier not in time_to_train:
            print("Invalid tier. Please enter a number between 1 and 11.")
            continue
        else:
            break
    while True: # Loop to ensure valid troop type input
        troop_type = input("Enter the troop type (A for Archers, I for Infantry, C for Calvery, V for Vehicle): ").upper()
        if troop_type in ["A", "I", "C", "V"]:
            break
        else:
            print("Invalid troop type. Please enter A, I, C, or V.")
            continue

    one_m = check_if_digit("1 Minute")
    five_m = check_if_digit("5 Minute")
    ten_m = check_if_digit("10 Minute")
    fifteen_m = check_if_digit("15 Minute")
    thirty_m = check_if_digit("30 Minute")
    sixty_m = check_if_digit("1 Hour")
    three_h = check_if_digit("3 Hour")
    eight_h = check_if_digit("8 Hour")
    fifteen_h = check_if_digit("15 Hour")
    twenty_four_h = check_if_digit("24 Hour")
    three_d = check_if_digit("3 Day")
    seven_d = check_if_digit("7 Day")

    total_speedup_time = (
        one_m * 60 +
        five_m * 300 +
        ten_m * 600 +
        fifteen_m * 900 +
        thirty_m * 1800 +
        sixty_m * 3600 +
        three_h * 10800 +
        eight_h * 28800 +
        fifteen_h * 54000 +
        twenty_four_h * 86400 +
        three_d * 259200 +
        seven_d * 604800
    )

    print(f"Total speedup time in minutes: {round(total_speedup_time / 60)}")
    print(f"Total speedup time in hours: {round(total_speedup_time / 3600)}")
    print(f"Total speedup time in days: {round(total_speedup_time / 86400)}")
    resource_amount_food = input("Enter the amount of food you have in total: ")
    while not resource_amount_food.isdigit():  # Ensure the amount is a digit
        print("Invalid amount. Please enter a valid number.")
        resource_amount_food = input("Enter the amount of food you have in total: ")
    resource_amount_food = int(resource_amount_food)
    resource_amount_wood = input("Enter the amount of wood you have in total: ")
    while not resource_amount_wood.isdigit():  # Ensure the amount is a digit
        print("Invalid amount. Please enter a valid number.")
        resource_amount_wood = input("Enter the amount of wood you have in total: ")
    resource_amount_wood = int(resource_amount_wood)
    resource_amount_stone = input("Enter the amount of stone you have in total: ")
    while not resource_amount_stone.isdigit():  # Ensure the amount is a digit
        print("Invalid amount. Please enter a valid number.")
        resource_amount_stone = input("Enter the amount of stone you have in total: ")
    resource_amount_stone = int(resource_amount_stone)
    resource_amount_iron = input("Enter the amount of iron you have in total: ")
    while not resource_amount_iron.isdigit():  # Ensure the amount is a digit
        print("Invalid amount. Please enter a valid number.")
        resource_amount_iron = input("Enter the amount of iron you have in total: ")
    resource_amount_iron = int(resource_amount_iron)

    if troop_type == "A":
        cost_food = cost_A["food"][troop_tier]
        cost_wood = cost_A["wood"][troop_tier]
        cost_stone = cost_A["stone"][troop_tier]
        cost_iron = cost_A["iron"][troop_tier]
    elif troop_type == "I":
        cost_food = cost_I["food"][troop_tier]
        cost_wood = cost_I["wood"][troop_tier]
        cost_stone = cost_I["stone"][troop_tier]
        cost_iron = cost_I["iron"][troop_tier]
    elif troop_type == "C":
        cost_food = cost_C["food"][troop_tier]
        cost_wood = cost_C["wood"][troop_tier]
        cost_stone = cost_C["stone"][troop_tier]
        cost_iron = cost_C["iron"][troop_tier]
    elif troop_type == "V":
        cost_food = cost_V["food"][troop_tier]
        cost_wood = cost_V["wood"][troop_tier]
        cost_stone = cost_V["stone"][troop_tier]
        cost_iron = cost_V["iron"][troop_tier]
  
    food_trainable = resource_amount_food // cost_food
    wood_trainable = resource_amount_wood // cost_wood
    stone_trainable = resource_amount_stone // cost_stone
    iron_trainable = resource_amount_iron // cost_iron
    train_time = time_to_train[troop_tier]  # Get the training time for the specified tier
    time_trainable = total_speedup_time // train_time  # Calculate the total trainable time based on speedups
    max_trainable = round(min(food_trainable, wood_trainable, stone_trainable, iron_trainable, time_trainable))  # Get the minimum of all trainable resources and time
    print(f"Based on your resources and speedups, you can train a maximum of {max_trainable} troops of tier {troop_tier}.")

    trainable_factors = {
    "food": food_trainable,
    "wood": wood_trainable,
    "stone": stone_trainable,
    "iron": iron_trainable,
    "speedups": time_trainable
    }
    
    for factor, value in trainable_factors.items():
        if round(value) == max_trainable:
            limiting_factor = factor
            break
    print(f"The thing stoping you from training more troops is {limiting_factor}.")



def main(): # Main function to run the program
    print("Welcome to the PaCMath program!")
    print("This program will help you calculate the power and capacity of your troops based on their tier and type.")
    while True:
        q1 = input("what would you like to do: 1 = Enter Info, 2 = Calculate, 3 = Calculate Trainable Troops, 4 = Quit: ").upper()
        if q1 == "1":
            tier, type, amount = get_info()
            print(f"You have entered: Tier {tier}, Type {type}, Amount {rounder(amount)}")
            continue
        elif q1 == "2":
            total_power, total_capacity = do_math(tier, type, int(amount))
            cost = get_tier_cost(tier, type, int(amount))
            print(f"Total Power: {total_power}, Total Capacity: {total_capacity}")
            if tier == "12":
                print("Tier 12 troop cost are not available yet.")
            else:
                print(f"Total Cost:\n{cost}")
            continue
        elif q1 == "3":
            get_max_troop_training()
            continue
        elif q1 == "4":
            print("Thank you for using the PaCMath program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            continue
        
main() # Run the main function to start the program


    