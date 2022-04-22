"""
utility.py
Library of general utility functions for this program
"""
import pygame,random,pygame.freetype
pygame.init()
#universal reference point for colors in program
#if these are changed then changes across program, which is useful for when inverting colors
colors = {
  'white': (255,255,255),
  'black' : (0,0,0),
  'cyan' : (0,255,255),
  'buttonbg': (0,0,0)
}
#replaces a color with its opposite, or replaces all colors in a dictionary or list with their opposites
#used to create a darkmode effect across the program
#program only ever returns the color's inverse, but will modify non-primitive typed variables
def invert(color):
    if type(color)==dict:
        for key in color:
            color[key]=invert(color[key])
    elif type(color)==list:
        for c in color:
            c=invert(c)
    else:
        #(255,255,255)-(x,y,z)
        #(255-x,255-y,255-z)
        #a color's inverse is given by (255,255,255)- color
        return tupleSubtract((255,255,255),color)
#adds 2 tuples together, index by index
#example: (0,0,50) + (50, 100, 200) = (50, 100, 250)
#useful for adding colors together
def tupleAdd(t1,t2):
    t1=list(t1)
    t2=list(t2)
    fintuple= []
    for i in range(len(t1)):
        fintuple.append(t1[i]+t2[i])
    return tuple(fintuple)
#subtracts 2 tuples from each other
#example: (200,200,200) - (50,10,20) = (150,190,180)
#primarily used for inverting colors 
def tupleSubtract(t1,t2):
    t1=list(t1)
    t2=list(t2)
    fintuple= []
    for i in range(len(t1)):
        fintuple.append(t1[i]-t2[i])
    return tuple(fintuple)
#gets value at index index of tuple t
#may be unnecessary, but I think I wrote this because I was having issues with getting idices of tuples
def tupleIndex(t,index):
    t=list(t)
    return t[index]
#prepopulates a list lst out to num indices for the purposes of allowing indices to be referenced before assignment 
def populate(lst, num):
   for i in range(num):
     lst.append([])
   return lst
#checks if position pos (tuple) is within an object obj (any object with a width, height, x, and y attributes)
#examples of possible objects for obj: pygame.Rect, textButton, Keyboard
#returns boolean of whether position is within the object's bounds
def within(pos, obj):
  x,y = pos
  bounds=[x>obj.x, x<(obj.x+obj.width), y>obj.y, y<(obj.y+obj.height)]
  return(all(bounds))
