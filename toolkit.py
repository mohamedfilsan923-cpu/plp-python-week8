import random

# List to store tasks while the program runs
tasks = []

# Welcoming start message
print("==========================================")
print("   Welcome to Filsan's Personal Toolkit!  ")
print("==========================================")

# Main menu loop - keeps running until Quit (4) is chosen
while True:
    print("\n=== PERSONAL TOOLKIT MENU ===")
    print("1. To-Do List Manager")
    print("2. Simple Calculator")
    print("3. Number-Guessing Game")
    print("4. Quit")

    choice = input("Choose a tool (1-4): ").strip()

    # TOOL 1: To-Do List Manager
    if choice == "1":
        while True:
            print("\n--- TO-DO LIST MANAGER ---")
            print("a. Add a task")
            print("b. View tasks")
            print("c. Remove a task")
            print("d. Back to main menu")

            action = input("Select an action (a-d): ").strip().lower()

            if action == "a":
                new_task = input("Enter a new task: ").strip()
                if new_task:
                    tasks.append(new_task)
                    print(f"Added '{new_task}'! You now have {len(tasks)} task(s).")
                else:
                    print("Task cannot be blank. Please type something to add.")

            elif action == "b":
                if len(tasks) == 0:
                    print("Your to-do list is empty right now.")
                else:
                    print("\nYour Current Tasks:")
                    for number, item in enumerate(tasks, start=1):
                        print(f"  {number}. {item}")

            elif action == "c":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    print("\nWhich task would you like to remove?")
                    for number, item in enumerate(tasks, start=1):
                        print(f"  {number}. {item}")
                    try:
                        remove_num = int(input("Enter task number: ").strip())
                        if 1 <= remove_num <= len(tasks):
                            removed_task = tasks.pop(remove_num - 1)
                            print(f"Removed '{removed_task}'. {len(tasks)} task(s) remaining.")
                        else:
                            print(f"Please enter a number between 1 and {len(tasks)}.")
                    except ValueError:
                        print("Invalid input. Please enter a whole number.")

            elif action == "d":
                print("Returning to the main menu...")
                break

            else:
                print(f"'{action}' is not a valid option. Please choose a, b, c, or d.")

    # TOOL 2: Simple Calculator
    elif choice == "2":
        print("\n--- SIMPLE CALCULATOR ---")
        try:
            num1 = float(input("Enter the first number: ").strip())
            operator = input("Choose an operation (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: ").strip())

            if operator == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 == 0:
                    print("Error: You cannot divide by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {round(num1 / num2, 2)}")
            else:
                print(f"'{operator}' is not a supported operator. Please use +, -, *, or /.")
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

    # TOOL 3: Number-Guessing Game
    elif choice == "3":
        print("\n--- NUMBER-GUESSING GAME ---")
        secret_number = random.randint(1, 20)
        attempts = 0
        print("I am thinking of a number between 1 and 20. Can you guess it?")

        while True:
            try:
                guess = int(input("Your guess: ").strip())
                attempts += 1

                if guess < 1 or guess > 20:
                    print("Please guess a number between 1 and 20.")
                elif guess < secret_number:
                    print(f"{guess} is too low! Try a higher number.")
                elif guess > secret_number:
                    print(f"{guess} is too high! Try a lower number.")
                else:
                    print(f"Congratulations! You guessed {secret_number} in {attempts} attempt(s)!")
                    break
            except ValueError:
                print("That is not a whole number. Please enter a number from 1 to 20.")

    # OPTION 4: Quit Program
    elif choice == "4":
        print("\nThank you for using Filsan's Personal Toolkit. Goodbye!")
        break

    # Invalid menu choice
    else:
        print(f"Sorry, '{choice}' is not on the menu. Please enter 1, 2, 3, or 4.")