import pygame
from tkinter import *

root = Tk()
root.withdraw()
pygame.init()

size = (1500, 900)
screen = pygame.display.set_mode(size)

black = 0, 0, 0


def main():
	while True:
		screen.fill(black)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()




if __name__=='__main__':
	main()