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
    return tiers_power[tier]

def get_tier_capacity(tier, troop_type):
    """Function to get the capacity of a troop based on its tier and type"""
    if troop_type in ["A", "I"]:
        return tiers_capacity_A_I[tier]
    elif troop_type == "C":
        return tiers_capacity_C[tier]
    elif troop_type == "V":
        return tiers_capacity_V[tier]

def get_tier_cost(tier, troop_type, amount):
    """Function to get the cost of a troop based on its tier and type"""
    if tier == "12":
        return "Tier 12 troop costs are not available yet."
    
    cost_dict = {"A": cost_A, "I": cost_I, "C": cost_C, "V": cost_V}
    
    if troop_type in cost_dict:
        costs = cost_dict[troop_type]
        cost_food = costs["food"][tier] * amount
        cost_wood = costs["wood"][tier] * amount
        cost_stone = costs["stone"][tier] * amount
        cost_iron = costs["iron"][tier] * amount
        
        return {
            "food": cost_food,
            "wood": cost_wood,
            "stone": cost_stone,
            "iron": cost_iron
        }

def calculate_max_trainable(tier, troop_type, resources, speedups):
    """Calculate maximum trainable troops based on resources and speedups"""
    if tier == "12" or tier == "11":
        return "Training calculations not available for tier 11 and 12."
    
    cost_dict = {"A": cost_A, "I": cost_I, "C": cost_C, "V": cost_V}
    costs = cost_dict[troop_type]
    
    # Calculate trainable based on each resource
    food_trainable = resources["food"] // costs["food"][tier] if costs["food"][tier] > 0 else float('inf')
    wood_trainable = resources["wood"] // costs["wood"][tier] if costs["wood"][tier] > 0 else float('inf')
    stone_trainable = resources["stone"] // costs["stone"][tier] if costs["stone"][tier] > 0 else float('inf')
    iron_trainable = resources["iron"] // costs["iron"][tier] if costs["iron"][tier] > 0 else float('inf')
    
    # Calculate speedup trainable
    train_time = time_to_train[tier]
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
    limiting_factor = min(trainable_factors, key=trainable_factors.get)
    
    return int(max_trainable), limiting_factor, trainable_factors

# Streamlit App
st.set_page_config(page_title="PaCMath - Troop Calculator", page_icon="⚔️", layout="wide")

st.title("⚔️ PaCMath - Troop Power & Capacity Calculator")
st.markdown("Calculate troop power, capacity, costs, and maximum trainable troops for your army!")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Function:", ["Troop Calculator", "Max Trainable Troops", "Troop Comparison"])

if page == "Troop Calculator":
    st.header("🏹 Troop Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Troop Information")
        tier = st.selectbox("Select Tier:", options=list(range(1, 13)), format_func=lambda x: f"Tier {x}")
        troop_type = st.selectbox("Select Troop Type:", 
                                  options=["A", "I", "C", "V"], 
                                  format_func=lambda x: {"A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicles"}[x])
        amount = st.number_input("Number of Troops:", min_value=1, value=1, step=1)
    
    with col2:
        st.subheader("Results")
        if st.button("Calculate", type="primary"):
            tier_str = str(tier)
            
            # Calculate power and capacity
            power = get_tier_power(tier_str)
            capacity = get_tier_capacity(tier_str, troop_type)
            total_power = power * amount
            total_capacity = capacity * amount
            
            # Display results
            st.metric("Total Power", rounder(total_power))
            st.metric("Total Capacity", rounder(total_capacity))
            
            # Calculate and display costs
            if tier != 12:
                costs = get_tier_cost(tier_str, troop_type, amount)
                st.subheader("Resource Costs")
                cost_cols = st.columns(4)
                with cost_cols[0]:
                    st.metric("Food", rounder(costs["food"]))
                with cost_cols[1]:
                    st.metric("Wood", rounder(costs["wood"]))
                with cost_cols[2]:
                    st.metric("Stone", rounder(costs["stone"]))
                with cost_cols[3]:
                    st.metric("Iron", rounder(costs["iron"]))
            else:
                st.warning("Tier 12 troop costs are not available yet.")

elif page == "Max Trainable Troops":
    st.header("🎯 Maximum Trainable Troops Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Troop Information")
        tier = st.selectbox("Select Tier:", options=list(range(1, 12)), format_func=lambda x: f"Tier {x}")
        troop_type = st.selectbox("Select Troop Type:", 
                                  options=["A", "I", "C", "V"], 
                                  format_func=lambda x: {"A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicles"}[x])
        
        st.subheader("Your Resources")
        food = st.number_input("Food:", min_value=0, value=0, step=1000)
        wood = st.number_input("Wood:", min_value=0, value=0, step=1000)
        stone = st.number_input("Stone:", min_value=0, value=0, step=100)
        iron = st.number_input("Iron:", min_value=0, value=0, step=100)
    
    with col2:
        st.subheader("Speed-ups (in seconds)")
        speedups = 0
        speedups += st.number_input("1 Minute (60s):", min_value=0, value=0) * 60
        speedups += st.number_input("5 Minutes (300s):", min_value=0, value=0) * 300
        speedups += st.number_input("10 Minutes (600s):", min_value=0, value=0) * 600
        speedups += st.number_input("15 Minutes (900s):", min_value=0, value=0) * 900
        speedups += st.number_input("30 Minutes (1800s):", min_value=0, value=0) * 1800
        speedups += st.number_input("1 Hour (3600s):", min_value=0, value=0) * 3600
        speedups += st.number_input("3 Hours (10800s):", min_value=0, value=0) * 10800
        speedups += st.number_input("8 Hours (28800s):", min_value=0, value=0) * 28800
        speedups += st.number_input("15 Hours (54000s):", min_value=0, value=0) * 54000
        speedups += st.number_input("24 Hours (86400s):", min_value=0, value=0) * 86400
        speedups += st.number_input("3 Days (259200s):", min_value=0, value=0) * 259200
        speedups += st.number_input("7 Days (604800s):", min_value=0, value=0) * 604800
        
        st.metric("Total Speedup Time", f"{speedups:,} seconds")
        st.caption(f"≈ {speedups/3600:.1f} hours ≈ {speedups/86400:.1f} days")
    
    if st.button("Calculate Maximum Trainable", type="primary"):
        resources = {"food": food, "wood": wood, "stone": stone, "iron": iron}
        result = calculate_max_trainable(str(tier), troop_type, resources, speedups)
        
        if isinstance(result, str):
            st.warning(result)
        else:
            max_trainable, limiting_factor, factors = result
            
            st.success(f"**Maximum Trainable Troops: {max_trainable:,}**")
            st.info(f"**Limiting Factor: {limiting_factor.title()}**")
            
            # Show breakdown
            st.subheader("Resource Breakdown")
            breakdown_cols = st.columns(5)
            factor_names = ["Food", "Wood", "Stone", "Iron", "Speedups"]
            for i, (factor, name) in enumerate(zip(factors.keys(), factor_names)):
                with breakdown_cols[i]:
                    value = factors[factor]
                    if value == float('inf'):
                        st.metric(name, "∞")
                    else:
                        st.metric(name, f"{int(value):,}")

elif page == "Troop Comparison":
    st.header("⚖️ Troop Comparison")
    
    st.subheader("Compare Different Troop Types")
    
    # Create comparison table
    comparison_data = []
    for tier in range(1, 13):
        tier_str = str(tier)
        for troop_type in ["A", "I", "C", "V"]:
            power = get_tier_power(tier_str)
            capacity = get_tier_capacity(tier_str, troop_type)
            
            if tier != 12:
                costs = get_tier_cost(tier_str, troop_type, 1)
                comparison_data.append({
                    "Tier": tier,
                    "Type": {"A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicles"}[troop_type],
                    "Power": power,
                    "Capacity": capacity,
                    "Food Cost": costs["food"],
                    "Wood Cost": costs["wood"],
                    "Stone Cost": costs["stone"],
                    "Iron Cost": costs["iron"],
                    "Power/Food": round(power/costs["food"], 3) if costs["food"] > 0 else "∞"
                })
            else:
                comparison_data.append({
                    "Tier": tier,
                    "Type": {"A": "Archers", "I": "Infantry", "C": "Cavalry", "V": "Vehicles"}[troop_type],
                    "Power": power,
                    "Capacity": capacity,
                    "Food Cost": "N/A",
                    "Wood Cost": "N/A",
                    "Stone Cost": "N/A",
                    "Iron Cost": "N/A",
                    "Power/Food": "N/A"
                })
    
    df = pd.DataFrame(comparison_data)
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        selected_tiers = st.multiselect("Select Tiers:", options=list(range(1, 13)), default=list(range(1, 6)))
    with col2:
        selected_types = st.multiselect("Select Types:", 
                                       options=["Archers", "Infantry", "Cavalry", "Vehicles"], 
                                       default=["Archers", "Infantry", "Cavalry", "Vehicles"])
    
    # Filter dataframe
    filtered_df = df[
        (df["Tier"].isin(selected_tiers)) & 
        (df["Type"].isin(selected_types))
    ]
    
    st.dataframe(filtered_df, use_container_width=True)
    
    # Charts
    if not filtered_df.empty:
        st.subheader("Power by Tier and Type")
        chart_data = filtered_df.pivot(index="Tier", columns="Type", values="Power")
        st.line_chart(chart_data)

# Footer
st.markdown("---")
st.markdown("**PaCMath Calculator** - Calculate your troop power and optimize your army! 🗡️")