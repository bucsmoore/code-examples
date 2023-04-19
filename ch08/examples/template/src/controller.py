import pygame

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background_color = (200, 200, 250)
        self.background.fill(self.background_color)


    def mainloop(self):
        # one time through the loop is one frame (picture)
        while True:  
            # check for events since the last time through the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            # update models

            # detect and respond to collisions

            # redraw
            self.background.fill(self.background_color)
            self.screen.blit(self.background, (0, 0))


            # update the screen
            pygame.display.flip()