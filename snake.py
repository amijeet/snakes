import pygame
import sys
from random import seed 
from random import randint

from pygame.locals import*
pygame.init()
BLUE = (0,255,0)
WHITE = (255,255,255)
RED = (255,0,0)
DISPLAY = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
clock.tick(30)
snake = [[200,200], [210,200], [220,200]]



def draw_snake(snake):
	for s in snake:
		pygame.draw.rect( DISPLAY, BLUE, [s[0], s[1], 10, 10], 0 )

def mouse():
	mousex = randint(0,40)*10
	mousey = randint(0,40)*10
	pygame.draw.rect( DISPLAY, RED, [mousex, mousey, 10, 10], 0 )


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		else:
			mouse()
			draw_snake(snake)

			pygame.display.update()
			pygame.display.flip()
			pygame.time.delay(2000)
			pygame.quit()
			sys.exit()
