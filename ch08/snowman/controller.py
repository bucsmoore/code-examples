import pygame
from snowman import Snowman


#controller class
class SnowControl:
    
    def __init__(self):
        # Initialize the game engine
        pygame.init()

        # Set the height and width of the screen
        self.screen = pygame.display.set_mode()

        # Get width and height of a window as a list of 2 items [w, h]
        size_list = pygame.display.get_window_size()
        self.width = size_list[0]
        self.height = size_list[1]

        self.snowpeoples = pygame.sprite.Group()
        self.max_snowmen = 10000000000000

        number_of_starting_snowpeople = 2
        interval = self.width/(number_of_starting_snowpeople+1)
        xpos = interval
        for _ in range(number_of_starting_snowpeople):
            new_sm = Snowman(xpos, self.height/2)
            self.snowpeoples.add(new_sm)
            xpos += interval

    def mainloop(self):
        
        ### 1. EVENTS  ###
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for s in self.snowpeoples:
                    if s.rect.collidepoint(event.pos):
                        s.kill() #remove from all Groups and delete

        ### 2. UPDATE  ###
        
        #Remove snowmen that go offscreen
        for s in self.snowpeoples:
            if not s.rect.collide_rect(self.background.get_rect()):
                s.kill()

        #quit if no snowpeople left
        if len(self.snowpeoples) == 0:
            pygame.quit()
            exit()

        for s in self.snowpeoples:
            result = pygame.sprite.spritecollide(s, self.snowpeoples, False)
            if len(result) > 1 and len(self.snowpeoples) <= self.max_snowmen:
                sm = Snowman(s.rect.x, s.rect.y)
                self.snowpeoples.add(sm)

        ### 3. REDRAW  ###
        
        self.background.fill(self.background_color)
        self.screen.blit(self.background, (0, 0))

        self.snowpeoples.draw(self.screen)

        ### 4. DISPLAY  ###
        
        pygame.display.flip()