import streamlit as st
import random

# Initialize session state
if 'dice_rollable' not in st.session_state:
    st.session_state.dice_rollable = 1
if 'dice_rolled' not in st.session_state:
    st.session_state.dice_rolled = 0
if 'dice_multiplier' not in st.session_state:
    st.session_state.dice_multiplier = 1
if 'dice_crit_chance' not in st.session_state:
    st.session_state.dice_crit_chance = 5
if 'dice_crit_multiplier' not in st.session_state:
    st.session_state.dice_crit_multiplier = 100
if 'roll_history' not in st.session_state:
    st.session_state.roll_history = []
if 'dice_type' not in st.session_state:
    st.session_state.dice_type = "d6"
if 'dice_s' not in st.session_state:
    st.session_state.dice_s = 6
if 'doin' not in st.session_state:
    st.session_state.doin = 100

# Game data
upgrade_cost = {
    "d6": 1200,
    "d8": 3000, 
    "d10": 8000, 
    "d12": 12000, 
    "d20": 30000, 
    "d25": 85000,
    "d50": 1200000,
    "d80": 30000000,
    "d100": 850000000,
    "d120": 12000000000,
    "d200": 300000000000,
    "d500": 850000000000,
    "d1000": 1200000000000,
    "dinfinity": 1000000000000000000000
}

dice_sides = {
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100,
    "d120": 120,
    "d200": 200,
    "d500": 500,
    "d1000": 1000,
    "dinfinity": int(1e18)
}

dice_progression = {
    "d6": "d8",
    "d8": "d10",
    "d10": "d12",
    "d12": "d20",
    "d20": "d100",
    "d100": "d120",
    "d120": "d200",
    "d200": "d500",
    "d500": "d1000",
    "d1000": "dinfinity"
}

def rounder(n):
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
    if st.session_state.dice_s == 6:
        return 1000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 8:
        return 5000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 10:
        return 10000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 12:
        return 12000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 20:
        return 20000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 100:
        return 100000000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 120:
        return 120000000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 200:
        return 200000000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 500:
        return 500000000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 1000:
        return 1000000000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == int(1e18):
        return 1000000000000000000000 * st.session_state.dice_rollable

def roll_dice():
    d_sides = dice_sides[st.session_state.dice_type]
    roll = 0
    roll_details = []

    for i in range(st.session_state.dice_rollable):
        r = random.randint(1, d_sides)
        roll_details.append(f"Die {i + 1}: {rounder(r)}")
        roll += r
    
    base_roll = roll
    roll *= st.session_state.dice_multiplier
    
    crit_hit = False
    if st.session_state.dice_crit_chance > 0:
        if random.random() < st.session_state.dice_crit_chance / 100:
            crit_hit = True
            roll *= st.session_state.dice_crit_multiplier
    
    st.session_state.doin += roll
    
    # Store roll result
    result = {
        'details': roll_details,
        'base_total': base_roll,
        'multiplied_total': base_roll * st.session_state.dice_multiplier,
        'final_total': roll,
        'crit_hit': crit_hit,
        'doins_gained': roll
    }
    
    return result

def upgrade_dice_type(quantity=1):
    total_cost = 0
    current_type = st.session_state.dice_type
    
    for _ in range(quantity):
        if current_type in dice_progression:
            total_cost += upgrade_cost[current_type]
            current_type = dice_progression[current_type]
        else:
            break
    
    if st.session_state.doin >= total_cost and current_type != st.session_state.dice_type:
        st.session_state.doin -= total_cost
        st.session_state.dice_type = current_type
        st.session_state.dice_s = dice_sides[current_type]
        return True, quantity
    return False, 0

def upgrade_dice_amount(quantity=1):
    total_cost = 0
    for i in range(quantity):
        total_cost += dice_amount_upgrade_cost()
        if st.session_state.doin >= total_cost:
            continue
        else:
            quantity = i
            break
    
    if quantity > 0 and st.session_state.doin >= total_cost:
        st.session_state.doin -= total_cost
        st.session_state.dice_rollable += quantity
        return True, quantity
    return False, 0

def upgrade_multiplier(quantity=1):
    total_cost = 0
    current_mult = st.session_state.dice_multiplier
    
    for _ in range(quantity):
        total_cost += 7500 * current_mult
        current_mult += 1
    
    if st.session_state.doin >= total_cost:
        st.session_state.doin -= total_cost
        st.session_state.dice_multiplier += quantity
        return True, quantity
    return False, 0

def upgrade_crit_chance(quantity=1):
    if st.session_state.dice_crit_chance >= 100:
        return False, 0
    
    max_upgrades = min(quantity, 100 - st.session_state.dice_crit_chance)
    total_cost = 0
    current_chance = st.session_state.dice_crit_chance
    
    for _ in range(max_upgrades):
        total_cost += 100000 * current_chance
        current_chance += 1
    
    if st.session_state.doin >= total_cost:
        st.session_state.doin -= total_cost
        st.session_state.dice_crit_chance += max_upgrades
        return True, max_upgrades
    return False, 0

def upgrade_crit_multiplier(quantity=1):
    total_cost = 0
    current_mult = st.session_state.dice_crit_multiplier
    
    for _ in range(quantity):
        total_cost += 25000 * current_mult
        current_mult += 50
    
    if st.session_state.doin >= total_cost:
        st.session_state.doin -= total_cost
        st.session_state.dice_crit_multiplier += (quantity * 50)
        return True, quantity
    return False, 0

# Streamlit UI
st.set_page_config(page_title="🎲 Dice Simulator", page_icon="🎲", layout="wide")

st.title("🎲 Dice Simulator")
st.markdown("---")

# Display current stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Doins", rounder(st.session_state.doin))
    st.metric("🎲 Dice Type", st.session_state.dice_type)

with col2:
    st.metric("🔢 Rollable Dice", st.session_state.dice_rollable)
    st.metric("✖️ Multiplier", st.session_state.dice_multiplier)

with col3:
    st.metric("💥 Crit Chance", f"{st.session_state.dice_crit_chance}%")
    st.metric("🚀 Crit Multiplier", st.session_state.dice_crit_multiplier)

with col4:
    st.metric("🎯 Total Dice Rolled", st.session_state.dice_rolled)

st.markdown("---")

# Roll dice section
st.subheader("🎲 Roll Dice")
if st.button("🎲 Roll Dice!", type="primary", use_container_width=True):
    result = roll_dice()
    st.session_state.dice_rolled += st.session_state.dice_rollable
    
    st.success(f"🎉 You gained {rounder(result['doins_gained'])} Doins!")
    
    with st.expander("Roll Details", expanded=True):
        for detail in result['details']:
            st.write(f"• {detail}")
        
        st.write(f"**Base Total:** {rounder(result['base_total'])}")
        st.write(f"**After Multiplier ({st.session_state.dice_multiplier}x):** {rounder(result['multiplied_total'])}")
        
        if result['crit_hit']:
            st.write(f"**💥 CRITICAL HIT! ({st.session_state.dice_crit_multiplier}x):** {rounder(result['final_total'])}")
        
        st.write(f"**Final Total:** {rounder(result['final_total'])}")

st.markdown("---")

# Upgrades section
st.subheader("⬆️ Upgrades")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🎲 Dice Type Upgrade")
    if st.session_state.dice_type in dice_progression:
        next_dice = dice_progression[st.session_state.dice_type]
        cost = upgrade_cost[st.session_state.dice_type]
        st.write(f"Upgrade to {next_dice} for {rounder(cost)} Doins")
        
        dice_upgrade_qty = st.number_input("Quantity", min_value=1, max_value=10, value=1, key="dice_upgrade_qty")
        
        if st.button("Upgrade Dice Type", use_container_width=True):
            success, upgraded = upgrade_dice_type(dice_upgrade_qty)
            if success:
                st.success(f"✅ Upgraded dice type {upgraded} time(s)!")
                st.rerun()
            else:
                st.error("❌ Not enough Doins!")
    else:
        st.write("🏆 Maximum dice type reached!")

    st.markdown("#### 🔢 Rollable Dice")
    cost = dice_amount_upgrade_cost()
    st.write(f"Add 1 die for {rounder(cost)} Doins")
    
    dice_amount_qty = st.number_input("Quantity", min_value=1, max_value=100, value=1, key="dice_amount_qty")
    
    if st.button("Upgrade Dice Amount", use_container_width=True):
        success, upgraded = upgrade_dice_amount(dice_amount_qty)
        if success:
            st.success(f"✅ Added {upgraded} dice!")
            st.rerun()
        else:
            st.error("❌ Not enough Doins!")

    st.markdown("#### ✖️ Multiplier")
    cost = 7500 * st.session_state.dice_multiplier
    st.write(f"Increase multiplier by 1 for {rounder(cost)} Doins")
    
    multiplier_qty = st.number_input("Quantity", min_value=1, max_value=50, value=1, key="multiplier_qty")
    
    if st.button("Upgrade Multiplier", use_container_width=True):
        success, upgraded = upgrade_multiplier(multiplier_qty)
        if success:
            st.success(f"✅ Increased multiplier by {upgraded}!")
            st.rerun()
        else:
            st.error("❌ Not enough Doins!")

with col2:
    st.markdown("#### 💥 Critical Hit Chance")
    if st.session_state.dice_crit_chance < 100:
        cost = 100000 * st.session_state.dice_crit_chance
        st.write(f"Increase crit chance by 1% for {rounder(cost)} Doins")
        
        crit_chance_qty = st.number_input("Quantity", min_value=1, max_value=100-st.session_state.dice_crit_chance, value=1, key="crit_chance_qty")
        
        if st.button("Upgrade Crit Chance", use_container_width=True):
            success, upgraded = upgrade_crit_chance(crit_chance_qty)
            if success:
                st.success(f"✅ Increased crit chance by {upgraded}%!")
                st.rerun()
            else:
                st.error("❌ Not enough Doins!")
    else:
        st.write("🏆 Maximum crit chance reached!")

    st.markdown("#### 🚀 Critical Hit Multiplier")
    cost = 25000 * st.session_state.dice_crit_multiplier
    st.write(f"Increase crit multiplier by 50 for {rounder(cost)} Doins")
    
    crit_mult_qty = st.number_input("Quantity", min_value=1, max_value=20, value=1, key="crit_mult_qty")
    
    if st.button("Upgrade Crit Multiplier", use_container_width=True):
        success, upgraded = upgrade_crit_multiplier(crit_mult_qty)
        if success:
            st.success(f"✅ Increased crit multiplier by {upgraded * 50}!")
            st.rerun()
        else:
            st.error("❌ Not enough Doins!")

st.markdown("---")

# Reset game
if st.button("🔄 Reset Game", type="secondary"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

st.markdown("---")
st.markdown("*Roll dice to earn Doins and upgrade your dice for bigger rolls!*")