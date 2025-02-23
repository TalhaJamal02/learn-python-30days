import random

# Mini Project 1
# Simple Calculator


def calculator():
    while True:
        try:
            print("Simple Calculator")
            print("Operations: +, -, *, /")

            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Error! Division by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation!")
                continue

            print(
                f"✅ Result: {int(result) if result.is_integer() else result}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        again = input(
            "Do you want to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            break


calculator()


# Mini Project 2
# Number Guessing Game
def guessing_game():
    # random integer (randint) between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 10.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print(f"📉 Too low! Try again.")
        elif guess > secret_number:
            print(f"📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break


guessing_game()


# Mini Project 4
# To-Do List (CLI-Based)
def todo_list():
    todos = []

    while True:
        print("\n💡 To-Do List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Save and Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter a task: ")
            todos.append(task)
            print(f"✅ Task added: {task}")

        elif choice == "2":
            if not todos:
                print("📌 No tasks available.")
            else:
                print("\nYour To-Do List:")
                for idx, todo in enumerate(todos, start=1):
                    print(f"{idx}. {todo}")

        elif choice == "3":
            if not todos:
                print("❌ No tasks to remove.")
                continue
            try:
                task_no = int(input("Enter the task number to remove: "))
                if 1 <= task_no <= len(todos):
                    removed_task = todos.pop(task_no - 1)
                    print(f"🗑️ Removed: {removed_task}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        elif choice == "4":
            print("👋 Exiting To-Do List.")
            break


todo_list()


# Mini Project 3
# Word Counter
def word_counter():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(f"Number of words: {len(words)}")


word_counter()
