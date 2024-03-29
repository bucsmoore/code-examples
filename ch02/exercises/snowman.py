import pygame

# Initialization
pygame.init()

screen = pygame.display.set_mode()
screen.fill("lightblue")
#  returns as a list of 2 items (w, h)
# dimensions = pygame.display.get_window_size()
# width = dimensions[0]
# height = dimensions[1]
width, height = pygame.display.get_window_size()

size = width / 4
pos = [width / 2, (height / 2) + size]

for _ in range(3):
    pygame.draw.circle(screen, "grey", pos, size + 5)
    pygame.draw.circle(screen, "white", pos, size)
    pos[1] = pos[1] - size
    size = size / 2
    pos[1] = pos[1] - size * 0.70

pygame.display.flip()
pygame.time.wait(3000)
