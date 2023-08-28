# The below code fills the screen with 3 colors of your choosing.
# After each color, it waits 1000 milliseconds before continuing.
import pygame

# Initialize Pygame
pygame.init()
background = pygame.display.set_mode()

# Set the color of the background to red and wait 1 second
color = (255, 0, 0)
background.fill(color)
pygame.display.flip()

pygame.time.wait(1000)

# Set the color of the background to green and wait 1 second
color = (0, 255, 0)
background.fill(color)

pygame.display.flip()

pygame.time.wait(1000)

# Set the color of the background to blue and wait 1 second
color = (0, 0, 255)
background.fill(color)
pygame.display.flip()

pygame.time.wait(1000)

pygame.quit()
quit()
