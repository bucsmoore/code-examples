import random
import pygame   

class Point:
    # method
    def __init__(self, x=0, y=0, color=None):
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 50, 50)
        self.color = color
        # NEVER RETURN FROM __INIT__


    

    
        
