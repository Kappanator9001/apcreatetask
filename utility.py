import pygame,random,pygame.freetype
pygame.init()
colors = {
  'white': (255,255,255),
  'black' : (0,0,0),
  'cyan' : (0,255,255),
  'buttonbg': (0,0,0)
}

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
        return tupleSubtract((255,255,255),color)
def tupleAdd(t1,t2):
    t1=list(t1)
    t2=list(t2)
    fintuple= []
    for i in range(len(t1)):
        fintuple.append(t1[i]+t2[i])
    return tuple(fintuple)
def tupleSubtract(t1,t2):
    t1=list(t1)
    t2=list(t2)
    fintuple= []
    for i in range(len(t1)):
        fintuple.append(t1[i]-t2[i])
    return tuple(fintuple)
def tupleIndex(t,index):
    t=list(t)
    return t[index]
def populate(lst, num):
   for i in range(num):
     lst.append([])
   return lst
def within(pos, obj):
  x,y = pos
  bounds=[x>obj.x, x<(obj.x+obj.width), y>obj.y, y<(obj.y+obj.height)]
  return(all(bounds))
