def percentage_to_letter(percent=99):
    """
    This is a function that returns a letter grade based on a percentage
    args: percent (int)
    return: letter (str)
    """
    let = "A"
    if 80 <= percent < 90:
        let = "B"
    elif 70 <= percent < 80:
        let = "C"
    elif 60 <= percent < 70:
        let = "D"
    elif percent < 60:
        let = "F"
    elif percent < 100:
        let = "ABC"
    return let


def is_passing(letter):  # boolean functions, is_* convention
    """
    This is a function that returns a letter grade based on a percentage
    args: None
    return: letter (str)
    """
    return letter.lower() in "abc"


def main():  # historically called main
    # no docstring
    grades = [90, 80, 70, 60, 50]
    for grade in grades:
        letter = percentage_to_letter(grade)
        if is_passing(letter):
            print("You passed!")
        else:
            print("Someone messed up your grades!")


main()
