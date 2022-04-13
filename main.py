import pygame
from buttons import *
from utility import *
pygame.init()
winSize = 800
w = pygame.display.set_mode([winSize, winSize])
invertColorsDefault = True
if invertColorsDefault:
  invert(colors)
fileName = 'cache.txt'
file = open(fileName, 'r')
gaming = True

keyboard = Keyboard(0,500,winSize, 300)
while gaming: 
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_d:
            invert(colors)
            for row in keyboard.keys:
              for button in row:
                button.fontcolor = colors['black']
                button.buttoncolor = colors['white']
        elif event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          #estimate row by y position, then use list slicing with countKeys to figure out what key is being pressed
  w.fill(colors['white'])
  keyboard.draw()
  pygame.display.flip()
