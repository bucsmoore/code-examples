import io

import pygame
import requests


class Dog(pygame.sprite.Sprite):
    """
    Dog class that represents a dog sprite in a Pygame application. The dog image is fetched from an online API and updated periodically.

    Attributes:
        image (pygame.Surface): The current image of the dog.
        rect (pygame.Rect): The rectangle representing the position and size of the dog image.

    Methods:
        __init__(): Initializes the Dog sprite and sets the initial image.
        change_image(): Fetches a new dog image from the online API and updates the sprite.
        update(): Periodically updates the dog image based on the game clock.
    """

    def __init__(self):
        super().__init__()
        self.change_image()

    def change_image(self):
        """
        Fetches a random dog image from the Dog CEO API and updates the object's image and rect attributes.

        This method sends a GET request to the Dog CEO API to retrieve a random dog image URL.
        It then downloads the image, loads it into a Pygame surface, and updates the object's
        image and rect attributes accordingly.
        ## ARGS
        None
        ## RETURN
        None
        """

        results = requests.get("https://dog.ceo/api/breeds/image/random")
        print(results.json())
        image = requests.get(results.json()["message"]).content
        self.image = pygame.image.load(io.BytesIO(image))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        """
        Update the state of the dog object.
        This method checks the current time in milliseconds since the pygame
        module was initialized. If the time is a multiple of 100 milliseconds,
        it calls the change_image method to update the dog's image.
        ## ARGS
        None
        ## RETURN
        None
        """

        if pygame.time.get_ticks() % 10000 == 0:
            self.change_image()
