# def myfunction(x):  # x = y
#     # x = 6
#     x = str(x + 5) * 10  # "11" => 111111..., 11 => 110
# #     print(x)


# # def myfunction(x):  # x = y
# #     # gathering data
# #     # x = input("What is your number?")
# #     x = str(x + 5) * 10  # processing data
# #     print(x)


# # # x = 7
# # # x = str(x + 5) * 10
# # # print(x)
# # y = 7
# # x = input("What is your number?")
# # myfunction(y)
# # print(myfunction)
# # # x = 9
# # # x = str(x + 5) * 10
# # # print(x)
# # y = 10
# # myfunction(y)
# # # x = 7
# # # x = str(x + 5) * 10
# # # print(x)
# # y = 2.3
# # myfunction(y)

# # y = "2"
# # myfunction(y)

# # print()
# # print(5, 7)
# # print(7)


# # This s not running code


# def myfunction(x, y, z):  # x = y
#     print(x, y, z)


# # Positional arguments
# myfunction(5, 6, 7)

# # keyword arguments
# myfunction(y=5, z=6, x=7)


# def myfunction(y, x, z=1):  # x = y
#     x = 1
#     y = 2
#     z = 3
#     total = x + y + z  # created
#     print(total)
#     # x,y,z,total


# my_value = 10
# # Positional arguments - Required
# myfunction(5, 6)

# # keyword arguments - Optional if given a default value
# myfunction(y=5, z=1, x=7)

# # a = 1
# # b = 2
# # c = 3
# x = 100
# y = 200
# z = 300
# jhgfliasdghalkwhvaCHGKJF = 7
# myfunction(y=x, z=y, x=jhgfliasdghalkwhvaCHGKJF)
# print(total)


def find_max(numbers=[1,2,3]): {"numbers":[1,2,3]}
    max = numbers[0]
    if numbers[1] > max:
        max = numbers[1]
    if numbers[2] > max:
        max = numbers[2]

    print(max)


num_list = input("Please enter 3 numbers separated by commas: ")
num_list = num_list.split(",")
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

find_max(numbers=num_list) #find_max["numbers"] = num_list