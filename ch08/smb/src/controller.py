import pygame
from src.cloud import Cloud
from src.enemy import Enemy
from src.player import Player


class Controller:
    def __init__(self):
        pygame.init()
        pygame.event.pump()

        self.screen = pygame.display.set_mode()

        self.p1 = Player()
        self.p2 = Player()
        self.clouds = pygame.sprite.Group()
        for _ in range(3):
            c = Cloud()
            self.clouds.add(c)

        self.enemies = pygame.sprite.Group()

    def mainloop(self):
        self.player = self.p1
        while True:
            pass
            # 1. event loop
            for event in pygame.events.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                ## handle any important events ##
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.is_jumping_up = True

            enemies = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for enemy in enemies:
                #handle collision

            # 2. Updates
            self.player.jump()
            # 3. Redraw
            self.clouds.draw()
            # completely overlay the screen
            self.background = pygame.image.load("assets/background.png")
            self.screen.blit(self.background, (0, 0))

            # 4. Display
