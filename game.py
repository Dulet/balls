import pygame
import settings
import entities
import images
import random
from ball import Ball

GAME_WIDTH = settings.SCREEN_WIDTH
GAME_HEIGHT = settings.SCREEN_HEIGHT

def update():
    entities.update_balls()

def random_tuple():
    return random.random() * 2.0 - 1.0, random.random() * 2.0 - 1.0

def draw():
    settings.screen.fill((50, 50, 50))
    entities.draw_balls()

pygame.init()

settings.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

game_running = True
delta_time = 0.0
clock = pygame.time.Clock()

mouse_position = (0, 0)
while game_running:

    mouse_position = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            elif event.key == pygame.K_SPACE:
                circle_follow_mouse = False
                circle_falling = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                circle_follow_mouse = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                print("spawn")
                entities.balls.append(Ball(pygame.Vector2(event.pos[0], event.pos[1]), pygame.Vector2((random.random() * 200 - 1.0, random.random() * 200 - 1.0))))
                
    update()
    draw()
    
    pygame.display.flip()
    
    settings.delta_time = 0.001 * clock.tick(60)
    
    pygame.quit
