import pygame
from buttons import *
from utility import *
pygame.init()
winSize = 600
w = pygame.display.set_mode([winSize, winSize])
invertColorsDefault = True
gaming = True

button = textButton(0,0,100,100)
button2 = ellipseTextButton(200,100,30,50, 'amogus', colors['cyan'])
while gaming: 
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
  w.fill(colors['white'])
  button.draw()
  button2.draw()
  pygame.display.flip()
