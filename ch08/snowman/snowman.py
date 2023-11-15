import random

import pygame


class Snowman:

    def __init__(self, x, y):
        self.color = [
            random.randint(0, 255), 
            random.randint(0, 255), 
            random.randint(0, 255)
            ]
        self.speed = 5
        #makes background transparent pygame.SRCALPHA
        self.image = pygame.Surface( (40, 70) , pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        # Draw the snowman on the model surface
        head_radius = 5
        self.head = pygame.draw.circle(
            self.image, 
            self.color, 
            (self.rect.width/2, head_radius), 
            head_radius
            )
        body_radius = 10
        self.body = pygame.draw.circle(
            self.image, 
            self.color, 
            (self.rect.width/2, self.head.bottom+body_radius), 
            body_radius
            )
        bottom_radius = 20
        self.bottom = pygame.draw.circle(
            self.image, self.color, 
            (self.rect.width/2, self.body.bottom+bottom_radius), 
            bottom_radius
            )

    def update(self):
        size = pygame.display.get_window_size()
        if self.rect.y <  10:
            self.direction = "DOWN"
        elif self.rect.bottom > size[1]:
            self.direction = "UP"
        if self.direction == "UP":
            self.rect.y = self.rect.y - 1
        else:
            self.rect.y = self.rect.y + 1

        if self.rect.x < 0:
            self.rect.x += random.randint(0, self.speed)
        elif self.rect.right > size[0] :
            self.rect.x += random.randint(-self.speed, 0)
        else:
            self.rect.x += random.randint(-self.speed, self.speed)