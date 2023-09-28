import pygame
import settings
background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
ball_default = pygame.image.load("images/ball.png")
ball_default = pygame.transform.scale(ball_default, (16, 16))
peg_default = pygame.image.load("images/peg.png")
peg_default = pygame.transform.scale(peg_default, (24, 24))