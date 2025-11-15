from time import *
from random import *
from os import *


def animated_print(text):
    for char in text:
        print(char, end="", flush=True)
        sleep(0.06)


def yes_input(y):
    global n, m, name, a, count, gender
    n = 1
    m = 100
    name = input("What is your name??😃\n")

    while True:
        gender = input("\nWhat is your gender Male or Female ??😃\n")
        gender = gender.strip().capitalize()
        if gender == "Male":
            name = "Mr." + name.strip().capitalize()
            break
        elif gender == "Female":
            name = "Ms." + name.strip().capitalize()
            break
        animated_print("Please enter a valid gender!!😡\n(Male or Female)??")

    animated_print("Please guess a number between 1 to 100 !!!")
    Question = input("\n(Whenever you guessed , please enter Y):\n")
    Question = Question.upper().strip()

    while Question != "Y":
        print("Please enter a valid alphabet!!😡")
        Question = input("\n(Whenever you guessed , please enter Y):\n")
        Question = Question.upper().strip()
    if Question == "Y":
        a = randint(n, m)
        count = 0
        print("\n", a)


win_loss_list = []


def main():
    global hint, count, n, m, a, name
    yes_input("Y")
    hint = input(f"Is it higher or lower or correct, {name}?\n").strip()
    while True:
        count = 0
        while hint != "correct":

            if hint == "higher":
                count += 1
                n = a + 1
                a = randint(n, m)
                print(a)
                hint = input(f"Is it higher or lower or correct, {name}?\n").strip()
            elif hint == "lower":
                count += 1
                m = a - 1
                a = randint(n, m)
                print(a)
                hint = input(f"Is it higher or lower or correct, {name}?\n").strip()
            else:
                hint = input(
                    f"Please enter a valid hint: higher or lower or correct, {name}?😡\n"
                ).strip()
        while hint == "correct":
            animated_print(
                f"\nBravo!, you found it!👏\nYou are a true winner🥇, {name}!!!\n"
            )
            print("\nthe number was", a)
            system(
                "afplay /Users/nikan86p/Downloads/Nikan-mabani/Drums.mp3"
            )  # You can download any sound you want and add it here for playing plus if you don't want it you can comment this
            break

        animated_print(f"\nDo you want to play again, {name}??\n")
        answer = input("Enter Y for Yes and N for No: ").strip()
        if answer.upper() == "Y":
            win_loss_list.append(
                f"{name}: Win by count of: {count+1}; and the number was {a} "
            )
            animated_print("\nGreat! Let's play again.\nRestarting the game...✨\n\n")
            sleep(3)
            yes_input("Y")
            hint = input(f"Is it higher or lower or correct, {name}?\n").strip()
            continue
        elif answer.upper() == "N":
            win_loss_list.append(
                f"{name}: Win by count of: {count+1}; and the number was {a} "
            )
            print(win_loss_list)
            rounds_of_play = len(win_loss_list)
            print(f"\nYou played this game {rounds_of_play} times!!!")
            sleep(2)
            animated_print("\nThank you for playing the game! Goodbye!👋\n\n")
            break
        else:
            while True:
                answer = (
                    input("\nInvalid input! Please enter Y or N: 😡").strip().upper()
                )
                if answer == "Y":
                    win_loss_list.append(
                        f"{name}: Win by count of: {count+1}; and the number was {a} "
                    )
                    animated_print(
                        "\nGreat! Let's play again.\nRestarting the game...✨\n\n"
                    )
                    sleep(3)
                    yes_input("Y")
                    hint = input(f"Is it higher or lower or correct, {name}?\n").strip()
                    break
                elif answer == "N":
                    win_loss_list.append(
                        f"{name}: Win by count of: {count+1}; and the number was {a} "
                    )
                    print("\n", win_loss_list)
                    rounds_of_play = len(win_loss_list)
                    print(f"\nYou played this game {rounds_of_play} times!!!")
                    sleep(2)
                    animated_print("\nThank you for playing the game! Goodbye!👋\n\n")
                    exit()
                else:
                    continue


if __name__ == "__main__":
    main()
