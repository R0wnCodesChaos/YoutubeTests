import streamlit as st

# Troop data dictionaries
tiers_power = {"1": 4, "2": 6, "3": 8, "4": 12, "5": 15, "6": 20, "7": 25, "8": 33, "9": 45, "10": 60, "11": 80, "12": 100}
tiers_capacity_A_I = {"1": 10, "2": 12, "3": 14, "4": 16, "5": 18, "6": 18, "7": 20, "8": 22, "9": 24, "10": 26, "11": 28, "12": 30}
tiers_capacity_C = {"1": 8, "2": 8, "3": 10, "4": 12, "5": 12, "6": 14, "7": 14, "8": 16, "9": 16, "10": 18, "11": 20, "12": 22}
tiers_capacity_V = {"1": 15, "2": 17, "3": 19, "4": 21, "5": 23, "6": 25, "7": 27, "8": 29, "9": 31, "10": 33, "11": 35, "12": 40}

# Functions
def get_tier_power(tier):
    return tiers_power[tier]

def get_tier_capacity(tier, troop_type):
    if troop_type in ["A", "I"]:
        return tiers_capacity_A_I[tier]
    elif troop_type == "C":
        return tiers_capacity_C[tier]
    elif troop_type == "V":
        return tiers_capacity_V[tier]

def do_math(tier, type, amount):
    power = get_tier_power(tier)
    capacity = get_tier_capacity(tier, type)
    return power * amount, capacity * amount

# Streamlit Interface
st.title("⚔️ PaCMath Troop Calculator")
st.markdown("Use this tool to calculate the **power** and **capacity** of your troops.")

# User inputs
tier = st.selectbox("Select Troop Tier", options=list(tiers_power.keys()), index=0)
type = st.radio("Select Troop Type", options=["A", "I", "C", "V"], format_func=lambda x: {
    "A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicle"
}[x])
amount = st.number_input("Enter Number of Troops", min_value=1, step=1)

# Calculate button
if st.button("Calculate"):
    total_power, total_capacity = do_math(tier, type, amount)
    st.success(f"💥 Total Power: **{total_power}**")
    st.info(f"🎒 Total Capacity: **{total_capacity}**")
