import pygame
from sprites import *
import settings



# Giving dimensions for the cell grid
cell_size = 40
cell_number= 20

# Using RGB tuples to describe colors
RED = (255, 11, 3)
BLUE = (50, 105, 194)
L_GREEN = (175,215,70)
D_GREEN = (161, 196, 69)
BLACK = (0,0,0)
pygame.font.init()
font = pygame.font.Font(None, 36)

game_font = pygame.font.Font(None, 36)