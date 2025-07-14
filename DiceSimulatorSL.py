import streamlit as st
import random

# Initialize session state variables
def init_session_state():
    if 'dice_rollable' not in st.session_state:
        st.session_state.dice_rollable = 1
    if 'dice_rolled' not in st.session_state:
        st.session_state.dice_rolled = 0
    if 'dice_multiplier' not in st.session_state:
        st.session_state.dice_multiplier = 1
    if 'dice_crit_chance' not in st.session_state:
        st.session_state.dice_crit_chance = 10
    if 'dice_crit_multiplier' not in st.session_state:
        st.session_state.dice_crit_multiplier = 20
    if 'roll_history' not in st.session_state:
        st.session_state.roll_history = []
    if 'dice_type' not in st.session_state:
        st.session_state.dice_type = "d6"
    if 'dice_s' not in st.session_state:
        st.session_state.dice_s = 6
    if 'doin' not in st.session_state:
        st.session_state.doin = 100

# Constants
UPGRADE_COST = {
    "d6": 5000, 
    "d8": 15000, 
    "d10": 50000, 
    "d12": 250000, 
    "d20": 1000000, 
    "d100": 10000000
}

DICE_TYPES = ["d6", "d8", "d10", "d12", "d20", "d100"]

DICE_SIDES = {
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
        return 3000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 10:
        return 10000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 12:
        return 50000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 20:
        return 200000 * st.session_state.dice_rollable
    elif st.session_state.dice_s == 100:
        return 2000000 * st.session_state.dice_rollable

def roll_dice():
    """Roll dice and update currency"""
    d_sides = DICE_SIDES[st.session_state.dice_type]
    roll = 0
    roll_details = []

    for i in range(st.session_state.dice_rollable):
        r = random.randint(1, d_sides)
        roll_details.append(f"Die {i + 1}: {rounder(r)}")
        roll += r
    
    original_roll = roll
    roll *= st.session_state.dice_multiplier
    
    crit_hit = False
    if st.session_state.dice_crit_chance > 0:
        if random.random() < st.session_state.dice_crit_chance / 100:
            crit_hit = True
            roll *= st.session_state.dice_crit_multiplier
    
    st.session_state.doin += roll
    
    # Store roll in history
    roll_info = {
        'details': roll_details,
        'total': rounder(original_roll),
        'multiplied': rounder(roll if not crit_hit else roll // st.session_state.dice_crit_multiplier),
        'final': rounder(roll),
        'crit': crit_hit
    }
    
    return roll_info

def upgrade_dice_type():
    """Upgrade dice type"""
    cost = UPGRADE_COST[st.session_state.dice_type]
    if st.session_state.doin >= cost:
        st.session_state.doin -= cost
        current_index = DICE_TYPES.index(st.session_state.dice_type)
        if current_index < len(DICE_TYPES) - 1:
            st.session_state.dice_type = DICE_TYPES[current_index + 1]
            st.session_state.dice_s = DICE_SIDES[st.session_state.dice_type]
            return True, f"Upgraded to {st.session_state.dice_type}!"
        else:
            return False, "You have reached the maximum dice type!"
    else:
        return False, f"You need {rounder(cost)} Doins to upgrade!"

def upgrade_dice_amount():
    """Upgrade number of rollable dice"""
    cost = dice_amount_upgrade_cost()
    if st.session_state.doin >= cost:
        st.session_state.doin -= cost
        st.session_state.dice_rollable += 1
        return True, f"Now rolling {st.session_state.dice_rollable} dice!"
    else:
        return False, f"You need {rounder(cost)} Doins to upgrade!"

def main():
    st.set_page_config(page_title="🎲 Dice Simulator", page_icon="🎲", layout="wide")
    
    # Initialize session state
    init_session_state()
    
    # Title and header
    st.title("🎲 Dice Simulator")
    st.markdown("---")
    
    # Create columns for layout
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        st.header("💰 Your Stats")
        st.metric("Doins", rounder(st.session_state.doin))
        st.metric("Dice Type", st.session_state.dice_type)
        st.metric("Rollable Dice", st.session_state.dice_rollable)
        st.metric("Dice Multiplier", f"{st.session_state.dice_multiplier}x")
        st.metric("Crit Chance", f"{st.session_state.dice_crit_chance}%")
        st.metric("Crit Multiplier", f"{st.session_state.dice_crit_multiplier}x")
    
    with col2:
        st.header("🎯 Actions")
        
        # Roll Dice Button
        if st.button("🎲 Roll Dice", type="primary", use_container_width=True):
            roll_info = roll_dice()
            
            # Display roll results
            st.success("🎉 Roll Results:")
            for detail in roll_info['details']:
                st.write(f"• {detail}")
            
            st.write(f"**Total:** {roll_info['total']}")
            
            if st.session_state.dice_multiplier > 1:
                st.write(f"**After {st.session_state.dice_multiplier}x multiplier:** {roll_info['multiplied']}")
            
            if roll_info['crit']:
                st.write("💥 **CRITICAL HIT!**")
                st.write(f"**Final amount:** {roll_info['final']}")
            
            st.write(f"**New total Doins:** {rounder(st.session_state.doin)}")
        
        st.markdown("---")
        
        # Upgrade Dice Type
        next_dice_type = None
        current_index = DICE_TYPES.index(st.session_state.dice_type)
        if current_index < len(DICE_TYPES) - 1:
            next_dice_type = DICE_TYPES[current_index + 1]
        
        if next_dice_type:
            upgrade_cost = UPGRADE_COST[st.session_state.dice_type]
            if st.button(f"⬆️ Upgrade to {next_dice_type}\n({rounder(upgrade_cost)} Doins)", 
                        use_container_width=True):
                success, message = upgrade_dice_type()
                if success:
                    st.success(message)
                else:
                    st.error(message)
        else:
            st.info("🏆 Maximum dice type reached!")
        
        # Upgrade Dice Amount
        amount_cost = dice_amount_upgrade_cost()
        if st.button(f"➕ Add Dice\n({rounder(amount_cost)} Doins)", 
                    use_container_width=True):
            success, message = upgrade_dice_amount()
            if success:
                st.success(message)
            else:
                st.error(message)
    
    with col3:
        st.header("📊 Upgrade Costs")
        
        # Show all upgrade costs
        st.subheader("Dice Type Upgrades:")
        for i, dice_type in enumerate(DICE_TYPES):
            if i == 0:
                st.write(f"• {dice_type} (Starting)")
            else:
                prev_dice = DICE_TYPES[i-1]
                cost = UPGRADE_COST[prev_dice]
                if dice_type == st.session_state.dice_type:
                    st.write(f"• **{dice_type} (Current)**")
                elif DICE_TYPES.index(st.session_state.dice_type) < i:
                    st.write(f"• {dice_type} ({rounder(cost)} Doins)")
                else:
                    st.write(f"• ~~{dice_type}~~ (Owned)")
        
        st.subheader("Dice Amount:")
        st.write(f"Next dice: {rounder(dice_amount_upgrade_cost())} Doins")
        
        # Reset button
        st.markdown("---")
        if st.button("🔄 Reset Game", type="secondary", use_container_width=True):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.experimental_rerun()

if __name__ == "__main__":
    main()