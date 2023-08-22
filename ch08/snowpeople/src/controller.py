import pygame
from src.snowman import Snowman


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background_color = (200, 200, 250)
        self.background.fill(self.background_color)

        self.snowpeoples = pygame.sprite.Group()
        self.max_snowpeoples = 20

        number_of_snowpeoples = 5
        interval = self.screen.get_width() // (number_of_snowpeoples + 1)
        x = interval

        for _ in range(number_of_snowpeoples):
            s = Snowman(x, self.screen.get_height() / 2)
            self.snowpeoples.add(s)
            x += interval

    def mainloop(self):
        # one time through the loop is one frame (picture)
        while True:
            # check for events since the last time through the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for s in self.snowpeoples:
                        if s.rect.collidepoint(event.pos):
                            s.kill()

            # UPDATES
            for s in self.snowpeoples:
                if not s.rect.colliderect(self.screen.get_rect()):
                    s.kill()

            if len(self.snowpeoples) <= 0:
                pygame.quit()
                exit()

            for s in self.snowpeoples:
                # spritecollide(sprite, group, dokill)
                result = pygame.sprite.spritecollide(s, self.snowpeoples, False)

                if len(result) > 1 and len(self.snowpeoples) <= self.max_snowpeoples:
                    s2 = Snowman(s.rect.x, s.rect.y)
                    self.snowpeoples.add(s2)

            # update models
            self.snowpeoples.update()

            # detect and respond to collisions

            # redraw
            self.background.fill(self.background_color)
            self.screen.blit(self.background, (0, 0))

            self.snowpeoples.draw(self.screen)

            # update the screen
            pygame.display.flip()
