import pygame
pygame.init()


x = input('enter file name ')
print(x)
im = pygame.image.load(x)
width = im.get_width()
height = im.get_height()
surf = pygame.display.set_mode((width, height), pygame.SRCALPHA)
surf.fill((255,0,0))
surf.blit(im, (0,0))
pygame.display.update()
input()