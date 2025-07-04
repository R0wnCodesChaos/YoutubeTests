import streamlit as st

tiers_power = {"1": 4, "2": 6, "3": 8, "4": 12, "5": 15, "6": 20, "7": 25, "8": 33, "9": 45, "10": 60, "11": 80, "12": 100}
tiers_capacity_A_I = {"1": 10, "2": 12, "3": 14, "4": 16, "5": 18, "6": 18, "7": 20, "8": 22, "9": 24, "10": 26, "11": 28, "12": 30}
tiers_capacity_C = {"1": 8, "2": 8, "3": 10, "4": 12, "5": 12, "6": 14, "7": 14, "8": 16, "9": 16, "10": 18, "11": 20, "12": 22}
tiers_capacity_V = {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}

cost_V = {"food": {"1": 27, "2": 50, "3": 154, "4": 98, "5": 100, "6": 179, "7": 230, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0},
          "wood": {"1": 0, "2": 30, "3": 43, "4": 63, "5": 91, "6": 125, "7": 174, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0},
          "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 2, "6": 4, "7": 8, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0},
          "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0}}

cost_C = {"food": {"1": 48, "2": 68, "3": 94, "4": 128, "5": 182, "6": 235, "7": 316, "8": 392, "9": 566, "10": 0, "11": 0, "12": 0},
          "wood": {"1": 0, "2": 15, "3": 21, "4": 31, "5": 45, "6": 62, "7": 87, "8": 120, "9": 165, "10": 0, "11": 0, "12": 0},
          "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 3, "6": 6, "7": 10, "8": 17, "9": 30, "10": 0, "11": 0, "12": 0},
          "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 1, "9": 4, "10": 0, "11": 0, "12": 0}}

cost_A = {"food": {"1": 45, "2": 61, "3": 90, "4": 121, "5": 165, "6": 223, "7": 287, "8": 373, "9": 472, "10": 0, "11": 0, "12": 0},
          "wood": {"1": 0, "2": 19, "3": 26, "4": 41, "5": 54, "6": 75, "7": 113, "8": 156, "9": 199, "10": 0, "11": 0, "12": 0},
          "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 3, "6": 6, "7": 10, "8": 16, "9": 25, "10": 0, "11": 0, "12": 0},
          "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 1, "9": 3, "10": 0, "11": 0, "12": 0}}

cost_I = {"food": {"1": 54, "2": 61, "3": 108, "4": 121, "5": 199, "6": 223, "7": 345, "8": 373, "9": 566, "10": 0, "11": 0, "12": 0},
          "wood": {"1": 0, "2": 19, "3": 21, "4": 38, "5": 45, "6": 75, "7": 87, "8": 144, "9": 165, "10": 0, "11": 0, "12": 0},
          "stone": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 4, "6": 6, "7": 11, "8": 16, "9": 30, "10": 0, "11": 0, "12": 0},
          "iron": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 1, "9": 4, "10": 0, "11": 0, "12": 0}}

def rounder(n):
    if n >= 1_000_000_000:
        return f"{round(n / 1_000_000_000, 2)}b"
    elif n >= 1_000_000:
        return f"{round(n / 1_000_000, 2)}m"
    elif n >= 1_000:
        return f"{round(n / 1_000, 2)}k"
    else:
        return str(n)

def get_tier_power(tier):
    return tiers_power[tier]

def get_tier_capacity(tier, troop_type):
    if troop_type in ("A", "I"):
        return tiers_capacity_A_I[tier]
    elif troop_type == "C":
        return tiers_capacity_C[tier]
    elif troop_type == "V":
        return tiers_capacity_V[tier]

def get_tier_cost(tier, troop_type, amount):
    if tier == "12":
        return None  # No costs available for tier 12
    if troop_type == "A":
        cost_data = cost_A
    elif troop_type == "I":
        cost_data = cost_I
    elif troop_type == "C":
        cost_data = cost_C
    elif troop_type == "V":
        cost_data = cost_V

    cost_food = cost_data["food"][tier] * amount
    cost_wood = cost_data["wood"][tier] * amount
    cost_stone = cost_data["stone"][tier] * amount
    cost_iron = cost_data["iron"][tier] * amount

    return {
        "Food": rounder(cost_food),
        "Wood": rounder(cost_wood),
        "Stone": rounder(cost_stone),
        "Iron": rounder(cost_iron)
    }

st.title("PaCMath Troop Calculator")

tier = st.selectbox("Select troop tier", options=[str(i) for i in range(1, 13)])
troop_type = st.selectbox("Select troop type", options=["A (Archers)", "I (Infantry)", "C (Calvary)", "V (Vehicle)"])
amount = st.number_input("Enter the amount of troops", min_value=1, step=1)

troop_type_code = troop_type[0]

if st.button("Calculate"):
    total_power = get_tier_power(tier) * amount
    total_capacity = get_tier_capacity(tier, troop_type_code) * amount
    cost = get_tier_cost(tier, troop_type_code, amount)

    st.write(f"**Total Troops:** {amount}")
    st.write(f"**Total Power:** {rounder(total_power)}")
    st.write(f"**Total Capacity:** {rounder(total_capacity)}")

    if tier == "12":
        st.warning("Tier 12 troop cost are not available yet.")
    else:
        st.write("**Total Cost:**")
        for resource, value in cost.items():
            st.write(f"- {resource}: {value}")
