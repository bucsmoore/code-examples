import json


def main():
    # fptr = open("data/myideas.txt", "r")
    # lines = list(fptr.readlines())
    # fptr.close()
    # fptr = open("data/myideas.json", "w")
    # # stores a list or a dictionary
    # json.dump(lines, fptr)
    # fptr.close()

    # fptr = open("data/myideas.txt", "r")
    # # fptr.read() #read in entire file as a single string
    # # fptr.readline() #read in a single line as a  string
    # # fptr.readlines() #read in entire file as a list of string strings
    # for i in fptr:
    #     print(i, end="")
    # fptr.close()

    mydata = {"name": "Jill", "age": "5", "pets": ["Dog", "Cat", "Elephant"]}

    fptr = open("data.json", "w")
    json.dump(mydata, fptr, indent=2)
    fptr.close()


main()
