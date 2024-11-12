import json
import random


def main():
    fptr = open("data/myideas.json")
    ideas = json.load(fptr)
    print(ideas)
    print(random.choice(ideas))


main()
