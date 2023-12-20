#This file was created by Akshaj Bozza

'''
Title: Snake Game

Goals: 
1) have the snake body move with the arrow keys and have the head switch direction when the arrow key is pressed (and then have the body follow)
2) have an apple that randomly generates after it collides with the snake
3) have the snake expand in length each time it consumes an apple
4) terminate the game when the snake either collides with itself or with the borders of the screen

I wanted to solve the problem of movement, since the snake's movement is somewhat complicated. In addition, I wanted to solve the issue of elongation. From my previous experiences in programming
'''
#general inspiration (more for the entire game rather than a specific concept is in the README file)

# importing the necesscary contents for the game
import sprites
import settings
from sprites import *
from settings import *
import pygame, sys
pygame.font.init()

pygame.init() #initializing pygame

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #if the user wants to exit pygame, it can do so
        if event.type == SCREEN_UPDATE:
            main_game.update() #moving the snake, checking for collision continuously 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snake.direction.y != 1: #if the sprite is not currently moving down (so that it can't collide with itself)
                    main_game.snake.direction = Vector2(0,-1) #changing the direction vector to reflect the necesscary change in x or y position that needs to occur 
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: #-1 is up in pygame (while positive is down)
                if main_game.snake.direction.y != -1: #if the sprite is not currently moving 
                    main_game.snake.direction = Vector2(0,1) #the move snake just adds the position and direction vectors to get a new position 
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: #if the sprite is not currently moving left
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0) 
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: #if the sprite is not currently moving right
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill(D_BLUE) # This is the color for the screen
    main_game.draw_elements() # drawing the original snake body with three default blocks and a randomly generated fruit
    pygame.display.update() 
    