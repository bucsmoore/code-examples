import pygame

pygame.init()
screen = pygame.display.set_mode()
screen.fill("red")
pygame.display.flip()
pygame.time.wait(1000)
screen.fill("green")
pygame.display.flip()
pygame.time.wait(1000)
screen.fill("blue")
pygame.display.flip()
pygame.time.wait(1000)
