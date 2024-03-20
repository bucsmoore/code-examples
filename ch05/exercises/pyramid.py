def star_pyramid(num_stars):
    for i in range(num_stars):
        print("*" * (i + 1))


def rstar_pyramid(num_stars):
    for i in range(num_stars, 0, -1):
        print("*" * (i))


star_pyramid(5)
star_pyramid(100)
rstar_pyramid(1000)
rstar_pyramid(1000000)
rstar_pyramid(int(input("Please enter a number")))
