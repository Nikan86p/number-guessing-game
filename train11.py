from time import*
from random import*
from os import*


def animated_print(text):
    for char in text:
        print(char, end="", flush=True)
        sleep(0.06)



def yes_input(y):
    global n,m,name,a
    n = 1
    m = 100
    name=input("What is your name??😃\n")
    name="Mr."+name.capitalize()
    animated_print("Please guess a number between 1 to 100 !!!")
    Question=input("\n(Whenever you guessed , please enter Y):\n")
    Question=Question.upper()



    while Question!="Y":
            print("Please enter a valid alphabet!!😡")
            Question=input("\n(Whenever you guessed , please enter Y):\n")
            Question=Question.upper()
    if Question=="Y":
        a=randint(n,m)
        print("\n",a)




yes_input('Y')
hint=input(f"Is it higher or lower or correct, {name}?\n")
while True :
    while hint!="correct":
    
        if hint=="higher":
            n=a+1
            a=randint(n,m)
            print(a)
            hint=input(f"Is it higher or lower or correct, {name}?\n")
        elif hint=="lower":
            m=a-1
            a=randint(n,m)
            print(a)
            hint=input(f"Is it higher or lower or correct, {name}?\n")
        else:
            hint=input(f"Please enter a valid hint: higher or lower or correct, {name}?😡\n")
    while hint=="correct":
        animated_print(f"\nBravo!, you found it!👏\nYou are a true winner🥇, {name}!!!\n")
        print("\nthe number was",a)
        system("afplay /Users/nikan86p/Downloads/Nikan-mabani/Drums.mp3")
        break
    
    animated_print(f"\nDo you want to play again, {name}??\n")
    answer=input("Enter Y for Yes and N for No: ")
    if answer.upper()=='Y':
        animated_print("\nGreat! Let's play again.\nRestarting the game...✨\n\n")
        sleep(3)
        yes_input('Y')
        hint=input(f"Is it higher or lower or correct, {name}?\n")
        continue
    elif answer.upper()=='N':
        animated_print("\nThank you for playing the game! Goodbye!👋\n\n")
        break
    else:   
        while True:
            answer = input("\nInvalid input! Please enter Y or N: 😡").strip().upper()
            if answer == 'Y':
                animated_print("\nGreat! Let's play again.\nRestarting the game...✨\n\n")
                sleep(3)
                yes_input('Y')
                hint = input(f"Is it higher or lower or correct, {name}?\n")
                break  
            elif answer == 'N':
                animated_print("\nThank you for playing the game! Goodbye!👋\n\n")
                exit()  
            else:
                continue  