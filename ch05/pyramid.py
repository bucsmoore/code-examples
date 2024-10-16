def star_pyramid(n, p):  # n = num, p = "nothing"
    for i in range(n):
        print("*" * (i + 1))

    # [print("*" * (i + 1)) for i in range(int(input("Number of rows: ")))]


def rstar_pyramid():
    for i in range(num, 0, -1):
        print("*" * (i))


num = int(input("Number of rows: "))
star_pyramid(num, "nothing")
print(num)
# rstar_pyramid()
