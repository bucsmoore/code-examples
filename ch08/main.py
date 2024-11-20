import pygame


class Maze(pygame.sprite.Sprite):
    def __init__(self, maze_file):
        self.maze_text = open(maze_file).read()

    def build_maze(self):
        for c in self.maze_text:
            pass
