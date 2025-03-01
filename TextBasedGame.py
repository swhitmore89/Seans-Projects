'''
Name: Sean Whitmore
Teacher: Francis Fiskey
Class: IT-140
Week 7 Final Project
Date: 2/15/2025
'''


def show_intro():
    """Displays the game introduction."""
    print("Welcome to the Legends of the Hidden Temple!")
    print("You have been chosen to embark on a perilous journey deep within the ancient temple.")
    print("Your mission: Collect powerful artifacts, evade deadly traps, and confront the fearsome guardian, Silph.")
    print("Claim the legendary Olmec Idol and prove your courage!")
    print("--------------------------------------------------")


def show_instructions():
    """Displays the game instructions."""
    print("To move, type 'go North', 'go South', 'go East', or 'go West'.")
    print("To examine your surroundings, type 'look'.")
    print("To check your inventory, type 'inventory'.")
    print("To get an item, type 'get [item name]'.")
    print("To quit the game, type 'quit'.")
    print("--------------------------------------------------")


def move_player(current_room, direction, room_connections):
    """
    Handles player movement between rooms.

    Args:
        current_room: Current room of the player (str).
        direction: Chosen direction (str).
        room_connections: Dictionary of room connections.

    Returns:
        The name of the new room if the move is valid, otherwise None.
    """
    current_room = current_room.lower()  # Normalize case for consistency
    if current_room in room_connections and direction in room_connections[current_room]:
        return room_connections[current_room][direction]
    else:
        return None


def get_item(current_room, inventory, room_items):
    """
    Allows the player to retrieve items from the room.

    Args:
        current_room: Current room of the player (str).
        inventory: List of items in the player's inventory.
        room_items: Dictionary mapping rooms to available items.

    Returns:
        True if an item is successfully added to inventory, False otherwise.
    """
    current_room = current_room.lower()  # Normalize case for consistency
    if current_room in room_items:
        item_name = room_items[current_room].lower()
        inventory.append(item_name)
        del room_items[current_room]
        print(f"You picked up the {item_name}!")
        return True
    else:
        print("There is no item to get here.")
        return False


def check_for_win(current_room, inventory, items):
    """
    Checks if the player has won the game.

    Args:
        current_room: Current room of the player (str).
        inventory: List of items in the player's inventory.
        items: List of all required items (list of str).

    Returns:
        True if the player wins, otherwise False.
    """
    current_room = current_room.lower()  # Normalize case for consistency
    if current_room == "chamber of olmec" and set(inventory) == set(items):
        return True
    return False

def play_game():
    """
    Starts and manages the main gameplay loop.
    """
    while True:  # Allows restarting the game
        # Define the game map and initial states
        rooms = {
            "temple entrance": {"North": "bridge of the serpent"},
            "bridge of the serpent": {"North": "hall of the jaguar", "West": "hall of moai"},
            "hall of the jaguar": {"West": "maze of mirrors", "South": "bridge of the serpent"},
            "maze of mirrors": {},  # Silph is placed here.
            "hall of moai": {"North": "maze of mirrors", "East": "bridge of the serpent",
                             "South": "temple of the moon"},
            "temple of the moon": {"North": "hall of moai", "West": "temple of the sun"},
            "temple of the sun": {"South": "chamber of olmec", "East": "temple of the moon"},
            "chamber of olmec": {"North": "temple of the sun"}
        }

        items = ["amulet of strength", "sun stone", "rope of ages", "spider's eye", "jaguar claw"]

        room_items = {
            "hall of moai": "amulet of strength",
            "temple of the sun": "sun stone",
            "bridge of the serpent": "rope of ages",
            "temple of the moon": "spider's eye",
            "hall of the jaguar": "jaguar claw"
        }

        current_room = "temple entrance"  # Normalized for consistency
        player_inventory = []
        villian_room = "maze of mirrors"  # Location of Silph

        show_intro()
        show_instructions()

        # Main game loop
        while True:
            print(f"\nYou are currently in the {current_room.capitalize()}.")
            if current_room in room_items:
                print(f"You see a {room_items[current_room]} here.")

            print("\nWhat do you want to do?")
            player_input = input().lower()

            if player_input.startswith("go "):
                direction = player_input.split(" ")[1].capitalize()
                new_room = move_player(current_room, direction, rooms)
                if new_room:
                    current_room = new_room
                else:
                    print("You cannot go that way.")
            elif player_input == "look":
                print(f"\nYou are in the {current_room}.")
                if current_room in room_items:
                    print(f"You see a {room_items[current_room]} here.")
                else:
                    print("There is nothing of particular interest here.")
            elif player_input == "inventory":
                print("\nYour Inventory:")
                for item in player_inventory:
                    print(f"- {item}")
            elif player_input.startswith("get "):
                item_name = player_input[4:].strip().lower()
                if current_room in room_items and room_items[current_room].lower() == item_name:
                    get_item(current_room, player_inventory, room_items)
                else:
                    print("You cannot get that item here.")
            elif player_input == "quit":
                print("Goodbye, adventurer!")
                return  # Exits the game loop entirely
            elif player_input == "instructions":
                show_instructions()
            else:
                print("Invalid command. Please try again.")

            if current_room == villian_room:
                print("\nAs you take a step forward, your body freezes."
                      "Before you stands Silph, the fearsome guardian of the temple.")
                print("His gaze freezes you in your tracks.")
                print("With a swift motion, Silph ends your journey. GAME OVER.")
                break  # Player loses and the game ends

            if check_for_win(current_room, player_inventory, items):
                print("\nCongratulations! You have conquered the Hidden Temple and claimed the Olmec Idol!")
                break  # Player wins and the game ends
            else:
                if current_room == "chamber of olmec":
                    missing_items = set(items) - set(player_inventory)
                    if missing_items:
                        print(f"You are in the Chamber of Olmec, but you are missing the following items: "
                              f"{', '.join(missing_items)}.")
                    else:
                        print("Keep exploring the temple!")

        # Ask the player if they want to restart
        restart = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thank you for playing! Goodbye!")
            break  # Exit the outermost loop, ending the game




if __name__ == "__main__":
    play_game()