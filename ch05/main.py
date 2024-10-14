# print("Hello")  # procedure
# val = input("input something")  # functions return a value


# def myfunc():
#     x = 5  # variable created inside a function are dleted when the function ends
#     print("in function")
#     print("still in the function")
#     print(x) # the variable's scope


# myfunc()

# print(x) - invalid


## find max


def findmax():
    nums = []
    new_num = int(input("add some numbers (0 to stop): "))
    while new_num:
        nums.append(new_num)
        new_num = int(input("add some numbers (0 to stop): "))

    max = nums[0]
    for i in nums:
        if i > max:
            max = i

    print(max)


findmax()
# do some more code
findmax()
# do some more code
findmax()
