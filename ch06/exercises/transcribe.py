# JavaScript Object Notation

import json


def main():
    open("transcribe.json", "w").close()
    key = input("Access Key:")
    text = input("Please enter some text to record:")
    transcriptions = {}
    while key and text:
        transcriptions[key] = text
        key = input("Access Key:")
        text = input("Please enter some text to record:")
    print(transcriptions)
    fileref = open("transcribe.json", "w")
    json.dump(transcriptions, fileref)
    fileref.close()
    print("You can find your text in the transcribe.txt file")


main()
