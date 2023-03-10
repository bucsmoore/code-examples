# define a function
def star_pyramid(rows):  # rows=levels
    for i in range(1, rows + 1):  # range(5), range(1, 5), range(1, 5, 2)
        print("*" * i)


# define a function
def rstar_pyramid(stars):  # stars=levels
    for i in range(stars, 0, -1):
        print("*" * i)


# define a function
def rstar_pyramid():
    for i in range(levels, 0, -1):  # global variable
        print("*" * i)


# range(start, stop, step)

# scope
levels = int(input("Enter the desired pyramid height: "))

star_pyramid(levels)
rstar_pyramid(levels)

star_pyramid(levels)
rstar_pyramid(levels)

star_pyramid(levels)
rstar_pyramid(levels)
