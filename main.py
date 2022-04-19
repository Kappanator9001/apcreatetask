import pygame
from buttons import *
from utility import *
pygame.init()
winSize = 500
w = pygame.display.set_mode([winSize, winSize])
invertColorsDefault = True
if invertColorsDefault:
  invert(colors)
fileName = 'cache.txt'
file = open(fileName, 'r')
gaming = True
c= pygame.time.Clock()
keyboard = Keyboard(0,300,winSize, 200)
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
          if within((x,y), keyboard):
            keyboard.click(x,y, "")
          
          
  w.fill(colors['white'])
  keyboard.draw()
  renderText()
  c.tick(60)
  pygame.display.flip()
file.close()