#This file was created by Akshaj Bozza

'''
Title: Snake Game

Goals: 
1) have the snake body move with the arrow keys and have the head switch direction when the arrow key is pressed (and then have the body follow)
2) have an apple that randomly generates after it collides with the snake
3) have the snake expand in length each time it consumes an apple
4) terminate the game when the snake either collides with itself or with the borders of the screen

MAYBE
1) adding power-ups such as a score multiplier or one that expands the size of the screen or one that increases/decreases the speed of the snake
2) adding some obstacles (maybe not feasible if the snake achieves a longer length) -- maybe one to reduce score without reducing length
3) sound-effects
4) letting the player customize the look of the snake before playing

'''

import pygame, sys
from pygame.math import Vector2
from random import randint

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (50, 105, 194), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True



class FRUIT:
    def __init__(self):
        self.x = randint(0,cell_number-1)
        self.y = randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)
    
    def randomize(self):
        self.x = randint(0,cell_number-1)
        self.y = randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size, cell_size)
        pygame.draw.rect(screen, (255, 11, 3), fruit_rect)
    


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    
    def check_fail(self):
        if not (0 <= self.snake.body[0].x < cell_number) or not (0 <= self.snake.body[0].y < cell_number):
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()

    

pygame.init()
cell_size = 40
cell_number=20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill((175,215,70)) # This is the color for the screen
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
    