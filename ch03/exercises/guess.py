import random

num = random.randrange(1, 11)

guess = -1

for _ in range(3):
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == num:
        print("You guessed it!")
        break
    elif guess < num:
        print("Too low!", num)
    else:
        print("Too high!", num)


# for _ in range(10):

#     for __ in range(10):
#         break

#     print(_)
# mylist = ['a', 'b', 'c']
# for num in mylist: #num = mylist[n]
#     print(num)
#     num = num + 5  # num += 5
#     print(num)
