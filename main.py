import pygame
from buttons import *
from utility import *
pygame.init()
winSize = 800
w = pygame.display.set_mode([winSize, winSize])
invertColorsDefault = True
gaming = True

button = textButton(0,0,100,100)
button2 = ellipseTextButton(200,100,30,50, 'amogus', colors['cyan'])
buttons = [button, button2]
while gaming: 
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          for button in buttons:
            button.tryClicked(x,y)
  w.fill(colors['white'])
  for button in buttons:
    button.draw()
  pygame.display.flip()
