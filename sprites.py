import pygame, sys
from pygame.math import Vector2
from pygame import font
from random import randint
from settings import *
import os
pygame.font.init()

pygame.init()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100) # setting the speed at which the snake moves
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) # the dimensions of the grid
game_folder = os.path.dirname(__file__) #getting the needed images to play the game
#inspiration from movement: https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #creating a default length and position for the snake
        self.direction = Vector2(0,0) #creating the original direction [right] using vectors
        self.new_block = False #there should not be a new_block created now because the snake has not collided
    
    def draw_snake(self):
        for block in self.body: #iterating through every element of the snake's body to print it
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size) #rectangularly creating each part of the snake so that it fully occupies the required cells
            pygame.draw.rect(screen, BLUE, block_rect) #drawing it

    def move_snake(self):
        if self.new_block == True: # if a new block needs to be created (collision with fruit)
            body_copy = self.body[:] #creating a copy of the snake
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] #this removes the last block in the list because it is now the next one, and then a new block is inserted at the head
            body_copy.insert(0,body_copy[0] + self.direction) #adding a new position block for the head
            self.body = body_copy[:] #changing self.body
    
    def add_block(self):
        self.new_block = True # a new block needs to be created upon collision

#knowledge about Vector2: https://www.trccompsci.online/mediawiki/index.php/Vectors_in_PyGame

apple = pygame.image.load(os.path.join(game_folder, "apple.png")).convert_alpha()
class FRUIT:
    def __init__(self):
        self.x = randint(0,cell_number-1) #assigning a random position to the fruit
        self.y = randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y) #storing the x and y pos in a vector
    
    def randomize(self):
        self.x = randint(0,cell_number-1) #this function is called whenever the snake's head collides with the fruit, giving the fruit a new random position
        self.y = randint(0,cell_number-1) 
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        # fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size, cell_size) # creating a rectangle for the fruit that occupies a full sell
        # pygame.draw.rect(screen, RED, fruit_rect) #drawing the rectangle
        # Load the apple image
        apple_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "apple.png"))

        # Resize the apple image to match the cell size
        apple_img = pygame.transform.scale(apple_img, (cell_size, cell_size))

        # Create a rectangle for the fruit that occupies a full cell
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)

        # Blit the apple image onto the screen at the fruit position
        screen.blit(apple_img, fruit_rect)

    


class MAIN:
    def __init__(self):
        self.snake = SNAKE() #creating the objects so both the snake and fruit can be manipulated in the same class
        self.fruit = FRUIT()
        self.font = pygame.font.Font(None, 36) #creating a default font
        self.screen = screen
    def update(self):
        self.snake.move_snake() #moving the snake
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit() #doing it all one one function to make the main.py loop much clearer
        self.snake.draw_snake()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: #if the position of the fruit is the same as the head of the snake's body (the first element), there is a "collision"
            self.fruit.randomize() # randomize the position upon collision
            self.snake.add_block() # elongate the snake
    
    def check_fail(self):
        if not (0 <= self.snake.body[0].x < cell_number) or not (0 <= self.snake.body[0].y < cell_number): #checking if the snake's head goes past the borders of the screen
            self.game_over() 
        
        for block in self.snake.body[1:]: 
            if block == self.snake.body[0]: # if the snake's head has the same position as any part of the snake's body, meaning the snake is colliding with itself, game over.
                self.game_over()
    
    def game_over(self): #for now, just quitting the game
        self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #creating a default length and position for the snake
        self.snake.direction = Vector2(0,0) #creating the original direction [right] using vectors
        self.snake.new_block = False #there should not be a new_block created now because the snake has not collided
    def draw_grass(self):
        for row in range(cell_number): #iterating through the # of rows
            if row % 2 == 0: #if it's every second row
                for col in range(cell_number):
                    if col % 2 == 0: #and every 2nd column, draw a dark green rectangle (grid pattern)
                        pygame.draw.rect(screen, D_GREEN, pygame.Rect(col*cell_size, row * cell_size, cell_size, cell_size))
            else:
                for col in range(cell_number): # otherwise
                    if col % 2 != 0: #for every 2nd column (and odd row)
                        pygame.draw.rect(screen, D_GREEN, pygame.Rect(col*cell_size, row * cell_size, cell_size, cell_size))
    

    def draw_score(self):
        score_text = "Score: " + str(len(self.snake.body) - 3)
        score_surface = self.font.render(score_text, True, (255, 255, 255))  # You can change the color

        # Adjust the position where you want to display the score
        score_rect = score_surface.get_rect(center=(100, 50))  # You can adjust the coordinates

        # Blit the score onto the screen
        self.screen.blit(score_surface, score_rect)


main_game = MAIN()

