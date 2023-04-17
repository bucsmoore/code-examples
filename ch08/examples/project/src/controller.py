"""
file: main.py
"""
import pygame
from src import graph


class Controller:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode()
        self.graph = graph.Graph(self.display.get_width(), self.display.get_height())
        self.drawing = False
        
    def mainloop(self):
        while True:
            # eventloop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.graph.complement()
                    elif event.key == pygame.K_c:
                        self.graph.clear()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.drawing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.drawing = True
                elif event.type == pygame.MOUSEMOTION and self.drawing:
                    self.graph.add_point(event.pos[0], event.pos[1])

            # draw updates
            self.display.fill("white")
            self.display.blit(self.graph.x_axis, self.graph.x_axis_rect)
            self.display.blit(self.graph.y_axis, self.graph.y_axis_rect)

            for p in self.graph.points:
                self.display.blit(p.image, p.rect)

            # show display
            pygame.display.flip()
