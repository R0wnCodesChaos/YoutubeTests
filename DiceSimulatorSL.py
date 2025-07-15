import streamlit as st
import random

# Initialize session state
if 'doin' not in st.session_state:
    st.session_state.doin = 100
if 'dice_rollable' not in st.session_state:
    st.session_state.dice_rollable = 1
if 'dice_multiplier' not in st.session_state:
    st.session_state.dice_multiplier = 1
if 'dice_crit_chance' not in st.session_state:
    st.session_state.dice_crit_chance = 5
if 'dice_crit_multiplier' not in st.session_state:
    st.session_state.dice_crit_multiplier = 100
if 'dice_type' not in st.session_state:
    st.session_state.dice_type = "d6"
if 'dice_s' not in st.session_state:
    st.session_state.dice_s = 6
if 'last_roll_result' not in st.session_state:
    st.session_state.last_roll_result = []

# Constants
upgrade_cost = {
    "d6": 3000,
    "d8": 3000, 
    "d10": 8500, 
    "d12": 12000, 
    "d20": 30000, 
    "d25": 85000,
    "d50": 120000,
    "d80": 300000,
    "d100": 850000,
}

dice_sides = {
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100
}

def rounder(n):
    """Function to round numbers for better readability"""
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
        return str(int(n))

def dice_amount_upgrade_cost():
    """Calculate the cost to upgrade dice amount"""
    if st.session_state.dice_s == 6:
        return 1000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 8:
        return 1500 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 10:
        return 2000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 12:
        return 2500 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 20:
        return 4500 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 100:
        return 7500 * st.session_state.dice_rollable

def roll_dice():
    """Roll the dice and update doins"""
    roll_results = []
    total_roll = 0
    
    for i in range(st.session_state.dice_rollable):
        r = random.randint(1, st.session_state.dice_s)
        roll_results.append(r)
        total_roll += r
    
    # Apply multiplier
    multiplied_roll = total_roll * st.session_state.dice_multiplier
    
    # Check for critical hit
    is_crit = False
    final_roll = multiplied_roll
    if st.session_state.dice_crit_chance > 0:
        if random.random() < st.session_state.dice_crit_chance / 100:
            is_crit = True
            final_roll = multiplied_roll * st.session_state.dice_crit_multiplier
    
    # Update doins
    st.session_state.doin += final_roll
    
    # Store results for display
    st.session_state.last_roll_result = {
        'individual_rolls': roll_results,
        'total_roll': total_roll,
        'multiplied_roll': multiplied_roll,
        'is_crit': is_crit,
        'final_roll': final_roll
    }

def upgrade_dice():
    """Upgrade dice type"""
    current_type = st.session_state.dice_type
    cost = upgrade_cost.get(current_type, 0)
    
    if st.session_state.doin >= cost:
        st.session_state.doin -= cost
        if current_type == "d6":
            st.session_state.dice_type = "d8"
            st.session_state.dice_s = 8
        elif current_type == "d8":
            st.session_state.dice_type = "d10"
            st.session_state.dice_s = 10
        elif current_type == "d10":
            st.session_state.dice_type = "d12"
            st.session_state.dice_s = 12
        elif current_type == "d12":
            st.session_state.dice_type = "d20"
            st.session_state.dice_s = 20
        elif current_type == "d20":
            st.session_state.dice_type = "d100"
            st.session_state.dice_s = 100
        return True
    return False

def upgrade_dice_amount():
    """Upgrade number of rollable dice"""
    cost = dice_amount_upgrade_cost()
    if st.session_state.doin >= cost:
        st.session_state.doin -= cost
        st.session_state.dice_rollable += 1
        return True
    return False

def upgrade_multiplier():
    """Upgrade dice multiplier"""
    cost = 1000 * st.session_state.dice_multiplier
    if st.session_state.doin >= cost:
        st.session_state.doin -= cost
        st.session_state.dice_multiplier += 1
        return True
    return False

def upgrade_crit_chance():
    """Upgrade critical hit chance"""
    cost = 1000 * st.session_state.dice_crit_chance
    if st.session_state.doin >= cost and st.session_state.dice_crit_chance < 100:
        st.session_state.doin -= cost
        st.session_state.dice_crit_chance += 2
        return True
    return False

def upgrade_crit_multiplier():
    """Upgrade critical hit multiplier"""
    cost = 250 * st.session_state.dice_crit_multiplier
    if st.session_state.doin >= cost:
        st.session_state.doin -= cost
        st.session_state.dice_crit_multiplier += 50
        return True
    return False

# Streamlit UI
st.title("🎲 Dice Simulator")
st.markdown("---")

# Display current stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Doins", rounder(st.session_state.doin))
with col2:
    st.metric("🎲 Dice Type", st.session_state.dice_type)
with col3:
    st.metric("🔢 Rollable Dice", st.session_state.dice_rollable)

col4, col5, col6 = st.columns(3)
with col4:
    st.metric("✨ Multiplier", f"{st.session_state.dice_multiplier}x")
with col5:
    st.metric("💥 Crit Chance", f"{st.session_state.dice_crit_chance}%")
with col6:
    st.metric("🔥 Crit Multiplier", f"{st.session_state.dice_crit_multiplier}x")

st.markdown("---")

# Roll dice section
st.subheader("🎲 Roll Your Dice")
if st.button("🎲 ROLL DICE", type="primary", use_container_width=True):
    roll_dice()

# Display last roll result
if st.session_state.last_roll_result:
    result = st.session_state.last_roll_result
    
    st.success("🎉 Roll Results:")
    
    # Show individual rolls
    if len(result['individual_rolls']) > 1:
        rolls_text = " + ".join([str(r) for r in result['individual_rolls']])
        st.write(f"**Individual Rolls:** {rolls_text} = {result['total_roll']}")
    else:
        st.write(f"**Roll:** {result['total_roll']}")
    
    # Show multiplied result
    if st.session_state.dice_multiplier > 1:
        st.write(f"**With {st.session_state.dice_multiplier}x Multiplier:** {rounder(result['multiplied_roll'])}")
    
    # Show critical hit
    if result['is_crit']:
        st.write(f"**💥 CRITICAL HIT! ({st.session_state.dice_crit_multiplier}x):** {rounder(result['final_roll'])}")
    
    st.write(f"**💰 Doins Earned:** {rounder(result['final_roll'])}")

st.markdown("---")

# Upgrades section
st.subheader("⬆️ Upgrades")

# Dice type upgrade
if st.session_state.dice_type != "d100":
    next_dice = {"d6": "d8", "d8": "d10", "d10": "d12", "d12": "d20", "d20": "d100"}
    upgrade_dice_cost = upgrade_cost.get(st.session_state.dice_type, 0)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(f"**Upgrade to {next_dice[st.session_state.dice_type]}** - Cost: {rounder(upgrade_dice_cost)} Doins")
    with col2:
        if st.button("Upgrade Dice", disabled=st.session_state.doin < upgrade_dice_cost):
            if upgrade_dice():
                st.success(f"Upgraded to {st.session_state.dice_type}!")
            else:
                st.error("Not enough Doins!")

# Dice amount upgrade
dice_amount_cost = dice_amount_upgrade_cost()
col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"**Add +1 Rollable Dice** - Cost: {rounder(dice_amount_cost)} Doins")
with col2:
    if st.button("Add Dice", disabled=st.session_state.doin < dice_amount_cost):
        if upgrade_dice_amount():
            st.success(f"Now have {st.session_state.dice_rollable} rollable dice!")
        else:
            st.error("Not enough Doins!")

# Multiplier upgrade
multiplier_cost = 1000 * st.session_state.dice_multiplier
col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"**Upgrade Multiplier** - Cost: {rounder(multiplier_cost)} Doins")
with col2:
    if st.button("Upgrade Multiplier", disabled=st.session_state.doin < multiplier_cost):
        if upgrade_multiplier():
            st.success(f"Multiplier upgraded to {st.session_state.dice_multiplier}x!")
        else:
            st.error("Not enough Doins!")

# Crit chance upgrade
crit_chance_cost = 1000 * st.session_state.dice_crit_chance
col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"**Upgrade Crit Chance** - Cost: {rounder(crit_chance_cost)} Doins")
with col2:
    if st.button("Upgrade Crit Chance", disabled=(st.session_state.doin < crit_chance_cost or st.session_state.dice_crit_chance >= 100)):
        if upgrade_crit_chance():
            st.success(f"Crit chance upgraded to {st.session_state.dice_crit_chance}%!")
        else:
            st.error("Not enough Doins or max crit chance reached!")

# Crit multiplier upgrade
crit_mult_cost = 250 * st.session_state.dice_crit_multiplier
col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"**Upgrade Crit Multiplier** - Cost: {rounder(crit_mult_cost)} Doins")
with col2:
    if st.button("Upgrade Crit Multiplier", disabled=st.session_state.doin < crit_mult_cost):
        if upgrade_crit_multiplier():
            st.success(f"Crit multiplier upgraded to {st.session_state.dice_crit_multiplier}x!")
        else:
            st.error("Not enough Doins!")

st.markdown("---")
st.markdown("*Keep rolling to earn more Doins and upgrade your dice!*")