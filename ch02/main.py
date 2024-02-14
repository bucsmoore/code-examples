import pygame

pygame.init()
screen = pygame.display.set_mode()
pygame.draw.circle(screen, "red", [200, 150], 10)
pygame.draw.circle(screen, "red", [200, 200], 30)
pygame.draw.circle(screen, "red", [200, 250], 50)
pygame.display.flip()
pygame.time.wait(1500)