import pygame, sys, time, random
from random import seed 
from random import randint

from pygame.locals import*
pygame.init()

W = 400
H = 400
DISPLAY = pygame.display.set_mode((W,H))
pygame.display.set_caption('Dedicated to the snakes of KGP')
clock = pygame.time.Clock()
FPS = 10
snake = [[20,20], [20,21], [20,22]]
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
LIME = (0, 255, 255)
BLUE = (0, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 128, 0)
MAROON = (128, 0, 0)
PINK = (255, 20, 147)
colours = [YELLOW, RED, LIME, BLUE, CYAN, MAGENTA, GREEN, MAROON, PINK]
flag = 1
direction = 0

def random_apple():
	count = 0
	A = [[0 for i in range(2)] for j in range(1444)]
	for i in range(1, 39):
		for j in range(1, 39):
			A[count][0] = i
			A[count][1] = j
			count += 1
	print(len(A))
	for x in snake:
		A.remove(x)
		print(x)
	return [ A[randint(0,len(A)-1)][0] , A[randint(0,len(A)-1)][1] ]
	#pygame.draw.rect(DISPLAY, RED, (A[randint(0,len(A)-1)][0]*10, A[randint(0,len(A)-1)][1]*10, 10, 10))

def display_snake():
	for s in snake:
		pygame.draw.rect(DISPLAY, YELLOW, (s[0]*10, s[1]*10, 10, 10))

def movement(direction):
	if (direction == 2): #left
		B = [ snake[0][0]-1, snake[0][1] ]
		snake.insert(0, B)
		snake.pop()
		display_snake()
	if (direction == 3): #right
		B = [ snake[0][0]+1, snake[0][1] ]
		snake.insert(0, B)
		snake.pop()
		display_snake()
	if (direction == 1): #up
		B = [ snake[0][0], snake[0][1]-1 ]
		snake.insert(0, B)
		snake.pop()
		display_snake()
	if (direction == -1): #down
		B = [ snake[0][0], snake[0][1]+1 ]
		snake.insert(0, B)
		snake.pop()
		display_snake()

def draw_apple(r_apple):
	colour_number = randint(0, len(colours)-1)
	pygame.draw.rect(DISPLAY, colours[colour_number], (r_apple[0]*10, r_apple[1]*10, 10, 10))
	pygame.display.update()

r_apple = random_apple()
print("initial coordinates of apple")
print(r_apple)
running = True
while(running):
	clock.tick(FPS)
	DISPLAY.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if ( (event.key == K_UP and direction != -1) or (direction == 1 and event.key == K_DOWN) ):
				direction = 1
			if ( (event.key == K_DOWN and direction != 1) or (direction == -1 and event.key == K_UP) ):
				direction = -1
			if ( (event.key == K_RIGHT and direction != 2) or (direction == 3 and event.key == K_LEFT) ):
				direction = 3
			if ( (event.key == K_LEFT and direction != 3) or (direction == 2 and event.key == K_RIGHT) ):
				direction = 2
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				flag = 1
		
	if (direction == 1): #up
		movement(direction)
	if (direction == -1): #down
		movement(direction)
	if (direction == 3): #right
		movement(direction)
	if (direction == 2): #left
		movement(direction)

	if (snake[0] == r_apple):
		if (direction == 1):
			snake.insert(0, [r_apple[0], r_apple[1]-1])
		if (direction == -1):
			snake.insert(0, [r_apple[0], r_apple[1]+1])
		if (direction == 3):
			snake.insert(0, [r_apple[0]+1, r_apple[1]])
		if (direction == 2):
			snake.insert(0, [r_apple[0]-1, r_apple[1]])
		print(snake)
		r_apple = random_apple()
		draw_apple(r_apple)

	display_snake()
	draw_apple(r_apple)
	