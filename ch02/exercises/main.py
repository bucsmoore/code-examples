import pygame

pygame.init()

while True:
    for event in pygame.event.get():
        pass

    screen = pygame.display.set_mode()
    screen.fill("red")
    pygame.time.wait(500)  # in real GUI programs, you wouldn't use this
    pygame.display.flip()
    screen.fill("blue")
    pygame.display.flip()
    pygame.time.wait(500)
    screen.fill("purple")
    pygame.display.flip()
    pygame.time.wait(1000)

    break
