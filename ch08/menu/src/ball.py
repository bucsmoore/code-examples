import pygame



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()

        self.direction = "left"
        self.size = size
        
        self.image = pygame.Surface((size, size), pygame.SRCALPHA, 32).convert_alpha()
        self.rect = pygame.draw.circle(
                self.image,
                "yellow",
                (size/2, size/2),
                self.size/2,
            )
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.direction == "left":
            self.rect.x -= 1
        else:
            self.rect.x += 1