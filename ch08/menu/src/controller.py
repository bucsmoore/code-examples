import pygame

import pygame_menu

from src.ball import Ball

class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        ## Bouncing Ball Model
        self.ball = Ball(self.width / 2, self.height / 2, 100)
        self.sprites = pygame.sprite.Group((self.ball,))

        self.state = "START"

    def mainloop(self):

        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endloop()
            elif self.state == "START":
                self.startloop()
        

    def startloop(self):
        self.menu = pygame_menu.Menu("Start Screen", self.width/2, self.height/2)
        self.menu.add.label("Click to start program", font_size=28)
        self.menu.add.button("Start", self.startgame, align=pygame_menu.locals.ALIGN_CENTER)

        while self.state == "START":
            self.menu.update(pygame.event.get())
            self.menu.draw(self.screen)
            pygame.display.flip()

            
    def endloop(self):
        font_obj = pygame.font.SysFont(None, 48)
        msg = font_obj.render("You won!", True, "yellow")

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.rect.collidepoint(event.pos):
                        self.state = "END"

            self.sprites.update()
            # adjust the direction of the ball based on position
            if self.ball.rect.x < 0:
                self.ball.direction = "right"
            elif self.ball.rect.x > (self.width - self.ball.rect.width):
                self.ball.direction = "left"
            
            self.screen.fill("purple")

            self.sprites.draw(self.screen)
            
            pygame.display.flip()

    def startgame(self):
        self.state = "GAME"