import pygame
import settings
import entities
import images
import random
from ball import Ball
from obstacle import Peg

def create_balls():
    if len(entities.pegs) < 20:
        entities.pegs.append(Peg((random.randint(100, 540), random.randint(600, 920))))

def update():
    entities.update_balls()
    create_balls()

def random_tuple():
    return random.random() * 2.0 - 1.0, random.random() * 2.0 - 1.0

def draw():
    settings.screen.blit(images.background, (0, 0))
    entities.draw_balls()
    entities.draw_pegs()