import random

random_number = random.randint(1, 1000)
num_guesses = 0
user_guess = -1
while random_number != user_guess:
    user_guess = int(input("What is your guess?"))
    if user_guess > random_number:
        print("Too High")
    elif user_guess < random_number:
        print("Too Low")
    num_guesses = num_guesses + 1
    # num_guesses += 1 #syntatic sugar
    
print("You did it! the number was:", random_number)
print("You took "+ str(num_guesses) + " guesses to get it.")

#binary search, set of size n, searches: log(n)


