import sys
import pygame
from pygame.locals import *

SCREEN_SIZE = (600, 500)

def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	pygame.display.set_caption("Test")

	while True:
		screen.fill((255, 0, 0))
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

if __name__ == "__main__":
	main()
