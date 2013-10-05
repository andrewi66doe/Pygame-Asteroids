__author__ = 'Andrew'
import pygame
import math

class Player:
    image = None

    width = 30
    height = 30

    x_pos = 0
    y_pos = 0
    direction = 0
    angle = 0

    velocity = 0

    def __init__(self, x, y, velocity):
        self.x_pos = x
        self.y_pos = y
        self.velocity = velocity
        self.image = pygame.Surface((30, 30))

    def update(self):
        self.x_pos += math.sin(math.radians(self.direction))*self.velocity
        self.y_pos += math.cos(math.radians(self.direction))*self.velocity
        temp_image = pygame.transform.rotate(self.image, self.angle)
        self.image = temp_image.copy()

