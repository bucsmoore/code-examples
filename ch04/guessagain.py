import random

num = random.randrange(1000) + 1
tries = 1
guess = int(input("What number, between 1-1000, do you guess?"))

while guess != num:
    tries += 1
    if guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    guess = int(input("Again, what number, between 1-1000, do you guess?"))


print("Correct. It took you", tries, "guesses.")
print("It should only take you, at most", log(1000, 2), "guesses.")
