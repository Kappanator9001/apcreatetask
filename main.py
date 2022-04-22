"""
main.py
Main body of the program, actually giving it functionality

"""

import pygame
from buttons import *
from utility import *
pygame.init()
winSize = 500
#create square window
w = pygame.display.set_mode([winSize, winSize])
#make base color black rather than white by default
invertColorsDefault = True
if invertColorsDefault:
  invert(colors)
#read cache file for previous input
string = ''
with open('cache.txt', 'r') as file:
  for line in file:
    string+=line
#basic event loop variables
gaming = True
c= pygame.time.Clock()
#initialize keyboard
keyboard = Keyboard(0,300,winSize, 200)
#main loop
while gaming: 
  #event loop
  for event in pygame.event.get():
        #if close window, stop running program
        if event.type == pygame.QUIT:
            gaming = False
        #if the d key is pressed, invert the colors of everything
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_d:
            invert(colors)
            for row in keyboard.keys:
              for button in row:
                button.fontcolor = colors['black']
                button.buttoncolor = colors['black']
        #if there is a click, determine where it is, and if it's within the keyboard then the keyboard was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          if within((x,y), keyboard):
            string = keyboard.click(x,y, string)
          
  #reset screen from last frame, draw keyboard and text, cap framefrate and flip display        
  w.fill(colors['white'])
  keyboard.draw()
  renderText(string)
  c.tick(60)
  pygame.display.flip()

#write to cache file for next run
with open('cache.txt', 'w') as file:
  file.write(string)