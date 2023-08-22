def multiply(x, y):  # x=5, y=0
    """
    multiplies two numbers without using `*`
    args: x (int), y (int)
    returns: (int)
    """
    accumulator = 0
    for _ in range(y):
        accumulator = accumulator + x
    return accumulator


def exponent(x, y):  # x=5, y=0
    accumulator = 1  # ""
    for _ in range(y):
        accumulator = accumulator * x
    return accumulator


def square(x):
    # return multiply(x, x)
    return exponent(x, 2)


def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(multiply(x, y))
    result = exponent(x, y)
    print(result)
    result = square(x)
    print(result)
    print(multiply.__doc__)


main()


def build_str(character_list):  # character_list = []
    """
    ghdfulsdg;oV;O
    """

    new_str = ""
    for ch in character_list:
        new_str = new_str + ch
    return new_str  # ""
