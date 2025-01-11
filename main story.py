import random
import time
from classes import characters
from enemies import enemies


lines = {
    "first_line": (
        "As you weave through the bustling streets, the cacophony of the port fades, replaced by the hum of city life.\n"
        "Narrow alleys lined with colorful stalls lead you to the tavern. Its sign—a golden tankard glowing faintly with\n"
        "magical light—hangs above a heavy wooden door reinforced with iron. The building itself is a sturdy structure of\n"
        "dark wood and stone, its windows glowing warmly against the mid-morning haze.\n"
        "Inside, the scent of roasted meats, stale ale, and well-worn leather envelops you.\n"
        "Adventurers of all kinds fill the room: cloaked figures hunched over maps, brawny fighters boasting of past exploits,\n"
        "and spellcasters in deep conversation about arcane mysteries.\n"
        "A hulking half-orc stands behind the bar, polishing a tankard with a rag that looks no cleaner than the mug itself.\n"
        "Behind him, a notice board brims with quests and bounties, each promising gold and glory.\n"
        "A grizzled elf seated near the bar gestures you to approach. His sharp eyes scan you with practiced scrutiny."
    )
} #first line, the line that the game will start with once the player has selected the class.
characters = {
    "Archer": {
        "name": "Artemis",
        "HP": 50,
        "AC": 14,
        "Attack_range": "20ft", #Archer has 20ft attack range
        "Damage_range": (1,8), # Archer uses 1d8 for attack damage
        "Special_ability": "Rapid Shot"
    },
    "Wizard": {
        "name": "Eviar",
        "HP": 40,
        "AC": 12,
        "Attack_range": "25ft", # Wizard has 25ft attack range
        "Damage_range": (1,10), # Wizard uses 1d10 for attack damage
        "Special_ability": "Mana Shield"
    },
    "Barbarian": {
        "name": "Yudrom",
        "HP": 100,
        "AC": 16,
        "Attack_range": "5ft", # Barbarian has 5ft attack range
        "Damage_range": (2,6), # Barbarian uses 2d6 for attack damage
        "Special_ability": "Rage"
    }
}

enemies = {
    "Goblin": {
         "AC": 12, # Armour Class
         "HP": 15, # Hit Points
         "Attack": [1,6] # Damage range for attacks (1d6)
    },
    "Skeleton": {
        "AC": 10, # Armour Class
         "HP": 20, # Hit Points
         "Attack": [1,8] # Damage range for attacks (1d8)
    },
    "Orc": {
        "AC": 14, # Armour Class
        "HP": 35, # Hit Points
        "Attack": [1,10] # Damage range for attacks (1d10)
    }
}

# Function to display class information
def display_class_info(class_name):
    if class_name in characters:
        class_info = characters[class_name]
        print(f"\n{class_name} Stats:")
        for key, value in class_info.items():
            print(f"{key}: {value}")


# Function to ask for class selection
def choose_class():
    while True:  # Keep asking until the player confirms their selection
        # Ask the player for their choice
        player_choice = input("Choose a class (Archer, Wizard, Barbarian): ")

        # Show the class stats
        if player_choice in characters:
            display_class_info(player_choice)

            # Ask for confirmation
            confirm = input(f"Do you confirm {player_choice} as your class? (yes/no): ")

            if confirm == "yes":
                print(f"{player_choice} is now your selected class!")
                return player_choice
            else:
                print("Let's pick another class.")
        else:
            print("Invalid choice. Please select a valid class.")


# Start the class selection process
#choose_class()


def slow_type(text, delay=0.025):
    for word in text:
        print(word, end='', flush=True)
        time.sleep(delay)
    print()
#slow_type(lines["first_line"])


def roll_dice(command):
     #Check the dice format
    if command == "1d20":
        roll = random.randint(1, 20)  # Rolls a number between 1 and 20
        print(f"Rolled 1d20: {roll}")
        return roll
    elif command == "1d6":
        roll = random.randint(1, 6)  # Rolls a number between 1 and 6
        print(f"Rolled 1d6: {roll}")
        return roll
    elif command == "1d8":
        roll = random.randint(1, 8)  # Rolls a number between 1 and 8
        print(f"Rolled 1d8: {roll}")
        return roll
    elif command == "1d10":
        roll = random.randint(1, 10)  # Rolls a number between 1 and 10
        print(f"Rolled 1d10: {roll}")
        return roll
    else:
        print("Invalid command! Use one of the following formats: 1d20, 1d6, 1d8, 1d10,")
        return 0



#============================================================================================================

#choose_class()
#slow_type(lines["first_line"])

#command = input("Enter dice roll command (e.g., 1d6, 1d8, 1d10, 1d20): ")
#roll_dice(command)

def elf_interaction():
    slow_type("\nThe grizzled elf peers at you with sharp eyes and speaks,"
              "\n his voice carrying a weight of authority")
    slow_type('"So, you wish to join the guild?"', delay=0.03)

    while True:
        response = input("\nDo you want to join the guild? (yes/no): ")
        if response == "yes":
            slow_type("\nThe elf nods approvingly."
                      "\n'Very well. Before you are granted membership, you must prove your worth.'"
                      "\n'Your task is very simple yet dangerous:"
                      "\nClear the first floor of the labyrinth beneath this city and you will earn a place among us'")
            break
        elif response == "no":
            slow_type("\nThen you have no business here")
        else:
            print("\nInvalid response. Please type 'yes' or 'no'.")
#elf_interaction()

def entrace_labyrinth():
    slow_type("\nYou step into the labyrinth, its moss-covered stone walls lit by flickering torches.")
    slow_type("\nThe air is cold and damp, and shadows dance around you. The fight awaits.")
    slow_type("\nIn front of you, you see a figure, looking for a fight")

#entrace_labyrinth()

def roll_dice(min_val, max_val):
    return random.randint(min_val, max_val)

def combat1(class_name, enemy_name):
    player = characters[class_name]
    enemy = enemies[enemy_name]

    print(f"\nA {enemy_name} appears! Prepare for battle!\n")
#player's turn to attack
    while player["HP"] > 0 and enemy["HP"] > 0:
        print(f"\nYour damage range: {player["Damage_range"][0]}d{player["Damage_range"][1]}")

        while True:
            player_roll_input = input(f"Roll the dice for your attack damage (type {player["Damage_range"][0]}d{player["Damage_range"][1]} to proceed): ")

            if player_roll_input == f"{player["Damage_range"][0]}d{player["Damage_range"][1]}":
                if player["Damage_range"][0] == 1:
                    player_damage = roll_dice(1, player["Damage_range"][1])

            else:
                player_damage = sum(roll_dice(1, player["Damage_range"][1]) for _ in range(player["Damage_range"][0]))
            print(f"You rolled the dice and deal {player_damage} damage to the {enemy_name}!")
            enemy["HP"] -= player_damage
            break
        else:
            print("Invalid dice format. Please try again")

        if enemy["HP"] <= 0:
            print(f"\nYou defeated the {enemy_name}!")
            break
#enemy's turn to attack
        enemy_damage = roll_dice(enemy["Attack"][0], enemy["Attack"][1])
        print(f"\nThe {enemy_name} attacks and deals {enemy_damage} damage!")
        player["HP"] -= enemy_damage

        if player["HP"] <= 0:
            print("\nYou have been defeated! Game over.")
            break

        print(f"\nYour HP: {player["HP"]} / {enemy_name} HP: {enemy["HP"]}")


#====================
def main():
    chosen_class = choose_class()
    #slow_type(lines["first_line"])
    #elf_interaction()
    #entrace_labyrinth()
    combat1(chosen_class,"Goblin")


main()

