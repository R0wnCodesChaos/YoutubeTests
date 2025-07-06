import streamlit as st
import pandas as pd

# Data dictionaries
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

time_to_train = {"1": 6, "2": 7, "3": 10, "4": 13, "5": 17, "6": 22, "7": 29, "8": 38, "9": 50, "10": 100, "11": 0}

def rounder(n):
    """Function to round numbers for better readability"""
    if n >= 1000000000:
        return str(round(n / 1000000000, 2)) + "b"
    elif n >= 1000000:
        return str(round(n / 1000000, 2)) + "m"
    elif n >= 1000:
        return str(round(n / 1000, 2)) + "k"
    else:
        return str(n)

def get_tier_power(tier):
    """Function to get the power of a troop based on its tier"""
    return tiers_power[str(tier)]

def get_tier_capacity(tier, troop_type):
    """Function to get the capacity of a troop based on its tier and type"""
    if troop_type in ["A", "I"]:
        return tiers_capacity_A_I[str(tier)]
    elif troop_type == "C":
        return tiers_capacity_C[str(tier)]
    elif troop_type == "V":
        return tiers_capacity_V[str(tier)]

def get_tier_cost(tier, troop_type, amount):
    """Function to get the cost of a troop based on its tier and type"""
    if tier == 12:
        return "Tier 12 troop costs are not available yet."
    
    cost_dict = {
        "A": cost_A,
        "I": cost_I,
        "C": cost_C,
        "V": cost_V
    }
    
    costs = cost_dict[troop_type]
    tier_str = str(tier)
    
    cost_food = costs["food"][tier_str] * amount
    cost_wood = costs["wood"][tier_str] * amount
    cost_stone = costs["stone"][tier_str] * amount
    cost_iron = costs["iron"][tier_str] * amount
    
    return {
        "food": cost_food,
        "wood": cost_wood,
        "stone": cost_stone,
        "iron": cost_iron
    }

def calculate_max_trainable(tier, troop_type, resources, speedups):
    """Calculate maximum trainable troops based on resources and speedups"""
    if tier == 12 or (troop_type == "I" and tier > 10):
        return 0, "Invalid tier for this troop type"
    
    # Get costs for one troop
    cost_dict = {
        "A": cost_A,
        "I": cost_I,
        "C": cost_C,
        "V": cost_V
    }
    
    costs = cost_dict[troop_type]
    tier_str = str(tier)
    
    cost_food = costs["food"][tier_str]
    cost_wood = costs["wood"][tier_str]
    cost_stone = costs["stone"][tier_str]
    cost_iron = costs["iron"][tier_str]
    
    # Calculate trainable by each resource
    food_trainable = resources["food"] // cost_food if cost_food > 0 else float('inf')
    wood_trainable = resources["wood"] // cost_wood if cost_wood > 0 else float('inf')
    stone_trainable = resources["stone"] // cost_stone if cost_stone > 0 else float('inf')
    iron_trainable = resources["iron"] // cost_iron if cost_iron > 0 else float('inf')
    
    # Calculate trainable by time
    train_time = time_to_train[tier_str]
    time_trainable = speedups // train_time if train_time > 0 else float('inf')
    
    # Find limiting factor
    trainable_factors = {
        "food": food_trainable,
        "wood": wood_trainable,
        "stone": stone_trainable,
        "iron": iron_trainable,
        "speedups": time_trainable
    }
    
    max_trainable = min(trainable_factors.values())
    
    # Find what's limiting
    limiting_factor = [k for k, v in trainable_factors.items() if v == max_trainable][0]
    
    return int(max_trainable), limiting_factor

# Streamlit App
st.set_page_config(page_title="PaCMath - Troop Calculator", page_icon="⚔️", layout="wide")

st.title("⚔️ PaCMath - Troop Calculator")
st.markdown("Calculate power, capacity, and training costs for your troops!")

# Sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Choose a function:", ["Power & Capacity Calculator", "Training Cost Calculator", "Maximum Trainable Troops"])

if page == "Power & Capacity Calculator":
    st.header("📊 Power & Capacity Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tier = st.selectbox("Select Tier:", options=list(range(1, 13)), index=0)
        troop_type = st.selectbox("Select Troop Type:", options=["A", "I", "C", "V"], 
                                 format_func=lambda x: {"A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicle"}[x])
        amount = st.number_input("Enter Amount of Troops:", min_value=1, value=1, step=1)
    
    with col2:
        if st.button("Calculate Power & Capacity", type="primary"):
            power = get_tier_power(tier)
            capacity = get_tier_capacity(tier, troop_type)
            
            total_power = power * amount
            total_capacity = capacity * amount
            
            st.success("✅ Calculation Complete!")
            
            col3, col4 = st.columns(2)
            with col3:
                st.metric("Total Power", rounder(total_power))
            with col4:
                st.metric("Total Capacity", rounder(total_capacity))
            
            # Display per-unit stats
            st.subheader("Per-Unit Stats:")
            stats_df = pd.DataFrame({
                "Metric": ["Power per Unit", "Capacity per Unit"],
                "Value": [power, capacity]
            })
            st.dataframe(stats_df, use_container_width=True)

elif page == "Training Cost Calculator":
    st.header("💰 Training Cost Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tier = st.selectbox("Select Tier:", options=list(range(1, 13)), index=0)
        troop_type = st.selectbox("Select Troop Type:", options=["A", "I", "C", "V"], 
                                 format_func=lambda x: {"A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicle"}[x])
        amount = st.number_input("Enter Amount of Troops:", min_value=1, value=1, step=1)
    
    with col2:
        if st.button("Calculate Training Cost", type="primary"):
            if tier == 12:
                st.warning("⚠️ Tier 12 troop costs are not available yet.")
            else:
                costs = get_tier_cost(tier, troop_type, amount)
                
                st.success("✅ Cost Calculation Complete!")
                
                # Display costs in a nice format
                col3, col4, col5, col6 = st.columns(4)
                with col3:
                    st.metric("🥖 Food", rounder(costs["food"]))
                with col4:
                    st.metric("🌲 Wood", rounder(costs["wood"]))
                with col5:
                    st.metric("🗿 Stone", rounder(costs["stone"]))
                with col6:
                    st.metric("⚒️ Iron", rounder(costs["iron"]))
                
                # Display cost breakdown table
                st.subheader("Cost Breakdown:")
                cost_df = pd.DataFrame({
                    "Resource": ["Food", "Wood", "Stone", "Iron"],
                    "Cost per Unit": [costs["food"]//amount, costs["wood"]//amount, costs["stone"]//amount, costs["iron"]//amount],
                    "Total Cost": [costs["food"], costs["wood"], costs["stone"], costs["iron"]]
                })
                st.dataframe(cost_df, use_container_width=True)

elif page == "Maximum Trainable Troops":
    st.header("🎯 Maximum Trainable Troops Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Troop Selection")
        tier = st.selectbox("Select Tier:", options=list(range(1, 12)), index=0)
        troop_type = st.selectbox("Select Troop Type:", options=["A", "I", "C", "V"], 
                                 format_func=lambda x: {"A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicle"}[x])
        
        st.subheader("Current Resources")
        food = st.number_input("Food:", min_value=0, value=0, step=1000)
        wood = st.number_input("Wood:", min_value=0, value=0, step=1000)
        stone = st.number_input("Stone:", min_value=0, value=0, step=100)
        iron = st.number_input("Iron:", min_value=0, value=0, step=100)
    
    with col2:
        st.subheader("Speed-up Items")
        one_m = st.number_input("1 Minute Speed-ups:", min_value=0, value=0)
        five_m = st.number_input("5 Minute Speed-ups:", min_value=0, value=0)
        ten_m = st.number_input("10 Minute Speed-ups:", min_value=0, value=0)
        fifteen_m = st.number_input("15 Minute Speed-ups:", min_value=0, value=0)
        thirty_m = st.number_input("30 Minute Speed-ups:", min_value=0, value=0)
        sixty_m = st.number_input("1 Hour Speed-ups:", min_value=0, value=0)
        three_h = st.number_input("3 Hour Speed-ups:", min_value=0, value=0)
        eight_h = st.number_input("8 Hour Speed-ups:", min_value=0, value=0)
        fifteen_h = st.number_input("15 Hour Speed-ups:", min_value=0, value=0)
        twenty_four_h = st.number_input("24 Hour Speed-ups:", min_value=0, value=0)
        three_d = st.number_input("3 Day Speed-ups:", min_value=0, value=0)
        seven_d = st.number_input("7 Day Speed-ups:", min_value=0, value=0)
    
    if st.button("Calculate Maximum Trainable Troops", type="primary"):
        # Calculate total speedup time in seconds
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
        
        resources = {
            "food": food,
            "wood": wood,
            "stone": stone,
            "iron": iron
        }
        
        max_trainable, limiting_factor = calculate_max_trainable(tier, troop_type, resources, total_speedup_time)
        
        st.success("✅ Maximum Trainable Calculation Complete!")
        
        col3, col4 = st.columns(2)
        with col3:
            st.metric("Maximum Trainable Troops", f"{max_trainable:,}")
        with col4:
            st.metric("Limiting Factor", limiting_factor.title())
        
        # Display speedup summary
        st.subheader("Speed-up Summary:")
        speedup_df = pd.DataFrame({
            "Time Unit": ["Minutes", "Hours", "Days"],
            "Total Available": [
                rounder(round(total_speedup_time / 60)),
                rounder(round(total_speedup_time / 3600)),
                rounder(round(total_speedup_time / 86400))
            ]
        })
        st.dataframe(speedup_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**PaCMath Troop Calculator** - Plan your army efficiently! 🎮")