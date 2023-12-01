# sprites.py
import pygame
from snake_settings import *

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.segments = [SnakeSegment(100, 100), SnakeSegment(80, 100), SnakeSegment(60, 100)]
        self.direction = 'RIGHT'
        self.new_segment = False

    def update(self):
        if self.direction == 'RIGHT':
            new_head = SnakeSegment(self.segments[0].rect.x + 20, self.segments[0].rect.y)
        elif self.direction == 'LEFT':
            new_head = SnakeSegment(self.segments[0].rect.x - 20, self.segments[0].rect.y)
        elif self.direction == 'UP':
            new_head = SnakeSegment(self.segments[0].rect.x, self.segments[0].rect.y - 20)
        elif self.direction == 'DOWN':
            new_head = SnakeSegment(self.segments[0].rect.x, self.segments[0].rect.y + 20)

        self.segments.insert(0, new_head)

        if self.new_segment:
            self.segments.append(SnakeSegment(-20, -20))
            self.new_segment = False

    def grow(self):
        self.new_segment = True

    def collide_with_self(self):
        return any(segment.rect.colliderect(self.segments[0].rect) for segment in self.segments[1:])


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def respawn(self):
        self.rect.x = pygame.time.get_ticks() % (WIDTH - GRID_SIZE)
        self.rect.y = pygame.time.get_ticks() % (HEIGHT - GRID_SIZE)