import random
import settings
import images
from pygame.sprite import Sprite
import pygame

class ObstacleBase(Sprite):
    def __init__(self, position):
        super(ObstacleBase, self).__init__()
        self.position = position
        self.image = None
        if self.image is None:
            self.image = images.peg_default
        self.health = 1
    
    def hit(self):
        pass
    
    def draw(self):
        settings.screen.blit(self.image, (int(self.position[0]), int(self.position[1])))

class Peg(ObstacleBase):
    def __init__(self, position):
        super().__init__(position)
        
        self.color = (255, 0, 0)
        

        
    