# x = 1
# y = 10

# while x < 100:
#     # event loop
#     x += 1

#     # updates
#     if x % y == 0:
#         print("clicked")
#         x = 1


import pygame

# class vs model


class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        self.color = (50, 50, 50)
        self.image = pygame.surface.Surface((width, height))
        self.rect = self.image.get_rect()

    def update(self):
        for idx, c in enumerate(self.color):
            self.colors[idx] = (c + 1) % 256
        self.image.fill(self.colors)


LIMIT = 10


class Controller:
    def __init__(self):
        # setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = Background(self.screen.get_size())
        self.mygroup = pygame.Group()
        self.mygroup.add(self.background)
        self.state = "menu"
        self.click = 1

    def mainloop(self):
        while True:
            if self.state == "menu":
                self.menuloop()
                # print(self.state)
            elif self.state == "game":
                self.gameloop()

    def menuloop(self):
        while self.state == "menu":
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "game"

    def gameloop(self):
        """
        menu elements must be defined before the mainloop
        """
        while self.state == "game":  # one time through the loop is one frame (picture)
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "menu"
                elif event.type == pygame.MOUSEMOTION:
                    if self.button.rect.collidepoint(event.pos):
                        self.button.highlight()
                    else:
                        self.button.color_default()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        click += 1

            # update
            if click % LIMIT == 0:
                # dosomething()
                click = 1
            self.mygroup.update()

            # redraw
            self.mygroup.draw()

            self.screen.blit(self.background, (0, 0))

            # display
            pygame.display.flip()
