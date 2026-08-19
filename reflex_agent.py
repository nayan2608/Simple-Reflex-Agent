import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ============================================================
# 1. DEFINE THE ENVIRONMENT
# ============================================================
# We have 4 rooms in our environment.
# Each room can either be "Clean" or "Dirty".
environment = {
    "Room1": "Clean",
    "Room2": "Dirty",  
    "Room3": "Clean",
    "Room4": "Clean"
}

# ============================================================
# 2. DEFINE ROOM POSITIONS
# ============================================================
# We are representing the environment as a 2x2 grid.
#
#       Room1 | Room2
#       ------+------
#       Room3 | Room4
#
# (x, y) represents the position of each room.
room_positions = {
    "Room1": (0, 1),  # Top-left
    "Room2": (1, 1),  # Top-right
    "Room3": (0, 0),  # Bottom-left
    "Room4": (1, 0)   # Bottom-right
}

# Get the list of room names.
# The agent will use the index to determine its current room.
rooms = list(environment.keys())  

# Initially, the agent starts in Room1.
agent_index = 0  

# ============================================================
# 3. REFLEX AGENT
# ============================================================
# A reflex agent makes a decision based only on the
# current state of the environment.
#
# Rules:
#   - If the current room is Dirty -> Clean it.
#   - If the current room is Clean -> Move to the next room.
def reflex_agent(state):
    if state == "Dirty":
        return "Clean"
    else:
        return "Move"
        
# ============================================================
# 4. DRAW THE ENVIRONMENT
# ============================================================
# This function visually displays:
#   - Clean rooms in green
#   - Dirty rooms in red
#   - Agent as a blue circle
#
# Parameters:
#   env       -> Current environment state
#   agent_pos -> Current position/index of the agent
#   step      -> Current simulation step
def draw_environment(env, agent_pos, step):
    # Create a new figure and axis.
    fig, ax = plt.subplots()

    # Set the size of the 2x2 grid.
    ax.set_xlim(0, 2) 
    ax.set_ylim(0, 2) 

    # Hide x-axis and y-axis numbers.
    ax.set_xticks([])
    ax.set_yticks([]) 

    # Display the current step and agent's location.
    ax.set_title(f"Step {step} — Agent in {rooms[agent_pos]}")

    for room, pos in room_positions.items():  
        x, y = pos
        color = 'red' if env[room] == "Dirty" else 'green'  
        rect = patches.Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black') 
        ax.add_patch(rect)
        ax.text(x + 0.5, y + 0.5, room, ha='center', va='center', color='white', fontsize=10) # "Room1"

    # Draw agent
    agent_x, agent_y = room_positions[rooms[agent_pos]] # Finds the agent's current position.
    agent_patch = patches.Circle((agent_x + 0.5, agent_y + 0.5), 0.1, color='blue') #blue circle
    ax.add_patch(agent_patch)

    plt.pause(1) 
    plt.close() 
     
     
     
# ============================================================
# 5. RUN THE SIMULATION
# ============================================================

# Turn on interactive plotting.
# This allows the environment to update step by step.
plt.ion()  
steps = 8  

# Run the simulation for the specified number of steps.
for step in range(steps):
    current_room = rooms[agent_index] 
    state = environment[current_room] 
    action = reflex_agent(state) 

    draw_environment(environment, agent_index, step + 1) 

    if action == "Clean": # If the agent decides to clean, this line updates the environment, marking the room as "Clean".
        environment[current_room] = "Clean"
    else:
        agent_index = (agent_index + 1) % len(rooms) 
        print(f"Step {step + 1}: " f"Agent moved to {rooms[agent_index]}")


# ============================================================
# 6. END THE SIMULATION
# ============================================================

# Turn off interactive plotting.
plt.ioff() 
print("✅ Simulation complete!") 
