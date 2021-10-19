# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import pygame
import math
import random

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (170, 0, 150)
SQUARE = (250, 107, 255)

# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################


class Box:
    def __init__(self, display, x, y, width, height):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0

    def draw_box(self):
        pygame.draw.rect(self.display, SQUARE, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.speed

        if self.x <= 0:
            self.x = 0
        elif self.x + self.width >= DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width


pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# create player
player_width = 50
x_loc = (DISPLAY_WIDTH - player_width)/2
y_loc = DISPLAY_HEIGHT - 2*player_width

# create enemies
enemy_width = 50
enemy_list = []
for i in range(7):
    x_coord = i * enemy_width // 6
    random_y = random.randrange(-100, 0, 5)
    print(random_y)
    enemy_list.append(Box(screen, x_coord, random_y, enemy_width, enemy_width))

player = Box(screen, x_loc, y_loc, player_width, player_width)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.speed = 5
            elif event.key == pygame.K_LEFT:
                player.speed = -5
        elif event.type == pygame.KEYUP:
            player.speed = 0

    screen.fill(PINK)

    player.draw_box()
    player.update()

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()

        if enemy.y > DISPLAY_HEIGHT:
            enemy.y = random.randrange(-100, 0, 5)
            enemy.y_speed = random.randint(1, 5)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
