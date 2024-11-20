import pygame
import pygame_menu
from src.dog import Dog


class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        ## Dog Model
        self.dog = Dog()
        self.sprites = pygame.sprite.Group((self.dog,))

        self.state = "START"

    def mainloop(self):
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endloop()
            elif self.state == "START":
                self.startloop()

    def startgame(self):
        self.state = "GAME"

    def startloop(self):
        self.menu = pygame_menu.Menu("Start Screen", self.width / 2, self.height / 2)
        self.menu.add.label("Click to start program", font_size=28)
        self.menu.add.button(
            "Start", self.startgame, align=pygame_menu.locals.ALIGN_CENTER
        )

        while self.state == "START":
            self.menu.update(pygame.event.get())
            self.menu.draw(self.screen)
            pygame.display.flip()

    def endloop(self):
        font_obj = pygame.font.SysFont(None, 48)
        msg = font_obj.render("Hope you enjoyed the puppies!", True, "pink")

        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.blit(msg, (50, 50))
            pygame.display.flip()

    def gameloop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.dog.change_image()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.state = "END"

            # update all sprite data
            self.sprites.update()
            self.dog.image = pygame.transform.smoothscale(
                self.dog.image, pygame.display.get_window_size()
            )
            self.dog.rect = self.dog.image.get_rect()
            # redraw the screen
            self.screen.fill("purple")
            self.sprites.draw(self.screen)

            pygame.display.flip()
