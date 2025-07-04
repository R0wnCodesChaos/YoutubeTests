tiers_power = {"1": 4, "2": 6, "3": 8, "4": 12, "5": 15, "6": 20, "7": 25, "8": 33, "9": 45, "10": 60, "11": 80, "12": 100}
tiers_capacity_A_I = {"1": 10, "2": 12, "3": 14, "4": 16, "5": 18, "6": 18, "7": 20, "8": 22, "9": 24, "10": 26, "11": 28, "12": 30}
tiers_capacity_C = {"1": 8, "2": 8, "3": 10, "4": 12, "5": 12, "6": 14, "7": 14, "8": 16, "9": 16, "10": 18, "11": 20, "12": 22}
tiers_capacity_V = {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
cost_V = {"food": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "wood": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "stone": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "iron": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}}

cost_C = {"food": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "wood": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "stone": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "iron": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}}

cost_A = {"food": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "wood": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "stone": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "iron": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}}

cost_I = {"food": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "wood": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "stone": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}
          , "iron": {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}}
# all tiers and corresponding capacities and power along with the type of troop for the ones with different capacities

def rounder(n):
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f}b"
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.2f}m"
    elif n >= 1_000:
        return f"{n / 1_000:.2f}k"
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
    troop_amount = rounder(int(troop_amount))  # Round the amount for better readability
    return troop_tier, troop_type, troop_amount

def do_math(tier, type, amount): # Function to calculate total power and capacity based on tier, type, and amount
    total_power = get_tier_power(tier) * (amount)
    total_capacity = get_tier_capacity(tier, type) * (amount)
    total_power = rounder(total_power)  # Round the total power for better readability
    total_capacity = rounder(total_capacity)  # Round the total capacity for better readability
    return total_power, total_capacity

def main(): # Main function to run the program
    print("Welcome to the PaCMath program!")
    print("This program will help you calculate the power and capacity of your troops based on their tier and type.")
    while True:
        q1 = input("what would you like to do: 1 = enter info, 2 = Calculate, 3 = Quit: ").upper()
        if q1 == "1":
            tier, type, amount = get_info()
            print(f"You have entered: Tier {tier}, Type {type}, Amount {amount}")
            continue
        elif q1 == "2":
            total_power, total_capacity = do_math(tier, type, int(amount))
            print(f"Total Power: {total_power}, Total Capacity: {total_capacity}")
            continue
        elif q1 == "3":
            print("Thank you for using the PaCMath program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            continue
        
main() # Run the main function to start the program


    