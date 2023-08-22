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
        self.lines = []
        textfile = open("assets/text.txt")
        for line in textfile:
            self.lines.append(line)
        self.font = pygame.font.SysFont(None, 48)
        self.update_display_text()

    def update_score(self, new_msg=None):
        if new_msg:
            self.lines.append(new_msg)

        textfile = open("assets/text.json", "w")
        text_dictionary = json.dump(self.lines)
        textfile.write(text_dictionary)
        textfile.close()

        self.msgs = []
        #convert the strings to a font object for display
        for m in self.lines():
            font_object = font.render(m, True, (255, 255, 255))
            



## Using your text class in the controller

...
 msg = Text()
    for m in msg:
        text = 
        screen.blit(text, (20, ypos))  # position is top left corner
        ypos += 60
...
