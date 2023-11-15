import pygame
import random
import pygame_menu


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
            self.rect.x -= 3
        else:
            self.rect.x += 3

class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        ## Bouncing Ball Model
        self.ball = Ball(self.width / 2, self.height / 2, 100)
        self.sprites = pygame.sprite.Group((self.ball,))
        

    def mainloop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            self.sprites.update()
            # adjust the direction of the ball based on position
            if self.ball.rect.x < 0:
                self.ball.direction = "right"
            elif self.ball.rect.x > (self.width - self.ball.rect.width):
                self.ball.direction = "left"
            
            self.screen.fill("purple")

            self.sprites.draw(self.screen)
            
            pygame.display.flip()


def main():
    game = Controller()
    game.mainloop()


if __name__ == "__main__":
    main()
