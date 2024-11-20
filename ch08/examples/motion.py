import json
import random

import pygame

## This intentionally does not directly use any of the
## additional helper classes from Pygame such as Sprites
## or Surfaces to keep it as simple as possible.


class Ball:
    def __init__(self, x, y, size, color=None):
        self.x = x
        self.y = y
        self.size = size
        self.direction = "up"
        self.color = color

    def get_color(self):
        if self.color:
            return self.color
        else:
            ## List Comprehension
            # https://realpython.com/list-comprehension-python/
            return [random.randrange(256) for i in range(3)]

    def move(self):
        if self.direction == "up":
            self.y -= 1
        else:
            self.y += 1

    def save_state(self):
        # write out state
        ball_state = self.__dict__
        fptr = open("assets/last_state.json", "w")
        json.dump(fptr, ball_state)

    def load_state(self):
        # read in state
        fptr = open("assets/last_state.json")
        self.__dict__ = json.loads(fptr)


class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        size = pygame.display.get_window_size()

        self.width = size[0]
        self.height = size[1]

        self.colors = {"purple": [150, 25, 150]}

        ## Bouncing Ball Model
        self.ball = Ball(self.width / 2, self.height / 2, 50)

    def mainloop(self):
        while True:
            # update the ball's position
            self.ball.move()

            # adjust the direction of the ball based on position
            if self.ball.y < 0:
                self.ball.direction = "down"
            elif self.ball.y > self.height:
                self.ball.direction = "up"

            ## Check the limit, if outside of screen, change direction

            self.screen.fill(self.colors["purple"])

            pygame.draw.circle(
                self.screen,
                self.ball.get_color(),
                (self.ball.x, self.ball.y),
                self.ball.size,
            )
            pygame.display.flip()


def main():
    game = Controller()
    game.mainloop()


if __name__ == "__main__":
    main()
