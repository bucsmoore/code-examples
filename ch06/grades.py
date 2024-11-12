def percentage_to_letter(score=0):
    grade = "A"
    if 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif score < 60:
        grade = "F"
    return grade


def is_passing(letter=None):
    return letter in "ABC"


def main():
    print(is_passing(percentage_to_letter(70)))
    num = int(input("Enter your score: "))
    print(num, is_passing(percentage_to_letter(num)))


main()
