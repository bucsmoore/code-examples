
import random

num = random.randint(1, 10)
print(num)
flag_correct = False # flag variable
for _ in range(3):
    if not flag_correct:
        user_guess = int(input("Guess a number between 1 and 10"))

        if user_guess < num: # required, only 1, always has a condition
            print("Too low")
        elif user_guess > num:# optional, any number, always has a condition
            print("Too high")
        else:                   #optional, only 1, never has a condition
            print("correct")
            flag_correct = True
            # breaks out of the nearest loop
            # not used for if statement
            # break