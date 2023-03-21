import json
import os
import random


def main():
    json_data = json.load(open("assets/ideas.txt", "r"))
    print(random.choice(json_data))


main()
