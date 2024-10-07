import random

num = random.randint(1, 100)
num_guesses = 0
guess = -1
while guess != num:
    guess = int(input("Enter a guess: "))
    if guess > num:
        print("Too high")
    elif guess < num:
        print("too low")
    num_guesses += 1

print("Correct! It took ", num_guesses)
