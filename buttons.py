"""
buttons.py
contains all button and button related functions for this program
"""
import pygame, pygame.freetype
from utility import *
pygame.init()
#default font is Comic Sans because I like it 
defaultfont = pygame.freetype.Font("ComicSansMS.TTF", 12)
defaultfont.origin = True
special_click_cases = ['SPACE', 'BACKSPC', 'CAPS', 'SHIFT', 'ENTER', 'TAB']
shift_caps = [False, False]
#used for creation of buttons on screen in pygame
class textButton(pygame.Rect):
  def __init__(self, x,y,width,height, text = ''):
    pygame.Rect.__init__(self, x,y,width,height)
    self._fontcolor = colors['black']
    self._color = colors['black']
    self.text= text
  #buttoncolor and fontcolor being properties just makes setting and getting them slightly easier and more convenient
  #allows values to be got and set just like normal variables (button.buttoncolor = ([color]))
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
  #called when the button is clicked
  #shift_caps is a effectively one variable but I needed it to have more scope than normal variables so it is a non-primitive type
  #tuple probably works here, but list works just fine
  #also adds the button's text to string [string] with the special cases called as needed, being the keys like space and enter that
  #aren't just as simple as adding their text to the rendered string
  #returns string back through so that it actually can update (primitive type)
  def click(self, string):
    if self.text in special_click_cases:
      return specialClickBehavior(string, self.text)
    upper = (shift_caps[1]+shift_caps[0])%2
    if shift_caps[0]:
      shift_caps[0] = False
    if upper:
      return string + self.text.upper()
    return string + self.text
  #draws the button on the pygame window
  #broken into 2 parts because I made them at different times, and for code clarity's sake
  #_drawButton draws the actual button part, and _drawText draws the text (shocking)
  #the "return" of the function is on the graphical window, with the button being rendered
  def draw(self, font = defaultfont, fcolor = None):
    if fcolor == None:
      fcolor = self._fontcolor
    self.window = pygame.display.get_surface()
    self._drawButton(self.window)
    self._drawText(self.window, font, fcolor)
  def _drawButton(self, window):
    pygame.draw.rect(window, self._color, self, 1)
  def _drawText(self,window, font=defaultfont, fontcolor = None):
    text_rect = font.get_rect(self.text)
    font.origin=True
    font.render_to(window, tupleSubtract(self.center, (text_rect.width/2, 0)), self.text, fontcolor)
#glorified array of buttons, modeled after the keyboard I am using on this pc
class Keyboard: 
  def __init__(self, x, y, width, height):
    rows = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BACKSPC'],['TAB', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],['CAPS', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", "ENTER"], ['SHIFT', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'SHIFT'], ['SPACE']]
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.keyHeight = (height/ (len(rows)*1.05))
    #prepopulating the lists allows me to reference things by index upon initial assignment
    #just appending things would've worked, but I like this way
    self.keys = populate([], len(rows))
    for i in range(len(rows)):
      keyWidth = width / (countKeys(rows[i]))
      populate(self.keys[i], len(rows[i]))
      for j in range(len(rows[i])):
        self.keys[i][j] = textButton(self.x+keyWidth*countKeys(rows[i][:j]), self.y+i*self.keyHeight, keyWidth*countKeys([rows[i][j]])*.95,self.keyHeight, rows[i][j])
  #iterates through the buttons in the keyboard and draws each of them
  def draw(self, buttonColor = colors['buttonbg'], fontColor = None, font = defaultfont):
    for row in self.keys:
      for button in row:
        button.color = buttonColor
        button.draw(font, fontColor)
  #when clicked, mouse position (x and y) and a string are passed in
  #determines what row was clicked by y position, and then iterates through each button in that row
  #if the clicked position is within any button, that button is signaled that it was clicked
  #edited string is then returned, or if a gap between the keys was clicked then the original string is returned
  def click(self, x, y, string):
    row = self.keys[int((y-self.y)//self.keyHeight)]
    for button in row:
      if within((x,y),button):
        return button.click(string)
    return string

#dictionary of all keys with abnormal key lengths, with names corresponding to their respective relative lengths
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
# used to size keys based on the amount of keys in that row of a keyboard
#allows custom sizing of keys on a case-by-case basis
#lst is a list of varying length
def countKeys(lst):
  count = 0
  
  for key in lst:
    if key not in special_length_cases:
      count+=1
    else: count+=special_length_cases[key]
      
  return count
#defines program behavior in the case that anything other than one of the letter or number keys is pressed
#string is a string, the text of the button being clicked
def specialClickBehavior(string, text):
  if text=='BACKSPC':
    return string[:len(string)-1]
  if text == 'TAB':
    return string+'    '
  if text == 'SPACE':
    return string+' '
  if text == 'CAPS':
    shift_caps[1] = not shift_caps[1]
    return string
  if text == 'SHIFT':
    shift_caps[0] = not shift_caps[0]
    return string
  if text == 'ENTER':
    return string+'\n'
#renders the entire text that has been inputted to screen
#split into lines by '\n', which is only inputted if enter key is pressed
#text is the text to rendered, font is the font to render with
def renderText(text='', font = defaultfont):
  w = pygame.display.get_surface()
  font.origin = False
  text= text.split('\n')
  for line in text:
    font.render_to(w, (0,text.index(line)*(font.size+1)), line, colors['black'])