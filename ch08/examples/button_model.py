import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, width=175, height=75, color=(200, 0, 200), text="Press Me"):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.color = color
        self.image.fill(self.color)
        
        text_color = (255-color[0], 255-color[1], 255-color[2]) #complimentary color
        self.message = pygame.font.SysFont(None, 36).render(text, True, text_color)
        
        self.image.blit(self.message, (20, 20))

    def highlight(self):
        highlight_color = []
        for i, c in enumerate(self.color):
            if c+50 < 255:
                highlight_color.append(c+50) 
            else:
                highlight_color.append(255)
        self.image.fill(highlight_color)
        self.image.blit(self.message, (20, 20))

    def color_default(self):
        self.image.fill(self.color)
        self.image.blit(self.message, (20, 20))


## EXAmPLE Button Creation

if __name__ == "__main__":

    b1 = Button(color=(200, 200, 200), text="Press Me")
    b2 = Button(color=(200, 0, 0), text="Don't Press Me")