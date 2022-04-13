import pygame, pygame.freetype
from utility import *
pygame.init()
defaultfont = pygame.freetype.Font("ComicSansMS.ttf", 12)
defaultfont.origin = True
class textButton(pygame.Rect):
  def __init__(self, x,y,width,height, text = ''):
    pygame.Rect.__init__(self, x,y,width,height)
    self._fontcolor = colors['black']
    self._color = colors['white']
    self.text= text
  def _get_color(self):
    return self._color
  def _set_color(self, color):
    self._color = color
    return
  buttoncolor = property(_get_color,_set_color)
  def _get_font_color(self):
    return self._fontcolor
  def _set_font_color(self, color):
    self._fontcolor = color
  fontcolor = property(_get_font_color,_set_font_color)
  def add_text(self, string):
    return string + self.text
  def click(self):
    print("clicked {}".format(self.text))
  def draw(self, font = defaultfont, fcolor = None):
    if fcolor == None:
      fcolor = self._fontcolor
    self.window = pygame.display.get_surface()
    self._drawButton(self.window)
    self._drawText(self.window, font, fcolor)
  def _drawButton(self, window):
    pygame.draw.rect(window, self._color, self)
  def _drawText(self,window, font=defaultfont, fontcolor = None):
    text_rect = font.get_rect(self.text)
    font.render_to(window, tupleSubtract(self.center, (text_rect.width/2, 0)), self.text, fontcolor)

class Keyboard: 
  def __init__(self, x, y, width, height):
    rows = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BACKSPC'],['TAB', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],['CAPS', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", "ENTER"], ['SHIFT', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'SHIFT'], ['SPACE']]
    self.x = x
    self.y = y

    keyHeight = (height/ (len(rows)*1.05))
    self.keys = populate([], len(rows))
    for i in range(len(rows)):
      keyWidth = width / (countKeys(rows[i]))
      populate(self.keys[i], len(rows[i]))
      for j in range(len(rows[i])):
        self.keys[i][j] = textButton(self.x+keyWidth*countKeys(rows[i][:j]), self.y+i*keyHeight, keyWidth*countKeys([rows[i][j]])*.95,keyHeight, rows[i][j])
  def draw(self, buttonColor = colors['buttonbg'], fontColor = None, font = defaultfont):
    for row in self.keys:
      for button in row:
        button.color = buttonColor
        button.draw(font, fontColor)
def countKeys(lst):
  count = 0
  for key in lst:
    match key:
      case '`':
        count+=1/2
      case 'BACKSPC':
        count += 3/2
      case 'TAB':
        count += 4/3
      case '\\':
        count+=4/3
      case 'CAPS':
        count+=5/3
      case 'ENTER':
        count+=7/3
      case 'SHIFT':
        count+=2
      case 'SPACE':
        count+=6
      case _:
        count+=1
  return count
