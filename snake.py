import pygame
import sys
from random import seed 
from random import randint

from pygame.locals import*
pygame.init()
GREEN = (0,255,0)
WHITE = (255,255,255)
RED = (255,0,0)
DISPLAY = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
FPS = 10
snake = [[200,200], [210,200], [220,200]]
x = 100
y = 100
direction = 0

def draw_snake():
	for s in snake:
		pygame.draw.rect( DISPLAY, GREEN, [s[0], s[1], 10, 10], 0 )
def draw_mouse(mouse_co):
	pygame.draw.rect( DISPLAY, RED, [mouse_co[0], mouse_co[1], 10, 10], 0 )

def random():
	mousex = randint(0,40)*10
	mousey = randint(0,40)*10
	R = [mousex, mousey]
	return R

def movement(direction):
	if (direction == 2):
		A = [ snake[0][0]-10, snake[0][1] ]
		snake.insert(0, A)
		snake.pop()
		draw_snake()
	if (direction == 3):
		A = [ snake[0][0]+10, snake[0][1] ]
		snake.insert(0, A)
		snake.pop()
		draw_snake()
	if (direction == 1):
		A = [ snake[0][0], snake[0][1]-10 ]
		snake.insert(0, A)
		snake.pop()
		draw_snake()
	if (direction == -1):
		A = [ snake[0][0], snake[0][1]+10 ]
		snake.insert(0, A)
		snake.pop()
		draw_snake()

def Draw():
	for X in range(200):
		pygame.draw.rect(DISPLAY, GREEN, [x, y, 10, 10], 0)
		clock.tick(3)
		pygame.display.update()
		x += 1
		y += 1

B = random()
mousecoordinates = B
flag = 1
while True:
	clock.tick(FPS)
	DISPLAY.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_UP:
				direction = 1
			if event.key == K_DOWN:
				direction = -1
			if event.key == K_RIGHT:
				direction = 3
			if event.key == K_LEFT:
				direction = 2
		
	if (direction == 1):
		movement(direction)
	if (direction == -1):
		movement(direction)
	if (direction == 3):
		movement(direction)
	if (direction == 2):
		movement(direction)

	if (snake[0] == B):
		snake.insert(0, B)
		B = random()
		draw_mouse(B)
	draw_snake()
	if (flag == 1):
		draw_mouse(B)
	pygame.display.update()
	


