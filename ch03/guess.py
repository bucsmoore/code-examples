import random

random_number = random.randint(1, 2)
guessed = False  # flag variable

for i in range(3):
    if not guessed:
        user_guess = int(input("What is your guess?"))
        if user_guess == random_number:
            print("You did it! the number was:", random_number)
            # break
            # exit() #okay in single scripts, but ends the program
            guessed = True
        elif user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")


if guessed:
    print("Do something")

for i in range(3):
    for j in range(3):
        pass
    break  # only breaks nearest loop
