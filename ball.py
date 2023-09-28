import images
import pygame
import settings

from pygame.sprite import Sprite
from enum import Enum
from pygame.locals import *


class BallType(Enum):
    DEFAULT = 0
    
class Ball(Sprite):
    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2 = pygame.Vector2(0, 0), 
                 radius = 8.0, ball_type = BallType.DEFAULT, image: pygame.Surface = None):
        
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        
        self.radius = radius
        self.diameter = radius * 2.0
        
        self.ball_type = BallType(ball_type)
        
        self.image = image
        if self.image is None:
            self.image = images.ball_default
        
        self.bounding_box = Rect(0, 0, 1, 1)
        self.alive = True

    def update(self):
        self.velocity.y += settings.delta_time * settings.gravity
        self.position += self.velocity * settings.delta_time
        
        self.check_screen_collisions()

    def draw(self):
        top_position = self.position.y - self.radius
        left_position = self.position.x - self.radius
        settings.screen.blit(self.image, (left_position, top_position))

    def check_screen_collisions(self):
        if self.position.x < self.radius or self.position.x > settings.SCREEN_WIDTH - self.radius:
            self.velocity.x = -self.velocity.x
        if self.position.y < self.radius:
            self.velocity.y = -self.velocity.y
        elif self.position.y > settings.SCREEN_HEIGHT + self.radius:
            self.alive = False