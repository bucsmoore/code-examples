import turtle


def percentage_to_letter(score=0):
    """
    converts a percentage grade to a letter grade
    params: score:int
    return: str
    """
    letter = "A"
    if 80 <= score < 90:
        letter = "B"
    elif 70 <= score < 80:
        letter = "C"
    elif 60 <= score < 70:
        letter = "D"
    else:
        letter = "F"
    return letter


def is_passing(letter=None):
    # Docstring
    """
    checks if the letter is a passing grade
    params: score:int
    return: str
    """
    return letter.upper() in "ABC"


# if "__main__" == __name__:
#     main()
# result = print("hi")
# None: NoneType
# has functions not procedures
# print(result)
def main():
    letter = percentage_to_letter(80)  # letter = 'B'
    passing = is_passing(letter)
    print(passing)
    print(percentage_to_letter.__doc__)


main()
