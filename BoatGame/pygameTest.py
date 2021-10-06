import tkinter
import pygame

pygame.init()

surf = pygame.display.set_mode((800, 600))
c =pygame.Color(255, 0, 0)
surf.fill((255,255,255))
y = 60
for n in range(0 ,27):
    for x in range(0,400):
        surf.set_at((x, y), c)
    y = y +20
c = (200, 0 ,0)
for y in range(0,400):
    surf.set_at((25, y), c)

pygame.display.update()

open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

pygame.quit()
quit()
