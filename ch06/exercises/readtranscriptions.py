import json


def main():
    fileref = open("transcribe.json")
    data = json.load(fileref)
    for key, value in data.items():
        print(key, value)


main()
