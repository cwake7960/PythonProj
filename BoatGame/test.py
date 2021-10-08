import pygame
import math

pygame.init()
y = 60 # Height at which to start
width = 400
height = 400
surf = pygame.display.set_mode((width, height),
pygame.SRCALPHA)
surf.fill ((255,255,255))
y = 60 # Height at which to start

pygame.draw.arc (surf, (255, 0, 0), (100,100, 200, 200), math.pi/4 , math.pi)
pygame.display.update()
input()