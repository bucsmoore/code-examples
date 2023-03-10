import pygame
import random

############################
#
# Below is an example of a Pygame program using multiple surfaces in a single model
# - You should have 1 primary surface that all surfaces for that object are blitted to
#
# The below example does not use the Sprite class or have any events to keep it simple.
#
# Although the entire program is in 1 file, keep in mind that in a full program, each 
# of the classes below should be in their own file.
#
############################

def random_color_generator():
    red = random.randrange(0, 256)
    blue = random.randrange(0, 256)
    green = random.randrange(0, 256)
    return [red, blue, green]

class Snowman:
    
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((200, 350))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.image.fill("purple")
        
        red = random.randrange(0, 256)
        blue = random.randrange(0, 256)
        green = random.randrange(0, 256)
        self.direction= "UP"
        self.draw_snowman()


    def draw_snowman(self):
        """
        Draws a snowman onto the primary surface for the object

        I put this into a separate method to break it up. Since it
        is only being called in the init, I could have put the code 
        in there.
        
        However, sometimes we break code into sperate functions
        to make it easier to read and understand, not for functional 
        reasons. 
        """
        self.color = random_color_generator()
        
        head_radius = 15
        head = pygame.draw.circle(self.image, self.color, (self.rect.width/2, head_radius), head_radius)
        
        #Draw the body
        body_radius = 25
        body = pygame.draw.circle(self.image, self.color, (self.rect.width/2, head.bottom+body_radius), body_radius)
        
        bottom_radius = 50
        bottom = pygame.draw.circle(self.image, self.color, (self.rect.width/2, body.bottom+bottom_radius), bottom_radius)
 
    def update(self):
        """
        We can have an update method to call for updates that should happen every frame
        This often contains the movement updates for the AI/NPC objects
        """
        if self.rect.y <  50:
            self.direction = "DOWN"
        elif self.rect.y > 150:
            self.direction = "UP"
        if self.direction == "UP":
            self.rect.y = self.rect.y - 1 
        else:
            self.rect.y = self.rect.y + 1
        self.rect.x += random.randrange(-1, 2)

        
        
class Controller:

    def __init__(self):
        # Initialize the game engine
        pygame.init()

        # Set the height and width of the screen
        self.screen = pygame.display.set_mode()

        # Get width and height of a window as a list of 2 items [w, h]
        size_list = pygame.display.get_window_size()
        width = size_list[0]
        height = size_list[1]

        self.number_of_snowpeoples = 3
        spacing_interval = 0
        self.snowpeoples = []
        for snowpeople in range(self.number_of_snowpeoples):
            self.snowpeoples.append(Snowman(spacing_interval, 0))
            spacing_interval += (width+1)/self.number_of_snowpeoples

    def mainloop(self):
        while True:

            ## Update our Models
            for snowpeople in self.snowpeoples:
                snowpeople.update()
                
            # update the screen with what we've drawn.
            # Clear the screen and set the screen background
            self.screen.fill([0, 0, 0]) # https://g.co/kgs/yKQbSu
          
            for snowpeople in self.snowpeoples:
                self.screen.blit(snowpeople.image, snowpeople.rect)
            
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()


def main():
    controller = Controller()
    controller.mainloop()
main()