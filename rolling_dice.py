def roll_dice(command):
    # Check the dice format
    if command == "1d20":
        roll = random.randint(1, 20)  # Rolls a number between 1 and 20
        print(f"Rolled 1d20: {roll}")
    elif command == "1d6":
        roll = random.randint(1, 6)  # Rolls a number between 1 and 6
        print(f"Rolled 1d6: {roll}")
    elif command == "1d8":
        roll = random.randint(1, 8)  # Rolls a number between 1 and 8
        print(f"Rolled 1d8: {roll}")
    elif command == "1d10":
        roll = random.randint(1, 10)  # Rolls a number between 1 and 10
        print(f"Rolled 1d10: {roll}")
    else:
        print("Invalid command! Use one of the following formats: 1d20, 1d6, 1d8, 1d10,")
#Get the user input for the dice roll
command = input("Enter dice roll command (e.g., 1d6, 1d8, 1d10, 1d20): ")

#Call the roll_dice function with the user's input
roll_dice(command)