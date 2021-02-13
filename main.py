from pygame import *
from tkinter import *
from math import *

root = Tk()
root.withdraw()
init()
size = (1500, 900)
screen = display.set_mode(size)


RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW = (226, 244, 66)
LIGHTBLUE = (0, 255, 250)
PINK = (255, 0, 246)
PURPLE = (165, 0, 255)
MEGENTA = (255, 0, 144)
AQUA_BLUE = (2, 255, 191)
GREEN_YELLOW = (131, 255, 0)

screen.fill(WHITE)
display.flip()

def main():
    while True:
        for e in event.get():
            if e.type == QUIT:
                return
            if e.type == KEYDOWN and K_e:
                return



if __name__=='__main__':
    main()
