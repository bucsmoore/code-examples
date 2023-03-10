import json

import pygame


class Text:
    def __init__(self):
        # naive approach
        self.all_text = {
            "texta": """
                    some long text
            """,
            "textb": """
                    some more long text
            """,
        }

        # store text in plain text files
        lines = []
        textfile = open("assets/text.txt")
        for line in textfile:
            lines.append(line)

        # store text in JSON files
        self.high_score
        lines = []
        textfile = open("assets/text.json")  # serialization
        text_dictionary = json.load(textfile)
        self.title = text_dictionary["highscore"]

    def update_score(self, new_score):

        self.highscore = new_score
        textfile = open("assets/text.json", "r")
        text_dictionary = json.load(textfile)
        textfile.close()

        text_dictionary["highscore"] = self.highscore
        textfile = open("assets/text.json", "w")
        text_dictionary = json.dump(text_dictionary)
        textfile.write(text_dictionary)
        textfile.close()

    def remove_text(self):
        pass
