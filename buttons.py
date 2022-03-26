import pygame, pygame.freetype
from utility import *
pygame.init()

class textButton(pygame.Rect):
  def __init__(self, x,y,width,height, text = '', color = colors['black'], fontcolor=  None):
    
    pygame.Rect.__init__(self, x,y,width,height)
    self.color = color
    self.text= text
    if fontcolor == None:
      fontcolor = invert(color)
    self.fontcolor = fontcolor
  def add_text(self, string):
    return string + self.text
  def tryClicked(self, x,y):
    rel_x, rel_y = x-self.x, y-self.y
    clicked = rel_x>=0 and rel_x<=self.width and rel_y>=0 and rel_y<=self.height
    if clicked: 
      self._click()
  def _click(self):
    pass
  def draw(self, fcolor = None):
    if fcolor == None:
      fcolor = self.fontcolor
    self.window = pygame.display.get_surface()
    self._drawButton(self.window)
    #self._drawText(font, fcolor)
  def _drawButton(self, window):
    pygame.draw.rect(window, self.color, self)
  def _drawText(self,window, font):
    pass
    #font.renderto(window, )
class ellipseTextButton(textButton):
  def __init__(self, x,y,width,height, text = '', color = colors['black'], fontcolor=  None):
    super().__init__(x,y,width,height, text, color, fontcolor)
  def _drawButton(self, font):
    window = pygame.display.get_surface()
    pygame.draw.ellipse(window, self.color, self)
