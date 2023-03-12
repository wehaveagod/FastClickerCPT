#Importing Libraries
import pygame
import button
import random as rand
import math

#Game Window Dimensions
HEIGHT = 600
WIDTH = 800

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Game Window Preliminaries
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fast Clicker CPT Project')

def run_game():
	#Clear screen
	SCREEN.fill(BLACK)

	#Running Boolean Variable
	running = True

	#Circle Characteristics
	CIRCLE_TIME = 1000
	CIRCLE_RADIUS = 15

	#Variables for Circle and Time Tracking
	circle_on_screen = False
	points = 0
	circle_center = None
	time_on_screen = None

	#Text Display for Points
	FONT = pygame.font.Font('freesansbold.ttf', 16)
	points_text = FONT.render(str(points), True, WHITE, BLACK)
	TEXT_RECT = points_text.get_rect()
	TEXT_RECT.center = (WIDTH - 20, HEIGHT - 20)

	#Game will run until "running" boolean is false
	while running:
		#Displaying the points text on the screen
		SCREEN.blit(points_text, TEXT_RECT)

		#Create a New Circle if the Screen is Empty
		if(not circle_on_screen):
			time_on_screen = pygame.time.get_ticks()
			circle_center = (rand.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS), rand.randint(CIRCLE_RADIUS, HEIGHT - CIRCLE_RADIUS))
			pygame.draw.circle(SCREEN, WHITE, circle_center, CIRCLE_RADIUS)
			circle_on_screen = True
			pygame.display.update()

		#Remove Circle if it is on Screen for More than CIRCLE_TIME
		elif(pygame.time.get_ticks() - time_on_screen >= CIRCLE_TIME):
			pygame.draw.circle(SCREEN, BLACK, circle_center, CIRCLE_RADIUS)
			circle_on_screen = False
			pygame.display.update()

		#Event Loop
		for event in pygame.event.get():
			#Quit game if Window is Closed
			if event.type == pygame.QUIT:
				running = False

			#Detect if Mouse if Pressed
			if event.type == pygame.MOUSEBUTTONUP:
				#Get the Mouse Position
				click_pos = pygame.mouse.get_pos()

				#Calculate if the Mouse Click is Inside the Circle and Within the Time Limit
				if(math.dist(circle_center, click_pos) <= CIRCLE_RADIUS and pygame.time.get_ticks() - time_on_screen <= CIRCLE_TIME):
					#Increment Points and Update Points Display
					points += 1
					points_text = FONT.render(str(points), True, WHITE, BLACK)
					SCREEN.blit(points_text, TEXT_RECT)

					#Removing the Circle After it is Pressed
					pygame.draw.circle(SCREEN, BLACK, circle_center, CIRCLE_RADIUS)
					circle_on_screen = False
					pygame.display.update()
	pygame.quit()

def start_screen():
	START_BUTTON = button.Button(color = RED, x = 300, y = 200, width = 200, height = 100, text = "Start")
	START_BUTTON.draw(SCREEN)
	pygame.display.update()

	start_click = False
	while not start_click:
		for event in pygame.event.get():
			if(event.type == pygame.MOUSEBUTTONUP and START_BUTTON.is_over_mouse(pygame.mouse.get_pos())):
				start_click = True
			if(event.type == pygame.QUIT):
				pygame.quit()

start_screen()
run_game()