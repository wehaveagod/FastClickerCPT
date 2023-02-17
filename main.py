#Import pygame package
import pygame
  
#Initializing imported module
pygame.init()

#Initializing constants
HEIGHT = 600
WIDTH = 600
  
# Specififying window characteristics
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fast Clicker CPT Project')

#Running boolean variable
running = True
  
#Keep game running until running boolean is false
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False