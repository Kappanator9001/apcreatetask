import pygame
from buttons import *
from utility import *
pygame.init()
winSize = 800
w = pygame.display.set_mode([winSize, winSize])
invertColorsDefault = True
gaming = True

keyboard = Keyboard(0,500,winSize, 300)
while gaming: 
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_d:
            invert(colors)
        elif event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          
  w.fill(colors['white'])
  keyboard.draw()
  pygame.display.flip()
