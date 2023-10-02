import random
import settings
import images
from pygame.sprite import Sprite
import pygame

class ObstacleBase(Sprite):
    def __init__(self, position, velocity):
        super(ObstacleBase, self).__init__()
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)

        self.image = None
        
        self.radius = 8
        self.diameter = self.radius * 2
        
        if self.image is None:
            self.image = images.peg_default

        self.health = 1
        
    def hit(self):
        pass
    
    def update(self):
        self.velocity.y += settings.delta_time * settings.gravity
        self.position += self.velocity * settings.delta_time
        
        self.position += self.velocity * settings.delta_time
        
        
        self.check_collisions()
        
    def check_collisions(self):
        if self.position.x < self.radius or self.position.x > settings.SCREEN_WIDTH - self.radius:
            self.velocity.x = -self.velocity.x
            if self.position.x < self.radius:
                self.position.x += 10
            elif self.position.y > settings.SCREEN_WIDTH - self.radius:
                self.position.x -= 10
                
        elif self.position.y < self.radius:
            self.velocity.y = -self.velocity.y
            
        elif self.position.y > settings.SCREEN_HEIGHT - self.radius:
            self.velocity.y *= -0.9
            self.position.y -= 10
            self.velocity.x += (random.randint(0, 50))
            self.alive = False
            
    def draw(self):
        settings.screen.blit(self.image, (int(self.position.x), int(self.position.y)))

class Peg(ObstacleBase):
    def __init__(self, position, velocity):
        super().__init__(position, velocity)
        
        self.color = (255, 0, 0)
        

        
    