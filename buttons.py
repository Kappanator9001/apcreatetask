import pygame, pygame.freetype
from utility import *
pygame.init()
defaultfont = pygame.freetype.Font("ComicSansMS.TTF", 12)
defaultfont.origin = True
special_click_cases = ['SPACE', 'BACKSPC', 'CAPS', 'SHIFT', 'SHIFT']
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
  def click(self, string=''):
    print("clicked {}".format(self.text))
    if self.text in special_click_cases:
      return specialClickBehavior(string, self.text)
    return string + self.text
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
    self.width = width
    self.height = height
    self.keyHeight = (height/ (len(rows)*1.05))
    self.keys = populate([], len(rows))
    for i in range(len(rows)):
      keyWidth = width / (countKeys(rows[i]))
      populate(self.keys[i], len(rows[i]))
      for j in range(len(rows[i])):
        self.keys[i][j] = textButton(self.x+keyWidth*countKeys(rows[i][:j]), self.y+i*self.keyHeight, keyWidth*countKeys([rows[i][j]])*.95,self.keyHeight, rows[i][j])
  def draw(self, buttonColor = colors['buttonbg'], fontColor = None, font = defaultfont):
    for row in self.keys:
      for button in row:
        button.color = buttonColor
        button.draw(font, fontColor)
 #estimate row by y position, then use list slicing with countKeys to figure out what key is being pressed
 #given y is within Keyboard
        
  def click(self, x, y, string):
    row = self.keys[int((y-self.y)//self.keyHeight)]
    for button in row:
      if within((x,y),button):
        button.click(string)
      
    
special_length_cases= {
  '`': 1/2,
  'BACKSPC':3/2,
  'TAB':4/3,
  '\\': 4/3,
  'CAPS': 5/3,
  'ENTER':7/3,
  'SHIFT':2,
  'SPACE':6
}
def countKeys(lst):
  count = 0
  
  for key in lst:
    if key not in special_length_cases:
      count+=1
    else: count+=special_length_cases[key]
      
  return count
def specialClickBehavior(string, text):
  
  if text=='BACKSPC':
    return string[:len(string)-1]
  return string
def renderText(text=''):
  pass