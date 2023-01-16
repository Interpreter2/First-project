# Adventure Game

# Initialize player's starting location
location = "forest"

# Define the different locations in the game
locations = {
    "forest": "You find yourself in a dense forest. You see a path to the left and a path to the right.",
    "cave": "You find yourself in a dark cave. You see a faint light to the left and a passage to the right.",
    "beach": "You find yourself on a beautiful beach. You see a ship in the distance and a path leading into the jungle."
}

# Define the actions that the player can take in each location
actions = {
    "forest": ["left", "right"],
    "cave": ["left", "right"],
    "beach": ["ship", "jungle"]
}

# Define the outcomes of the actions
outcomes = {
    "forest,left": "cave",
    "forest,right": "beach",
    "cave,left": "beach",
    "cave,right": "forest",
    "beach,ship": "end",
    "beach,jungle": "end"
}

# Print the starting locationd
print(locations[location])

# Start the game loop
while True:
    # Get the player's action
    action = input("What would you like to do? ").lower()

    # Check if the action is valid
    if action in actions[location]:
        # Determine the outcome of the action
        outcome = outcomes[location + "," + action]
        # Check if the game is over
        if outcome == "end":
            print("Thanks for playing!")
            break
        # Update the player's location
        location = outcome
        # Print the new location
        print(locations[location])
    else:
        print("Invalid action.")